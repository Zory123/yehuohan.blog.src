
---
title: 记录GCC,GDB的使用
date: 2017-06-07 01:05:36
tags:
 - gcc
 - c/c++
 - linux
categories:
 - 笔记
---


---
## **GCC介绍**
 - GCC 原名为 GNU C 语言编译器（GNU C Compiler），因为它原本只能处理 C语言。GCC 很快地扩展，变得可处理 C++。后来又扩展能够支持更多编程语言，如Fortran、Pascal、Objective-C、Java、Ada、Go以及各类处理器架构上的汇编语言等，所以改名GNU编译器套件（GNU Compiler Collection）。

 - GCC 对于操作系统平台及硬件平台支持，概括起来就是一句话：无所不在。Arm，X86_64等都有GCC的身影。

---
## **基本说明**
```
   gcc 编译c文件
   g++ 编译cpp文件

  .c      C源程序;预处理,编译,汇编
  .cpp    C++源程序;预处理,编译,汇编
  .cc     C++源程序;预处理,编译,汇编
  .cxx    C++源程序;预处理,编译,汇编
  .m      Objective-C源程序;预处理,编译,汇编
  .i      预处理后的C文件;编译,汇编
  .ii     预处理后的C++文件;编译,汇编
  .s      汇编语言源程序;汇编
  .S      汇编语言源程序;预处理,汇编
  .h      预处理器文件;通常不出现在命令行上
```

---
## **基本使用**

### 生成可执行文件

| `-o`                         | 说明                            |
| :-                           | :-                              |
| gcc main.c -o main           | c文件用gcc生成exe               |
| g++ main.cpp -o main         | cpp文件用gcc生成exe             |
| g++ main.cpp -o main         | cpp文件用gcc生成exe             |
| g++ main.cpp src.cpp -o main | 直接编译链接*.cpp，生成main.exe |

### 生成obj文件

| `-c`            | 说明                            |
| :-              | :-                              |
| g++ -c main.cpp | 编绎cpp文件，输出目标main.o文件 |

### 生成静态库(.a)

| `ar -crv`                | 说明                                 |
| :-                       | :-                                   |
| ar -crv libmain.a main.o | 由.o生成静态库.a文件（也称归档文件） |

### 生成动态库(.so)

| `-shared -fPIC`                        | 说明                      |
| :-                                     | :-                        |
| g++ -shared -fPIC -o libmain.so main.o | 由.o文件生成动态库.so文件 |

### 添加头文件目录

| 参数           | 示例                             | 说明                                           |
| :-             | :-                               | :-                                             |
| **`-I`**       | g++ main.cpp -I "./src"          | 头文件在 "./src" 中，多个文件夹用多个 "-I"     |
| **`-isystem`** | g++ main.cpp -isystem "/usr/inc" | 添加/usr/inc；搜索顺序 "-I >= -isystem >= std" |

### 添加库文件


| 参数     | 示例                            | 说明                            |
| :-       | :-                              | :-                              |
| **`-L`** | g++ main.cpp -o main -L "./lib" | 指定库文件路径"./lib"           |
| **`-l`** | g++ main.cpp -o main -llibmain  | 指定库文件libmain.so或libmain.a |

---
## **配置选项**

### 设置源文件编码和可执行文件编码

| 参数                   | 示例                                    | 说明                                                |
| :-                     | :-                                      | :-                                                  |
| **`-finput-charset"`** | g++ main.cpp -finput-charset=utf-8      | main.cpp文件编码为utf-8                             |
| **`-fexec-charset"`**  | g++ main.cpp -o main -fexec-charset=gbk | main.exe字符编码为gbk|

### 设置c++标准

| `-std`                  | 说明              |
| :-                      | :-                |
| g++ main.cpp -std=c++11 | 采用c++11标准编译 |

### 设置x86或x64

| 参数       | 示例              | 说明          |
| :-         | :-                | :-            |
| **`-m32`** | g++ main.cpp -m32 | 设置为x86程序 |
| **`-m64`** | g++ main.cpp -m64 | 设置为x64程序 |


---
## GDB使用
首先将GDB看成一个可以独立的软件，不再是像各种IDE一样，将编译、运行、调试都集成到一个软件中。
在这里介绍GDB命令的基本使用。gdb是一个命令交互试界面，所以需要使用一些命令来对exe进行调试。

