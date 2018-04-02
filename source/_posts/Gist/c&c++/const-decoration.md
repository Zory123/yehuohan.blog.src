---
title: 'c/c++:const修饰函数'
categories:
  - Gist
mathjax: false
tags:
  - c/c++
date: 2017-08-09 13:22:04
---

> File : const_decoration.cpp
> Type : c/c++
> Brief : const decoration

<!-- more -->

---

```c++
#include <iostream>
using namespace std;
class constTest
{
public:
    constTest(int x):data(x){}
    ~constTest(){}
    
    int set1(const int& n)
    {
        //n++;                  //error
        data = n;
        data ++;                //ok
    }
    
    int get1() const 
    {
        return data;
        //return data++;        //error
    }
    
    int get2()
    {
        return data++;          //ok
    }

    int& get3()                 //用于修改data
    {
        return data;
    }

    const int& get4() const     //用于const constTest访问data，但不能修改data
    {
        return data;
    }
    
private:
    int data;
};


int main()
{
    cout << "test const" << endl;
    
    // const 与函数
    constTest aa(10);
    int bb;
    bb = aa.get2();
    
    cout << aa.get1() << endl;
    aa.get2();
    cout << aa.get2() << endl;

    int m = 0,n = 0;
    // const 与指针
    const int *a;       // const 修饰*a，*a不能改
    int const *a;       // 与上面写法等价
    //*a = 100;         // error
    a = &m;             // ok
    
    int* const b = &m;  // const 修饰 b，b不能改
    *b = 100;           // ok
    //b = &n;           // error
    
    // const 与常量
    const int c = 0;
    int const d = 0;    //两种写法等价，const 与 int 在前在后是一样的，换成 *c *d 也是一样的
    
    return 0;
}
```
