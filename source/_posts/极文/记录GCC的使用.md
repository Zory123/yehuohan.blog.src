
---
title: 记录GCC的使用
date: 2017-06-07 01:05:36
tags:
 - gcc
 - c/c++
 - linux
categories:
  - 极文
  - Linux
---




---
# **GCC介绍**
 - GCC 原名为 GNU C 语言编译器（GNU C Compiler），因为它原本只能处理 C语言。GCC 很快地扩展，变得可处理 C++。后来又扩展能够支持更多编程语言，如Fortran、Pascal、Objective-C、Java、Ada、Go以及各类处理器架构上的汇编语言等，所以改名GNU编译器套件（GNU Compiler Collection）。
  
 - GCC 对于操作系统平台及硬件平台支持，概括起来就是一句话：无所不在。Arm，X86_64等都有GCC的身影。

<!-- more -->


---

# **基本说明**	
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

---
# **基本使用**
* 生成可执行文件
```bash
"gcc, g++"
gcc main.c -o main
g++ main.c -o main
# c 文件用gcc命令, cpp文件用g++命令

"-o"
g++ main.cpp src.cpp -o main
# 直接编译链接*.cpp，生成main.exe
```

* 生成obj文件
```bash
"-c"
g++ -c main.cpp
# 编绎cpp文件，输出目标main.o文件
```

* 生成静态库(.a)
```bash
"ar -crv"
ar -crv libmain.a main.o
# 由.o生成静态库.a文件（也称归档文件）
```

* 生成动态库(.so)
```bash
"-shared -fPIC"
g++ -shared -fPIC -o libmain.so main.o
# 由.o文件生成动态库.so文件
```

* 添加头文件目录
```bash
"-I"
g++ main.cpp -o main -I "./src"
# 头文件在 "./src" 中，多个文件夹用多个 "-I"
```

* 添加库文件
```bash
"-L"
g++ main.cpp -o main -L "./lib"
# 指定库文件路径"./lib"

"-l"
g++ main.cpp -o main -llibmain
# 指定库文件libmain.so或libmain.a
```


---
# **配置选项**
* 设置源文件编码和可执行文件编码
```bash
"-finput-charset"
g++ main.cpp -finput-charset=utf-8
# main.cpp文件编码为utf-8

"-fexec-charset"
g++ main.cpp -o main -fexec-charset=gbk
# main.exe字符编码为gbk，windows下用gbk输出才不会乱码
```

* 设置c++标准
```bash
"-std"
g++ main.cpp -std=c++11
# 采用c++11标准编译，支持新特性，如nullptr等
```

*  设置x86或x64
```bash
"-m32" "-m64"
g++ main.cpp -m32
# 编译成32位程序或64位程序
```
