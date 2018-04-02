---
title: 'c/c++:指针与数组'
categories:
  - Gist
mathjax: false
tags:
  - c/c++
date: 2017-08-09 13:17:57
---

> File : pointer and array.cpp
> Type : c/c++
> Brief : pointer and array

<!-- more -->

---

```c++
/*
int* a[4]   指针数组     
            表示：数组a中的元素都为int型指针    
            元素表示：*a[i]   *(a[i])是一样的，因为[]优先级高于*

int (*a)[4] 数组指针     
            表示：指向数组a的指针
            元素表示：(*a)[i]  
*/

#include <iostream>

int main()
{
    int* a[10];
    a[1] = new int[100];    // 元素 是 指针
    
    int(*b)[5];
    int c[] = { 1, 2, 3, 4, 5 };
    b = &c;                 // *b 是 数组首地址，则b 是二级地址，即二级指针
    (*b)[2] = 20;
    cout << (*b)[2] << endl;
    cout << *((*b) + 1) << endl;
    
    return 0;
}
```
