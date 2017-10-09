---
title: c/c++:function pointer
categories:
  - Gist
mathjax: false
date: 2017-08-09 13:28:41
tags:
 - c/c++
---

> File : func_ptr.cpp
> Type : c/c++
> Brief : function pointer

<!-- more -->

---

```c++
#include <iostream>
using namespace std;

void hello(void) 
{ 
    cout << "你好!" << endl;; 
}

void bye(void) 
{ 
    cout << "再见！" << endl; 
}

void ok(void) 
{
    cout << "好的！" <<  endl; 
}

//用于处理参数和返回值的形式都一样，但是功能不确定的一组函数，可以使用。
//比如算术运算符，加、减、乘、除，都可以用typedef int (*calc)(int,int)代表。

// 函数指针
typedef void (*funcptr)(void);
typedef void (A::*class_funcptr)(void);     // 指向类A的成员函数指针

void speak(int id)
{
   funcptr words[3] = {&hello, &bye, &ok};
   funcptr fun = words[id];
   (*fun)();
}

int main()
{
    speak(1);
    speak(2);
    
    return 0;
}

```
