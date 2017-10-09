---
title: c/c++:常量作为地址
categories:
  - Gist
mathjax: false
date: 2017-08-09 13:38:49
tags:
 - c/c++
---

> File : const value address.cpp
> Type : c/c++
> Brief : take const value as pointer address

<!-- more -->

---

```c
#include <stdio.h>

int main()
{
    const int *addr = (int*)0xaaaaffff;
    
    printf(" %x : ",addr);
    
    printf(" %x : ", *addr);        // 有可能会出错，若地址0xaaaaffff不在此程序的内存读取范围内，则会出错
    
}
```
