---
title: c/c++:sizeof pointer and array
categories:
  - 片段
mathjax: false
date: 2017-08-09 13:08:56
tags:
 - c/c++
---

> File : sizeof_ptrar.cpp
> Type : c/c++
> Brief : difference between size of pointer and arrray

<!-- more -->

---

```c++
#include <iostream>
using namespace std;

int main()
{
    int *ptr = new int[10];
    int ar[10] ={0};
    
    cout << sizeof(ptr) << endl;        // 指针变量占空间，32位机占4个字节，64位机占8个字节
    cout << sizeof(ar) <<  endl;        // 整个数组点的空间，10个int占40个字节
    
    return 0;
}
```
