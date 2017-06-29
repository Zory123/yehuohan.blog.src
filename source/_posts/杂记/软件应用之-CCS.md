---
title: 软件应用之 CCS
categories:
  - 杂记
date: 2017-06-16 16:36:56
tags: ccs
---

CCS v6.0的使用记录

<!-- more -->

---
# 文件说明
 - .gel : 仿真需要的文件，ccsv4后不再需要此文件
 - .cmd : ccs存放链接器的配置信息的，一个工程可以有多个cmd文件
 - rts2800.lib : C/C++运行支持库
 - rts2800_ml.lib : C/C++大内存模式运行支持库，其中有大量浮点运算处理的函数
 - rts2800_fpu32.lib : 浮点FPU支持库


---
# 设置 
 - 工程路径最好不要有中文，且路径长度<256
 - 补全提示：Window--Preferences--Editor--Content Assist，Delay改小，补全提示就会加快
 - 代码折叠：Window--Preferences--Editor--Folding，自己按需要勾上相应选项

---
# 使用
 - 代码时间测量：Run-clock
 - 重新开始运行：Run-Restart
 - 使用asm : 在汇编代码前需要加空格，如，asm(" NOP");
 
 
---
# CMD基本介绍
 - MEMORY(资源空间声明)
资源声明代码均入于MEMORY{}中，用于将空间资源进行划分。
使用PAGE n进行空间分块，并可以在PAGE中进行子分块。
空间子块使用如下语法：

```cpp
NAME : origin = <起始地址>, length = <长度>
/*
origin   : 起始地址
length   : 地址长度
结束地址 : = origin + length - 1

origin和length都要根据Data Manual中的Memory Maps部分进行配置。
其次，Memory Maps中的地址空间单位是类似 4K x 16 的方式，表示 4K x 16bit，这样就是说，origin和length的单位为 16bit，即单位是 2字节，或者说 1个字
*/
```

一个简单的实例，如下：

```cpp
MEMORY
{
/* 程序(指令)空间 */
PAGE 0 :
    /* 空间子块 */
    RAM : origin = 0x0033, length = 0x0200

/* 数据空间 */
PAGE 1 :
    /* 空间子块 */
    ROM1     : origin = 0x03f55, length = 0x0050
    ROM2     : origin = 0x04f55, length = 0x4050
    USER_VAR : origin = 0x7000, length = 0x1000
}
```

 - SECTIONS(资源空间分配)
资源声明代码均入于SECTIONS{}中，用于将相应的资源放入对应的空间中。
分配空间资源使用如下语法：

```cpp
/* 编译器定义好的SECTIONS，包括 .text, .cinit, .stack等 */
/* 如，将 .text段放入PAGE 0的RAM块 */
.text : > RAM,  PAGE = 0

/* 用户也可以自定义SECTIONS，将特定义变量放入其中 */
/* 将UserVar段放入PAGE 1中的USER_VAR块，而UserVar段中放于变量user_var */
UserVar : > USER_VAR,  PAGE = 1

/* c/c++源代码中，需要按如下声明变量 */
#ifdef __cplusplus
#pragma DATA_SECTION("UserVar")
#else
#pragma DATA_SECTION(user_var,"UserVar");
#endif
int user_var[10000];
```

一个实例如下：

```cpp
SECTIONS
{
    /* Allocate program areas: */
    .reset           : > PRAMH0,      PAGE = 0
    .text            : > PRAMH0,      PAGE = 0
    .cinit           : > PRAMH0,      PAGE = 0

    /* Allocate data areas: */
    .stack           : > RAMM1,       PAGE = 1
    .bss             : > DRAMH0,      PAGE = 1
    .ebss            : > DRAMH0,      PAGE = 1
    .const           : > DRAMH0,      PAGE = 1
    .econst          : > DRAMH0,      PAGE = 1      
    .sysmem          : > DRAMH0,      PAGE = 1
   
    /* Allocate user var:   */
    UserVar          : > USER_VAR,    PAGE = 1
```






 
