---
title: Windows使用mklink建立“符号链接”
categories:
  - 杂记
date: 2017-06-09 17:42:53
tags: cmd
---


# 说明
Linux下可以使用ln命令来实现文件和目录的链接，在windows下可以mklink来实现类似的功能。
这里说的链接不是快捷方式，快捷方式是一个*.lnk文件，mklink建立的是符号链接，简单来说，就是一个“磁盘物理位置”，多个“符号链接入口”。比如，某个软件在C盘某缓存文件夹的内容越来越多，软件又不能改变缓存置，又不能通过设置只读属性来禁用，这时就可通过mklink来改变文件夹的磁盘物理位置。

<!-- more -->

---
# 命令使用

```bash
创建符号链接：
MKLINK [[/D] | [/H] | [/J]] Link Target

        /D      创建目录符号链接。默认为文件
                符号链接。
        /H      创建硬链接，而不是符号链接。
        /J      创建目录联接。
        Link    指定新的符号链接名称。
        Target  指定新链接引用的路径
                (相对或绝对)。
```

 - 实例：
```bash
mklink /D C:\cache D:\temp_chche 
	// 软件缓存位置在D:\temp_cache,符号链接在C:\cache,这样，缓存内容都放在D:\temp_cache,通过C:\cache也能进入缓存文件夹，就不会影响软件运行
```