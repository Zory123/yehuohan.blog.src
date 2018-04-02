---
title: DSP FlashToRAM运行
categories:
  - 杂记
mathjax: false
tags:
  - dsp
date: 2017-09-08 19:15:09
---

简单介绍DSP的CMD文件，以及FlashToRAM配置。

<!-- more -->



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
其次，Memory Maps中的地址空间单位是类似 4K x 16 的方式，表示 4K x 16bit，
这样就是说，origin和length的单位为 16bit，即单位是 2字节，或者说 1个字
*/
```

一个简单的实例，如下(数值用16进制表示，与Memory Maps中相对应，方便查看)：

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

/* 用户也可以自定义SECTIONS，将特定变量放入其中 */
/* 将UserVar段放入PAGE 1中的USER_VAR块，而UserVar段中放变量my_var */
UserVar : > USER_VAR,  PAGE = 1

/* c/c++源代码中，需要按如下声明变量 */
#ifdef __cplusplus
#pragma DATA_SECTION("UserVar")
#else
#pragma DATA_SECTION(my_var,"UserVar");
#endif
int my_var[100];

/* asm源码如下 */
            .global _my_var
_my_var:    .usect "UserVar",200
```

一个CMD部分如下：

```cpp
SECTIONS
{
    /* Allocate program areas: */
    .text            : > PRAMH0,      PAGE = 0
    .cinit           : > PRAMH0,      PAGE = 0

    /* Allocate data areas: */
    .const           : > DRAMH0,      PAGE = 1
    .econst          : > DRAMH0,      PAGE = 1

    /* Allocate user var:   */
    UserVar          : > USER_VAR,    PAGE = 1
```


---
# FlashToRAM

## DSP运行过程
参考资料：
[SPRA958 - Running an Application from Internal Flash Memory on the TMS320F28xx DSP](http://www.ti.com/lit/an/spra958l/spra958l.pdf)
[SPRA958.zip](http://www-s.ti.com/sc/techlit/spra958.zip)
[SPRAAU8A - Copying Compiler Sections From Flash to RAM on the TMS320F28xxx DSCs](http://www.ti.com.cn/cn/lit/an/spraau8a/spraau8a.pdf)
[SPRAAU8.zip](http://www-s.ti.com/sc/techlit/spraau8.zip)

以TMS320F28xxx系列，说明从Flash到RAM运行的过程。

 - 使用CCS在线调试的代码流程：

```
code_start -> wd_disable -> c_int00 -> main() -> ...
```

 - 从Flash复制部分代码到RAM运行：

```
code_start -> wd_disable -> c_int00 -> main() -> memcpy() -> ...
其中，memcpy()用于将Flash中的代码复制到RAM中。
```

 - 从Flash复制所有代码到RAM中运行：

```
code_start -> wd_disable -> copy_sections -> c_int00 -> main() -> ...
因为main()本身都要复制到RAM中，所以只能在进入c环境之前，
使用汇编代码copy_sections进行复制。
```

## 从Flash到RAM的CMD编写

 - code_start, wd_disable, copy_sections需要在Flash中运行：

```
    codestart       : > BEGIN_FLASH,    PAGE = 0
    wddisable       : > FLASHA,         PAGE = 0
    copysections    : > FLASHA,         PAGE = 0
```

 - 已初始化段需要放于Flash中，通过copy_sections复制到RAM中：

| Initialized Sections                            | Uninitialized Sections   |
| :---                                            | :---                     |
| .binit, .cinit, .econst, .pinit, .switch, .text | .ebss, .stack, .esysmeme |

（.bss, .const, .sysmem是旧的段分配模型，已经不再使用。）

各段的解释如下：
![Initialized Sections](1.png)
![Uninitialized Sections](2.png)

copysections的代码，以.text为例：

```
    .text           :   LOAD = FLASHA,      PAGE = 0   /* can be ROM */
                        RUN = RAM_L0L1L2L3, PAGE = 0   /* must be CSM secured RAM */
                        LOAD_START(_text_loadstart),   /* 定义.text段的加载起始地址为_text_loadstart */
                        RUN_START(_text_runstart),     /* 定义.text段的运行起始地址为_text_runstart */
                        SIZE(_text_size)               /* 定义.text段的代码长度为_text_size */
    /*
    按上述CMD代码定义，.text段的代码会烧到FLASHA中，开电运行时，会选将FLASHA中
    的.text代码复制到RAM_L0L1L2L3中再运行
    */
```

LOAD_START, RUN_START, SIZE的具体意义，可以[参考汇编手册](http://www.ti.com/lit/ug/spru513n/spru513n.pdf)
在CMD中定义的变量(`_text_loadstart`等)用于copy_sections中，实现从Flash到RAM的复制，部分copy_sections代码如下：

```asm
    .global _text_loadstart, _text_runstart, _text_size
    .sect "copysections"
copy_sections:
    MOVL XAR5,#_text_size               ; Store Section Size in XAR5
    MOVL ACC,@XAR5                      ; Move Section Size to ACC
    MOVL XAR6,#_text_loadstart          ; Store Load Starting Address in XAR6
    MOVL XAR7,#_text_runstart           ; Store Run Address in XAR7
    LCR  copy                           ; Branch to Copy
    LB _c_int00                         ; Branch to start of boot.asm in RTS library

copy:
    B return,EQ                         ; Return if ACC is Zero (No section to copy)
    SUBB ACC,#1
    RPT AL                              ; Copy Section From Load Address to
    || PWRITE  *XAR7, *XAR6++           ; Run Address
return:
    LRETR                               ; Return
    .end
```

如果要在C/C++环境使用CMD中定义的变量，需要如下声明：

```
/* CMD中声明 */
LOAD_START(_RamfuncsLoadStart)

/* C/C++中声明，需要去掉第一个下划线 */
/* 附：C/C++中变量编译成汇编代码时，会在变量前加下划线，可查看map文件了解 */
extern Uint16 RamfuncsLoadStart
```