附：以下命令没有特殊说明，均在gdb环境中键入运行。
附：如果想使用一个相对方便点的终端界面，可以使用[gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard)，效果图如下：
{% asset_img gdb.png %}

### 打开

| 示例               | 说明                                                              |
| :-                 | :-                                                                |
| `gdb`              | 此命令在终端下运行，打开gdb                                       |
| `gdb <exec-file>`  | 此命令在终端下运行，打开gdb，并加载可执行文件                     |
| `gdb -tui`         | 此命令在终端下运行，使用gdb终端界面，可以显示源码                 |
| `help <cmd>`       | 显示gdb中cmd命令的帮助                                            |
| `file <exec-file>` | 加载可执行程序文件，以便调试，可执行程序用gcc编译时，需要加-g参数 |
| `quit`             | 退出gdb，可简写成q                                                |

### 源代码显示

| 示例                             | 说明                                                                      |
| :-                               | :-                                                                        |
| `list`                           | 显示当前行到之后10行源代码，可简写成l                                     |
| `l n1,n2`                        | 显示n1行到n2行的源代码                                                    |
| `l +/-ofs`                       | 显示当前行到正/负偏移量的源代码，仿移量为ofs                              |
| `l <filename:line-num/function>` | 显示某个文件的指定行号/指定函数<br />filename包括后缀名，省略则为当前文件 |


### 断点

| 示例                                             | 说明                                                                      |
| :-                                               | :-                                                                        |
| `break <filename:line-num/function> <condition>` | 在行号/函数处下断点<br />break可简写成b<br />filename可省略，代表当前文件 |
| `b 10 if tmp>10`                                 | 当变量tmp>10时，在此断点                                                  |
| `delete`, `d`                                    | 删除所有断点                                                              |
| `d N`                                            | 删除N号断点，(使用info b查看断点信息)                                     |

### 显示所调试程序的信息

| 示例                                                       | 说明                                                       |
| :-                                                         | :-                                                         |
| `display <var>`<br />`disp <var>`                               | 每次中断时，显示变量var的值                                |
| `disp <expr>`                                              | 每次中断时，显示表达式的值<br />如： disp (float)test/2.0  |
| `undisp N`                                                 | 取消显示，N为需要取消变量或表达式的编号(使用info disp查看) |
| `print <var>` <br /> `p /arg <var>` <br /> `p /arg <expr>` | 显示变量或表达式的值，不会每次中断显示                     |
| `p <var=?>`                                                | 改变变量的值并显示                                         |

```text
arg参数为显示格式，可省略：
  /x : 按十六进制格式显示变量。
  /d : 按十进制格式显示变量。
  /u : 按十六进制格式显示无符号整型。
  /o : 按八进制格式显示变量。
  /t : 按二进制格式显示变量。
  /a : 按十六进制格式显示变量。
  /c : 按字符格式显示变量。
  /f : 按浮点数格式显示变量。
```

### 显示gdb程序的信息

| 示例                 | 说明                               |
| :-                   | :-                                 |
| `info b`, `i b`      | 显示所有断点信息                   |
| `i disp`             | 显示所有disp信息                   |
| `i source`, `i s`    | 显示当前所在语言件和行号           |
| `i variables`,`i va` | 显示所有的全局变量和变静态变量名称 |

### 运行

| 示例                           | 说明                                                                          |
| :-                             | :-                                                                            |
| `run <args>` <br /> `r <args>` | 运行程序，直至遇到断点<br /> run后面可接参数，即传给main函数的参数            |
| `continue`<br /> `c`           | 断续执行，直至下一个断点                                                      |
| `step <N>`<br /> `s <N>`       | 执行一行源代码，若有函数，则进入函数<br />N表示执行N次step                    |
| `next <N>`<br /> `n <N>`       | 执行一行源代码，若有函数，则函数一并执行，不会进入函数<br /> N表示执行N次next |
| `nexti/stepi`<br /> `ni/si`    | 针对汇编指令的step和next                                                      |
| `finish`<br /> `f`             | 执行完当前函数，返回到调用它的函数(包括main函数)                              |
| `[enter]`                      | 直接回车，则执行上一次的命令(这样单步调试时，就不用一直输s/n了)               |
