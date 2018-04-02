---
title: 'c/c++:在main之前运行指定代码'
categories:
  - Gist
mathjax: false
tags:
  - c/c++
date: 2018-03-18 23:40:05
---

> File : before_main.cpp
> Type : c/c++
> Brief : 在main之前运行指定代码

<!-- more -->

---

```cpp
#include <iostream>

// 全局变量赋值
int bm_func1()
{
    std::cout << "Before main: func1\n";
    return 0;
}
int _bmf1 = bm_func1(); // 或者 static int _bmf1 = bm_func1();
int _bmf2 = []() //或者 static int _bmf2 = []()
{
    std::cout << "Before main: func2\n";
    return 0;
}();

// gcc,clang 可用
void __attribute__((constructor)) bm_func3()
    //或者static void __attribute__((constructor)) bm_func3()
{
    std::cout << "Before main: func3\n";
};

// 全局类的构造函数
class BmClass
{
public:
    BmClass()
    {
        std::cout << "Before main: class\n";
    }
};
BmClass _bmc; // 或者 static BmClass _bmc;


int main()
{
    std::cout << "In main function\n";
    return 0;
}
```
