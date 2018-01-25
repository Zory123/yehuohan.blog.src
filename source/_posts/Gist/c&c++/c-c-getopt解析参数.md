---
title: 'c/c++:getopt解析参数'
categories:
  - Gist
mathjax: false
date: 2018-01-25 10:44:23
tags:
  - c/c++
---

> File : getopt_args.cpp
> Type : c/c++
> Brief : 使用getopt函数解板字符串参数

<!-- more -->

---

```cpp
#include <getopt.h>
int main(int argc, char* argv[])
{
    /*
    int getopt(int argc, char * const argv[], const char *optstring);
    extern char *optarg;
    extern int optind, opterr, optopt;

    optstring:  选项字母组成的字串。如果该字串里的任一字符后面有冒号，那么这个选项就要求有选项参数。
    optarg:     当前选项参数字串（如果有）。
    optind:     argv的当前索引值。
                当getopt()在while循环中使用时，循环结束后，剩下的字串视为操作数，在argv[optind]至argv[argc-1]中可以找到。
    opterr:     这个变量非零时，getopt()函数为“无效选项”和“缺少参数选项，并输出其错误信息。
    optopt:     当发现无效选项字符之时，getopt()函数或返回'?'字符，或返回':'字符，并且optopt包含了所发现的无效选项字符。
    */

    int arg;
    opterr = 1;
    while ((arg = getopt(argc, argv, "se:v:")) != -1)
    {
        cout << "optind :" << optind << endl;
        switch (arg)
        {
        case 's':
            cout << "s: " << "Show this" << endl;
            break;
        case 'e':
            cout << "e: " << optarg << endl;
            break;
        case 'v':
            cout << "v: " << optarg << endl;
        }
    }

    while (1)
    {
    };

    return 0;
}

```
