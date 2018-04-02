---
title: Qt结束线程
categories:
  - Gist
mathjax: false
tags:
  - qt
date: 2017-10-09 18:59:23
---

> File : thread.h
> Type : qt
> Brief : Qt结束线程

<!-- more -->

---

```cpp
#include <QThread>
#include <QMutex>
class thread : public QThread
{
    Q_OBJECT
public:
    thread(QObject *parent = 0): QThread(parent){}

    void exitThread()
    {
        requestInterruption();                  // 发出终止线程请求
        quit();
        wait();
    }

protected:
    void run() {
        //while(1)                              // 不要用while(1)
        while (!isInterruptionRequested())      // 没有终止线程请求时，就相当于while(1)了
        {
        }
    }
};
```

[参考文章](http://blog.csdn.net/caoshangpa/article/details/62421334)，里面写了利用QMutex和bool实现requestInterruption()的原理。
