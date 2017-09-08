---
title: 软件应用之 CCS
categories:
  - 杂记
date: 2017-06-16 16:36:56
tags: ccs
---

CCS v6.0的使用记录

<!-- more -->

---
# 文件说明
 - .gel : 仿真需要的文件，ccsv4后不再需要此文件
 - .cmd : ccs存放链接器的配置信息的，一个工程可以有多个cmd文件
 - .map : CCS软件编译后产生的有关DSP用到所有程序、数据及IO空间的一种映射文件。
 - rts2800.lib : C/C++运行支持库
 - rts2800_ml.lib : C/C++大内存模式运行支持库，其中有大量浮点运算处理的函数
 - rts2800_fpu32.lib : 浮点FPU支持库
 - rts2800_fpu32_fast_supplement.lib : 浮点FPU加速库，计算速度更快


---
# 设置 
 - 工程路径最好不要有中文，且路径长度<256
 - 补全提示：Window--Preferences--Editor--Content Assist，Delay改小，补全提示就会加快
 - 代码折叠：Window--Preferences--Editor--Folding，自己按需要勾上相应选项

---
# 使用
 - 代码时间测量：Run-clock
 - 重新开始运行：Run-Restart
 - 使用asm : 在汇编代码前需要加空格，如，asm(" NOP");
 - char类型 : char类型也是占16bit（可以在.map中查看），故使用int16即可
 
