---
title: c/c++:回调函数
categories:
  - 片段
mathjax: false
date: 2017-08-09 13:20:28
tags:
 - c/c++
---

> File : cbfunc.cpp
> Type : c/c++
> Brief : callback function

<!-- more -->

---

```c++
/*
 * Callback Function
 * 回调函数
 *
 */


#include <iostream>
using namespace std;

// 回调函数定义
typedef void(*cbFunc)(const char* s);

// understand like this:
//typedef   void(*)(char *s)    cbFunc;

void cbPrintStr1(cbFunc func, const char* s)
{
    cout << "this is cbPrintStr 1" << endl;
    func(s);
}

void cbPrintStr2(void (*func)(const char* s), const char *s)
{
    cout << "this is cbPrintStr 2" << endl;
    func(s);
}

void outStr(const char* s)
{
    cout << s << endl;
}

int main(int argc, char* argv[])
{
    cbPrintStr1(outStr, "1st operation by outStr");
    cout << endl;

    cbPrintStr2(outStr, "2nd operation by outStr");
    cout << endl;

    cbFunc cbFp;
    cbFp = outStr;
    cbPrintStr1(cbFp, "3th operation by cbFp");
    cout << endl;
    
    cbPrintStr2(cbFp, "4th operation by cbFp");

    return 0;
}
```
