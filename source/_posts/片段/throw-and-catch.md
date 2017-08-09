---
title: throw and catch
categories:
  - 片段
mathjax: false
date: 2017-08-09 15:48:39
tags:
 - c/c++
---

> File : throw and catch.cpp
> Type : c/c++
> Brief : throw and catch for const string

<!-- more -->

---

```c++
#include <iostream>
using std::cout;
using std::endl;
/*
    void fun() throw() 表示fun不允许抛出任何异常，即fun是异常安全的。
    void fun()              表示fun可以抛出任何形式的异常。
    void fun() throw(...)   (只针对msvc++)表示fun可以抛出任何形式的异常。
    void fun() throw(exceptionType) 表示fun只能抛出exceptionType类型的异常。
*/

void hello()
{
    cout << "hello world" << endl;
    
    throw "it's so bored to throw hello";
}

void runHello()
{
    try
    {
        hello();
    }
    catch(const char *str)          // 必须加const
    {
        cout << str << endl;
        cout << "no zuo no die" << endl;
    }
}

int main(int argc, char *argv[])
{
    runHello();
    
    return 0;
}
```
