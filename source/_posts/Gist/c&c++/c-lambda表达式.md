---
title: 'c++:lambda表达式'
categories:
  - Gist
mathjax: false
date: 2018-01-18 15:46:56
tags:
---

> File : lambda.cpp
> Type : c++
> Brief : c++ lambda简单用法

<!-- more -->

---

```cpp
#include <iostream>
#include <functional>
using std::cout;
using std::endl;

/*
 * 基本用法
 * [] () mutable ->type {}
 * -- -- ------- ------ --
 *  1  2   3      4      5
 *
 *  1: 捕获值列表
 *  2: 传入参数列表
 *  3: 可修改标示符
 *  4: 返回值
 *  5: 函数体
 *
 * []     : 不捕获
 * [&]    : 按引用捕获作用域中的所有变量
 * [=]    : 按值捕获作用域中的所有变量
 * [=,&n] : n按引用捕获，其它变量按值捕获
 * [m,&n] : m按值捕获，n按引用捕获
 * [this] : 捕获当前类中this指针
 */

struct Num
{
    int num;
    std::function<int()> func;

    Num(int n) : num(n)
    {
        this->func = [this]()->int{std::cout << "num: " << this->num; return this->num;};
    }
};

int main()
{
    // 简单示例
    int xy =  [](int x, int y)->int{return x+y;} (4,5);
    auto add = [&xy](int a)->int{xy += a; return xy;};
    cout << "xy: " << xy << endl;
    add(1);
    cout << "xy++: " << xy << endl;

    // 有mutable参数或都->type时，()不可省略
    int m = 0, n = 0;
    // m为按值捕获，若要修改m，需要加mutable
    auto f1 = [m] () mutable ->int {return ++m;};
    auto f2 = [&m] () ->int {return ++m;};
    auto f3 = [=] () mutable {n ++; return ++m;};

    cout << "f1: " << f1() << endl;     // 将f1看成一个类对象，成员变量为f1.m
    cout << "f1: " << f1() << endl;     // 在定义f1时所捕获的m，即为f1.m的初始值
    cout << "f1: " << f1() << endl;     // 连续调用3次f1()，即m自增3次
    cout << "m: " << m << endl;

    cout << "f2: " << f2() << endl;
    cout << "f2: " << f2() << endl;
    cout << "m: " << m << endl;

    cout << "f3: " << f3() << endl;
    cout << "m: " << m << endl;

    // 使用function对象
    std::function<int(double)> plus = [](double a)->int{return (int)a;};
    cout << "plus: " << plus(2.33) << endl;
    Num num(9);
    num.func();
}
```
