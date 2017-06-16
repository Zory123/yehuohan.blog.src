---
title: 软件应用之 CCS
categories:
  - 杂记
date: 2017-06-16 16:36:56
tags: ccs
---

CCS v6.0的使用记录

<!-- more -->

# 文件说明
 - .gel : 仿真需要的文件，ccsv4后不再需要此文件
 - .cmd : ccs存放链接器的配置信息的，一个工程可以有多个cmd文件
 - rts2800.lib : C/C++运行支持库
 - rts2800_ml.lib : C/C++大内存模式运行支持库，其中有大量浮点运算处理的函数
 - rts2800_fpu32.lib : 浮点FPU支持库
 

# 使用
 - 代码时间测量：Run-clock
 - 重新开始运行：Run-Restart