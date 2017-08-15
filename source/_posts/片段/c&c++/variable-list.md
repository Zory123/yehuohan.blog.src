---
title: c/c++:可变参数用法
categories:
  - 片段
mathjax: false
date: 2017-08-09 13:35:17
tags:
 - c/c++
---

> File : variable list.cpp
> Type : c/c++
> Brief : variable list

<!-- more -->

---

```c++
#include <iostream>
#include <stdlib.h>
#include <stdarg.h>
using namespace std;

/**
 **通过 va_list变量，va_start、va_arg、va_end宏 实现可变参数访问
 **可变参数的 函数，入栈顺序都是 从 右 往 左
 ** printf("%d,%d,%d",a++,++b,a+b)中先计算a+b
 **/
float average(int n_values,...)
{
    va_list argPtr; /*列表指针argPtr用于访问未确定的可变参数*/
    int count;
    float sum = 0;

    /*准备访问可变参数*/
    va_start(argPtr,n_values);
        /*用va_start初始化var_arg为可变参数的第一个参数;
         *使用va_start至少需要一个命名参数，这里有n_values;
         */

    /*添加取自可变参数列表的值*/
    for(count = 0; count < n_values; count++)
    {
        sum += va_arg(argPtr, int);
            /*用va_arg返回var_arg的值，并使var_arg指向下一个可变参数;
             *需要指定正确的可变参数类型，这里指定为int型;
             *需要判断可变参数的数量，这里用n_values说明;
             */
    }
    va_end(argPtr); /*最后一个可变参数要调用va_end*/

    return sum / n_values;
}


int main(void)
{
    cout << average(5,2,3,4,5,6);
    return 0;
}
```
