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

| PMSM     | 面装式                                                                                                                 | 插入式、内装式                                                                                                             |
| :---     | :---                                                                                                                   | :---                                                                                                                       |
| 基本方程 | ${\boldsymbol u_s} = R_s{\boldsymbol i_s} + \cfrac{d\boldsymbol {\psi_s}}{dt}$                                         | ${\boldsymbol u_s} = R_s{\boldsymbol i_s} + \cfrac{d\boldsymbol {\psi_s}}{dt}$                                             |
| 同步电感 | $L_s = L_d = L_q$                                                                                                      | $L_{md} < L_{mq}$                                                                                                          |
| 数学模型 | ${\boldsymbol u_s} = R_s {\boldsymbol i_s} + L_s \cfrac{d \boldsymbol{i_s}}{dt} +  \cfrac{d \boldsymbol {\psi_f}}{dt}$ | $u_d = R_s i_d + {\cfrac {d\psi_d} {dt}} - \omega_r \psi_q$ <br> $u_q = R_s i_q + \cfrac{d\psi_q} {dt} + \omega_r \psi_d $ |
| 转矩方程 | $t_e = p_0 \psi_f i_s sin\beta = p_0 \psi_f i_q$                                                                       | $t_e = p_0[\psi_f i_q + (L_d - L_q)i_d i_q]$                                                                               |


---
# SVPWM控制系统介绍
SVPWM是电压矢量空间控制，其三相逆变电路原理图如[图1-1](#图1-1)所示。

<span id = "图1-1"></span>
> ![图1-1 三相逆变电路原理图](1-01.png) 


---
# 



通过PID，将 $i_s$ 的控制 $\beta$ 的效果， 体现为 $u_\alpha, u_\beta$ 控制电压矢量（因为电压可以通过电压方程式和电流算出来），这即是反馈控制的量化体现。
