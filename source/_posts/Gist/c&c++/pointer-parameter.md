---
title: c/c++:指针作为函数参数
categories:
  - Gist
mathjax: false
date: 2017-08-09 13:37:27
tags:
 - c/c++
---

> File : pointer parameter.cpp
> Type : c/c++
> Brief : pointer parameter

<!-- more -->

---

```c++
/* 
 * 指针没有完全理解
 * 将指针当成一个变量
 * 函数传指针，可以改变指针指向的地址的值，但不能改变指针指向的地址
 * 要改变指针指向的地址，就要传指针变量的地址，即二级指针
 */
 
/*
 *  var: **str = "hello"
    addr.   value.
    str     *str
    *str    **str == "hello"
 */

#include <iostream>
#include <string.h>

using namespace std;

typedef char* charptr;

// 指针类型的传值过程，p中存的地址不会保存到实参
void get1(char* p)
{
    p = new char[100];
}
void get2(charptr p)
{
    p = new char[100];
}

// get3和get4等价，指针类型的传址过程，*p保存的地址可以保存到实参
// get5为传递指针的引用，可以改变指针变量中存的地址
void get3(char **p)
{
    *p = new char[100]; 
}
void get4(charptr *p)
{
    *p = new char[100];
}
void get5(char*&p)
{
    p = new char[100];
}

// 函数中申请的内存空间不会释放，临时存放地址的变量t释放掉了，但cp指向了内存空间地址
char *cp;
void get6()
{
    char *t = new char[100];
    cp = t;
}

// 申请二组数组的内存空间
// n1 : 第一组的长度，即二维数组的行
void get7(int n1,char**& p)
{
    /*
    char* str[3];
    *(str + 0) = (char*) tmp;
    str也是指针数组，也是二级指针，因为str作为数组是一个地址，而str存储的也是char*指针
    */  
    p = new char*[n1];
    *(p + 1) = new char[20];
    /*
    p = (int **)malloc(sizeof(int*) * n1);
    *(p + 1) = (int *)malloc(sizeof(int) * 10);
    */
    strcpy(*(p+1),"hello 2d");
}


int main(int argc, char *argv[])
{
    charptr str = nullptr;
    //get4(&str);                   //传址
    get5(str);                      //指针的引用
    strcpy(str,"hello world");
    cout <<str << endl;
    
    char ** str2 = nullptr;
    get7(5,str2);
    cout << *(str2+1) << endl;
    
    return 0;
}

```
