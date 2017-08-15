---
title: c/c++:关于类成员变量的继承
categories:
  - 片段
mathjax: false
date: 2017-08-09 13:30:56
tags:
 - c/c++
---

> File : inherited variable.cpp
> Type : c/c++
> Brief : varible inherited from base class

<!-- more -->

---

```c++
/*
 * 使用g++编译问题：m_data变量没有声明(m_data应该是通过BaseTemp继承过来了，怎么会没有声明呢？)

 * 原因：
    查找C++Std文档，The lookup of names dependent on the template parameters is
    postponed until the actual template argument is known.
    
 * 意思是：
    依赖于模板参数的Name Lookup会推迟到模板参数的实际类型确定的时候（也就是模板实例化的时候），
    模板是编译时多态(区别于虚函数的运行时多态)。
    在程序中，由于m_data依赖于基类BaseTemp<T1>，而基类BaseTemp<T1>又依赖于子类 ChildTemp<T2>的模板参数T2。
    因此，在ChildTemp<T2>中定义SetData函数的时候，m_data的lookup会被推迟到BaseTemp<T1>实例化的时候。即这时候，
    就不知道m_data是从哪里来的了。

 * 解决方法：显式的指明m_data是从哪里来的
 *
 */


#include <iostream>

template< typename T1>
class BaseTemp 
{
protected:
    int m_data;
    T1  m_base;
};

template< typename T2>
class ChildTemp:public BaseTemp<T2>
{
public: 
    int GetData()
    {
        //return m_data;                        //出错，提示m_data未定义
        
        return this->m_data;                    //this指针 显式指明，所以，习惯性的加上this指针吧
        //return BaseTemp<T2>::m_data;          //类域符 显式指明
    }
};

int main(int argc, char** argv)
{
   // std::cout << obj.GetData() << std::endl;
    return 0;
}
```
