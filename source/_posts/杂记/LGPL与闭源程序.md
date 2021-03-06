---
title: '[转]LGPL与闭源程序'
categories:
  - 杂记
mathjax: false
date: 2017-11-01 11:46:54
tags:
---

[文章原链接：豆子空间-LGPL与闭源程序](http://devbean.blog.51cto.com/448512/313477)

<!-- more -->

---
## 介绍

最近一直在学习 Qt。Qt 有两个许可证：LGPL 和商业协议。这两个协议在现在的 Qt 版本中的代码是完全一致的（潜在含义是，Qt 的早期版本，商业版的 Qt 通常包含有一些开源版本所没有的库，比如 QtSingleApplication 这个库）。所以现在对于普通开发人员和部分商业公司来说，使用 LGPL 版本的 Qt 可以节省很大的开销。这两个版本最大的区别在于，前者是免费的，后者是收费的。既然代码都是一致的，所以费用就要是用来购买 Qt 的售后服务和培训等等相关服务。

现在我们是来说一下版权的问题。LGPL 是一个开源协议，因此，有人会担心 LGPL 能否用于开发闭源程序，能够拿来卖钱。尽管现在国内有些公司不是很重视这方面的问题，不过，如果你违反了协议，某一天被别人发来一纸律师函的时候，真的是欲哭无泪了哦。所以，我们还是先来研究一下这个协议，LGPL 究竟能不能用于开发闭源程序。

以下内容是我查找了 N 多网站总结出来的，因为豆子不是律师，所以 LGPL 协议基本看不懂。究竟怎样去理解这个协议，还是希望能够有专业人士说出来。这里就算做是一种抛砖引玉吧！尽管没有十分的确定，但是这里所说的理解基本也是八九不离十的了。

至于什么是 LGPL 协议，这里就不再多说了，我们关心的是，如果使用 LGPL 协议开发商业程序。请注意，这里所说的闭源程序，是指不以某种形式开放源代码，也就是说，用户（包括其他开发者）不能获取其源代码的程序。首先说明一点， ***LGPL协议是一个商业友好的协议***。这里的含义是，你可以用 LGPL协议开发商业程序，当然也可以是非商业的闭源程序。但是，它是有一些限制的。这就是我们要讨论的重点。

既然我们已经对其定性，那么我们直接进入主题：
- ***使用 LGPL 协议开发闭源程序，如果你使用动态链接的形式，那么，你可以以任何形式发布你的应用程序，商业的、非商业的、开源的、非开源的，随你。***
- ***如果你因某种原因必须静态链接一个基于 LGPL 协议发布的库（一下我们简称为 LGPL 库），那么，你有义务进行下面的工作：***
 - *你必须在你的文档中说明，你的程序中使用了 LGPL 库，并且说明这个库是基于 LGPL 发布的；*
 - *你必须在你的应用程序发布中包含一份 LGPL协议，通常就是那个文本文件；*
 - *你必须开放使用了 LGPL 库代码的所有代码，例如某些封装器。但是，其他使用这些封装器的代码就不需要开放了；*
 - *你必须包含你的应用程序的余下部分的目标文件（通常就是我们所说的 .o 等等），或者是其他等价的文件。源代码并不是必须的。*

是不是很难理解呢？我们详细的说一下。
 - 第一条很容易理解；
 - 第二条也很容易理解，你可以在这里找到 LGPL 协议的内容，复制下来随你的程序一起发布就可以了。
 - 第三条就不那么好理解了。简单来说，LGPL协议要求，如果你的类使用了LGPL库的代码，那么必须把这个类开源。例如，如果你的程序 app.exe 每个源文件都使用了 LGPL 库的代码，那么你的所有源代码都要开源。为了避免这种情况，我们通常编写一个封装器，把 LGPL库的代码封装起来，这样就只需要开放这个封装器的代码，而其他使用了这个封装器的代码就不需要开放。
 - 第四条是对第三条的一种补充：那些使用了封装器的程序不需要开源，但是你必须把你编译的那些中间文件开放出来，Windows 下就是那些 .o 文件。

---
## 实例
你很奇怪，为什么 LGPL协议要这样规定呢？LGPL 所做的工作是，它保证了用户能够有这样一种能力：修改你使用 LGPL 库函数的方式（那些封装器就是你使用 LGPL库的方式，那些已经开源了），重新编译这些代码，然后重新对程序进行连接（连接所需要的目标文件也是包含了的，这是第四条规定的），就可以得到一个新的可执行程序。

好了，如果你还不明白如何使用，我们来看一个例子。
假设我们使用一个名为 Lib 的库，这个库是基于 LGPL协议发布的。如果你使用 Lib.dll 做动态链接（Windows 下），好，一切 OK。无论你的程序怎么样，你都可以做你所做的事情。
我们主要是来看，如果你要使用静态链接，那么你需要如何组织你的代码。如果你有一个 main.cpp（我们假设所有 Lib 库的函数都是用了 lib_ 前缀）：

```
// main.cpp 
int main() { 
    lib_init(); 
    lib_do_something(); 
    lib_done(); 
    lib_close(); 
 
    return 0; 
} 
```

现在你已经完成了 main.cpp，但是你必须把它开源！因为它使用了 LGPL 库的代码。这是上面第三条规定的。我不想把它开源，怎么办呢？好，我们建一个新的文件 lib_wrapper.cpp:

```
void my_lib_init() 
{ 
    lib_init(); 
} 
 
void my_lib_do_something() 
{ 
    lib_do_something(); 
} 
 
void my_lib_done() 
{ 
    lib_done(); 
} 
 
void my_lib_close() 
{ 
    lib_close(); 
} 
```

在 main.cpp 中，我们做相应的修改:

```
int main() { 
    my_lib_init(); 
    my_lib_do_something(); 
    my_lib_done(); 
    my_lib_close(); 
 
    return 0; 
} 
```

现在，main.cpp 不再是直接使用了 LGPL 库的代码了，因此它不需要开源，而我们的封装器 lib_wrapper.cpp 必须开源。
好，编译一下我们的程序，你会得到 main.o（Windows 下）这个目标文件。
在最终程序的发布中，你需要包含一下文件：
 - *一份文档，其中声明：这个程序使用了 Lib库，这个库是基于 LGPL 协议发布的;*
 - *LGPL.txt;*
 - *lib_wrapper.cpp*
 - *main.o*

这样，用户可以通过修改 lib_wrapper.cpp  的内容改变你使用 LGPL 库的方式，例如：

```
void my_lib_done() 
{ 
    lib_done(); 
    lib_close(); 
} 
 
void my_lib_close() 
{ 
    // lib_close(); 
} 
```

然后编译这个 lib_wrapper.cpp，最终重新链接。一个新的可执行程序诞生啦！
好了，这就是在使用 LGPL库开发闭源程序所需要遵守的东西了。还是建议大家能够遵守协议，尊重作者的劳动成果哦~
