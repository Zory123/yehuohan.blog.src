---
title: Qt多线程中的信号-槽
categories:
  - 杂记
mathjax: false
tags:
  - qt
date: 2017-10-09 19:57:42
---

Qt的信号槽机制用好了非常方便。最近在多线程中使用信号槽时遇到了些问题，查下问题的原因，才知道还未得connect精髓。

<!-- more -->

## connect中被忽略的参数

connect用得最的多形式就是：

```
connect(sender, signal, receiver, slot);
```

其实，connect还有一个Qt::ConnectionType参数，只是它带有默认值，且多数情况下，默认值足够了，所以最少有机会去了解。Qt::ConnectionType的可选值如下：

 - Qt::AutoConnection:
默认值，使用这个值则连接类型会在信号发送时决定。如果接收者和发送者在同一个线程，则自动使用Qt::DirectConnection类型。如果接收者和发送者不在一个线程，则自动使用Qt::QueuedConnection。

 - Qt::DirectConnection: 槽函数会在信号发送的时候直接被调用，槽函数运行于信号发送者所在线程。效果看上去就像是直接在信号发送位置调用了槽函数。这个在多线程环境下比较危险，可能会造成奔溃。

 - Qt::QueuedConnection: 槽函数在控制回到接收者所在线程的事件循环时被调用，槽函数运行于信号接收者所在线程。发送信号之后，槽函数不会立刻被调用，等到接收者的当前函数执行完，进入事件循环之后，槽函数才会被调用。多线程环境下一般用这个。

 - Qt::BlockingQueuedConnection: 槽函数的调用时机与Qt::QueuedConnection一致，不过发送完信号后发送者所在线程会阻塞，直到槽函数运行完。接收者和发送者绝对不能在一个线程，否则程序会死锁。在多线程间需要同步的场合可能需要这个。

 - Qt::UniqueConnection: 这个flag可以通过按位或（|）与以上四个结合在一起使用。当这个flag设置时，当某个信号和槽已经连接时，再进行重复的连接就会失败。也就是避免了重复连接。


## 线程间使用信号槽进行通信

 - 使用元数据类型：
在线程间使用信号槽进行数据通信时，需要使用元数据类型。Qt的元数据类型，如int double QString 等。
如果要用自己定义的数据类型，需要在connect前将其注册为元数据类型：

```
#include <QMetaType>

qRegisterMetaType<new_type>("new_type");
connect(sender, signal(new_type), receiver, slot(new_type));
```

 - 使用Qt::DirectConnection类型
此方法官方不推荐使用，认为其不安全。
