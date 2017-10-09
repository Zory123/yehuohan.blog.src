---
title: c/c++:生成时间string
categories:
  - Gist
mathjax: false
date: 2017-08-09 13:05:30
tags:
 - c/c++
---

> File : time2string.cpp
> Type : c/c++
> Brief : convert time to string

<!-- more -->

---

```c++
// 将时间格式化成自己想要的字符串
std::time_t tt = std::time(nullptr);
std::tm     *tl = std::localtime(&tt);
char        str_time[100];
std::strftime(str_time, 100, "%Y%m%d-%H.%M.%S", tl);
file_name = std::string(str_time);
```
