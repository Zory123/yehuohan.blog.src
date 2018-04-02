---
title: 'c++:类的各类型成员初始化'
categories:
  - Gist
mathjax: false
tags:
  - c/c++
date: 2018-02-01 16:44:10
---

> File : init.h
> Type : c/c++
> Brief : c++类的各种类型成员的初始化方法

<!-- more -->

---

```cpp
#include <iostream>

class Init
{
public:
    Init(int &m2, int m3) : m_2(m2), m_3(m3) {
        m_1 = 1;
    }
    void print(){
        std::cout << m_1 << " "
                  << m_2 << " "
                  << m_3 << " "
                  << m_4 << " "
                  << m_5 << " "
                  << m_6 << " "
                  << m_7[0][0] << " "
                  << m_8[0][0] << " ";
    }

private:
    // a : 通初始化列表初始化
    // b : 在构造函数中初始化
    // c : 在类内初始化
    // d : 在类外初始化
    int m_1;                // 只能a或b
    int& m_2;               // 只能a
    const int m_3;          // 只能a
    static int m_4;         // 只能d
    static const int m_5;   // 只能d, gcc也可以c
    static const int m_6=6;
    static const int m_7[2][2];
    static constexpr int m_8[2][2] = {{8,8},{8,8}}; // gcc中，用constexpr代替const可以c
};

int Init::m_4 = 4;
const int Init::m_5 = 5;
const int Init::m_7[2][2] = {{7,7},{7,7}};
```
