---
title: 'c++:auto在遍历中的使用'
categories:
  - Gist
mathjax: false
date: 2018-01-24 15:22:12
tags:
---

> File : auto.cpp
> Type : c++
> Brief : c++ auto在遍历中的简单使用

<!-- more -->

---


```cpp
int main(void)
{
    std::string str = "Hello auto";
    std::vector<std::string> vstr;
    vstr.push_back("Hello cpp");
    vstr.push_back("Hello auto");
    vstr.push_back("Hello world");

    // 遍历string
    for (int k = 0; k < str.size(); k ++)
        std::cout << str[k];
    std::cout << std::endl;

    // 使用auto遍历string
    for (auto ch:str)       // 按值
    {
        std::cout << ch;
        ch ++;
    }
    std::cout << "  " << str << std::endl;
    for (auto &ch:str)      // 按引用
    {
        std::cout << ch;
        ch ++;
    }
    std::cout << "  " << str << std::endl;


    // 遍历vector
    for (int k = 0; k < vstr.size(); k ++)
        std::cout << vstr[k] << "  ";
    std::cout << std::endl;
    for (std::vector<std::string>::iterator it = vstr.begin();
            it != vstr.end(); it ++)
        std::cout << *it << "  ";
    std::cout << std::endl;

    // 使用auto遍历vector
    for (auto &it:vstr)     // 按引用
    {
        std::cout << it << "  ";
        it = "Changed";
    }
    for (auto it:vstr)      // 按值
    {
        std::cout << it << "  ";
        it = "Not Changed";
    }

    return 0;
}


```
