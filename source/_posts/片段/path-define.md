---
title: path define
categories:
  - 片段
mathjax: false
date: 2017-08-09 11:17:04
tags:
 - c/c++
---

> File : path_define.h
> Type : c&cpp
> Brief : path define

<!-- more -->

---

```c
// 用于配置路径的宏
// 重新定义LIB_DIR后(先undef再define)，即可使用LIB_NAME，或者直接使用LIB_PATH(path,lib)

#if defined _OS_WIN

#define LIB_DIR
#define _TO_STR(str)                #str
#define TO_STR(str)                 _TO_STR(str)
#define _LIB_PATH(path,file)        path##file
#define __LIB_PATH(path,file)       _LIB_PATH(path,file)
#define ___LIB_PATH(path,file)      __LIB_PATH(path,\\##file)
#define ____LIB_PATH(path,file)     ___LIB_PATH(path,file)
#define LIB_PATH(path,file)         TO_STR(____LIB_PATH(path,file))
#define LIB_NAME(file)              LIB_PATH(LIB_DIR,file)

#elif defined _OS_LINUX

#define LIB_DIR
#define _TO_STR(str)                #str
#define TO_STR(str)                 _TO_STR(str)
#define _LIB_PATH(path,file)        path##file
#define __LIB_PATH(path,file)       _LIB_PATH(path,file)
#define ___LIB_PATH(path,file)      __LIB_PATH(path,/##file)
#define ____LIB_PATH(path,file)     ___LIB_PATH(path,file)
#define LIB_PATH(path,file)         TO_STR(____LIB_PATH(path,file))
#define LIB_NAME(file)              LIB_PATH(LIB_DIR,file)

#endif

```
