---
title: 'C/C++:指针释放问题'
categories:
  - 片段
mathjax: false
date: 2017-09-29 21:32:02
tags:
 - c/c++
---

> File : pointer-release.h
> Type : c/c++
> Brief : pointer release

<!-- more -->

---

```cpp

class Test
{
public: 
    Test():m_pint(nullptr){}
    ~Test(){if(m_pint) delete m_pint;}

    void start()
    {
        m_pint = new int[10];
    }

    void stop()
    {
        if(m_pint)
            delete m_pint;
        m_pint = nullptr;       // 一定要再次赋值为nullptr，
                                // delelte只是释放内存，但指针m_pint的值不会改变
                                // 不赋值为nullptr，析构时可能出问题
    }

private:
    int* m_pint;
};


```
