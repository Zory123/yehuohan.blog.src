---
title: 电机控制之SVPWM
categories:
  - 笔记
mathjax: true
date: 2017-07-19 23:27:43
tags:
 - 电机控制
---

电机控制第一讲： {% post_link 笔记/电机控制之电磁基础 %}
电机控制第二讲： {% post_link 笔记/电机控制之空间矢量 %}
电机控制第三讲： {% post_link 笔记/电机控制之永磁同步电机矢量控制 %}
电机控制第四讲： {% post_link 笔记/电机控制之SVPWM %}


<!-- more -->


---
# 


通过PID，将 $i_s$ 的控制 $\beta$ 的效果， 体现为 $u_\alpha, u_\beta$ 控制电压矢量（因为电压可以通过电压方程式和电流算出来），这即是反馈控制的量化体现。
