---
title: 软件应用之 CMake
categories:
 - 杂记
mathjax: false
date: 2017-06-17 00:21:49
tags:
 - cmake
---

CMake使用记录。

<!-- more -->

# 设置
 - cmake设置inc和lib路径
 cmake 在 find_path 和 find_library 时，会搜索一些默认的路径。当我们将一些lib安装在非默认搜索路径时，cmake就没法搜索到了。这是我们需要添加路径。方法如下：

```
set(CMAKE_INCLUDE_PATH "include_path")
set(CMAKE_LIBRARY_PATH "lib_path")
```

 - cmake-gui像命令行使用一样设置参数
勾选Advanced和Grouped，可以给所有的参数赋值。每点一次configure，出错时，就说明有需要的赋值的参数没有赋值。


