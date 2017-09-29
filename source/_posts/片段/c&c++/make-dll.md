---
title: c/c++:dll动态库生成
categories:
  - 片段
mathjax: false
date: 2017-08-09 15:50:46
tags:
 - c/c++
---

> File : make_dll.h, make_dll.c
> Type : c/c++
> Brief : simple demo to make dll

<!-- more -->

---

 - make_dll.h

```c++
#ifndef _DLL_MAKE_H
#define _DLL_MAKE_H

//#define __MSVC
#define __GCC

// uncomment this to NOT create dll
//#define OS_API
#ifdef OS_API
    #define OS_CALL
#else

#ifdef __MSVC
    #define OS_API_IMPORT   __declspec(dllimport)
    #define OS_API_EXPORT   __declspec(dllexport)
    #define OS_CALL         __stdcall
#elif defined __GCC
    #define OS_API_IMPORT   __attribute__((dllimport))
    #define OS_API_EXPORT   __attribute__((dllexport))
    #define OS_CALL         __attribute__((__stdcall__))
#endif

#define __BUILD_DLL
#ifndef __BUILD_DLL
    #define OS_API  OS_API_IMPORT
#else
    #define OS_API  OS_API_EXPORT
#endif

#endif


// __cplusplus: cpp中自定义的一个宏
// extern     : 表明函数和全局变量可以在外部模块中使用
// "C"{}      : 表明{}中的代码按C语言格式进行编译
// extern "C" : 是为了实现C++与C及其它语言混合编程

// 使用cpp调用此库或此文件时，按照C语言格式编译
#ifdef __cplusplus
extern "C"{
#endif

OS_API int OS_CALL func_1(int a, int b);
OS_API float OS_CALL func_2(float x);

#ifdef __cplusplus
}
#endif

#endif
```


 - make_dll.c

```c++
#include "dll_make.h"

OS_API int OS_CALL func_1(int a, int b)
{
    return a+b;
}

OS_API float OS_CALL func_2(float x)
{
    return x*x;
}

```
