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
电机控制第五讲： {% post_link 笔记/电机控制之滑模控制 %}


<!-- more -->


---
# 回顾PMSM模型

在{% post_link 笔记/电机控制之永磁同步电机矢量控制 %}中，已经初步介绍了矢量控制的基本过程：

> 转速$n \to \;$ 电流$i_q \to \;$ 电压$u_d^\*,u_q^\* \to \;$ 电压$\boldsymbol{u_s}(u_A^\* \; u_B^\* \; u_C^\*) \to \;$ 逆变模块 $\to \;$ 电机
> 转速$n \to \;$ 电流$i_q \to \;$ 电流$i_d^\*,i_q^\* \to \;$ 电流$\boldsymbol{i_s}(i_A^\* \; i_B^\* \; i_C^\*) \to \;$ 逆变模块 $\to \;$ 电机

SVPWM是通过控制输出电压 $\boldsymbol{u_s}(u_A^\* \; u_B^\* \; u_C^\*)$，来控制电机。通过反馈调节（如PID），再结合Clarke和Park变换，即可得到$\boldsymbol{u_s}(u_A^\* \; u_B^\* \; u_C^\*)$。
此篇文章将具体介绍，如何输出电压矢量$\boldsymbol{u_s}$到电机。


---
# 电压矢量输出说明
如[图2-1](#图2-1)所示，现在我们要输出电压矢量$\boldsymbol{u_s}$。

将SVPWM加入到控制流程后，其大致过程如[图2-2](#图2-2)所示。


---
# SVPWM矢量表
SVPWM是电压矢量空间控制，其三相逆变电路原理图如[图3-1](#图3-1)所示。

<span id = "图3-1"></span>
> ![图3-1 三相逆变电路原理图](1-01.png) 

这里约定

---
# SVPWM合成






iq -> Te -> n -> 电压矢量（u-alpha, u-beta）
通过PID，将 $i_s$ 的控制 $\beta$ 的效果， 体现为 $u_\alpha, u_\beta$ 控制电压矢量（因为电压可以通过电压方程式和电流算出来），这即是反馈控制的量化体现。

---
电机控制第五讲： {% post_link 笔记/电机控制之控制策略 %}

SPWM和SVPWM的区别



