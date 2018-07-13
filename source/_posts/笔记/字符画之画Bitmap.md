---
title: 字符画之画Bitmap
categories:
  - 笔记
mathjax: false
date: 2018-07-14 00:55:05
tags:
  - 数据结构(dsa)
---

用字符“画”Bitmap数据结构。

## Bitmap

```
  (1) 原理：用一个bit来标记一个数是否存在。
  一个int-32bit，可以标记十进制0~31，即表示了32个整型数据。
  相当于存储32个数据只需要4个字节。
  若用char来存储32个数据(0~31)，则至少需要32个字节。

  (2) 存储序列图：
  char  char[0]         char[n]
  bit  [7      0]......[7      0]
       低字节          高字节

  k=0 : char[0]-bit[7]
  k=7 : char[0]-bit[0]
  k=8 : char[1]-bit[7]
  k=9 : char[1]-bit[6]
  k=15: char[1]-bit[0]
  char[n]  : n = k/8 = k>>3
  bit[n-1] : n = 0x80 >> (k%8) = 0x80 >> (k&0x07)
```

## c++ stl实现

c++ stl实现的数据结构为std::bitset，简单用法见[bitset](https://github.com/yehuohan/dsas/blob/master/dsas-usestl/container_bitset.cpp)。

## 参考代码

[Bitmap](https://github.com/yehuohan/dsas/blob/master/dsas-cpp/bitmap.h)
