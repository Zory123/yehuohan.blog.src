---
title: 'c++:用using定义类型别名'
categories:
  - Gist
mathjax: false
date: 2018-02-01 16:14:03
tags:
  - c/c++
---

> File : using.cpp
> Type : c/c++
> Brief : c++11中使用using定义类型别名

<!-- more -->

---

```cpp
#include <iostream>
#include <vector>

// using 与 typedef 类似
typedef unsigned char u8;
using uint8 = unsigned char;

// 定义函数类型
typedef int(*cfunc)(int,int);
using nfunc = int(*)(int,int);

int max(int a, int b) {return a>b?a:b;}
void print_max(nfunc f, int a, int b)
{
    std::cout << f(a, b) << std::endl;
}

// 使用using定义模版类类型
template <typename T> using Vec = std::vector<T>;

int main()
{
    u8 a = 10; uint8 b = a;
    Vec<int> v; v.push_back(10);
    print_max(max, 10, 20);
    std::cout << (int)b << std::endl;
    std::cout << v[0] << std::endl;
    return 0;
}
```
