---
layout: hexo_note
title: 工具参考书之FreeImage使用
date: 2018-03-22 17:21:41
tags:
  - FreeImage 
---

[FreeImage]()是一个基于C语言的轻量级图形库。使用时应查阅其官方[技术文档]()（且有中文版的，很是方便），这里只作简单的使用介绍。

## 初始化

 - FreeImage_Initialise: 初始化FreeImage库
 - FreeImage_DeInitialise: 撤消FreeImage的初始化（使用FreeImage动态库，会自动调用；但使用FreeImage静态库时，需要用户自行调用一次）

## 打开与保存

 - FreeImage_Allocate: 创建一个位图文件
 - FreeImage_Load: 加载位图文件
 - FreeImage_Save: 保存到位图文件

## 像素访问

 - FreeImage_GetBits: 获取一个指向位图数据位的指针
 - FreeImage_GetScanLine: 获取指向位图中指定行行首的指针
 - FreeImage_GetPixelIndex: 获取位图在指定位置的像素素引

## 示例
