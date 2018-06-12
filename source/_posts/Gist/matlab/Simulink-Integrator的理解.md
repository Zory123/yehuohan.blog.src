---
title: 'matlab:Simulink Integrator的理解'
categories:
  - Gist
mathjax: true
date: 2017-08-15 19:26:30
tags:
---

> File : [integrator.slx](integrator.slx) *(Simulink仿真文件，直接右键另存为下载)*
> Type : matlab/simulink
> Brief : Simulink仿真中Intergrator模块的理解，以及与拉氏变换有联系

<!-- more -->

---

 - Integrator模块
将输出量对时间进行积分（虽然模块有着$\frac{1}{s}$的标志，但不能将输入量进行拉氏变换后再输入）

 - 与拉氏变换联系
对于一个系统的微分方程：

$$
\cfrac{d^2y}{dt^2} = \cfrac{dy}{dt} + y + x
$$

式中，$x$为系统输出，$y$为系统输出。
可以化成如下形式，再使用Simulink的Integrator和Add模块搭建系统：

$$
y = \iint{(\cfrac{dy}{dt} + y + x)}dt
$$

也可以通过拉氏变换，化成如下形式，再使用Simulink的Transfer Fcn模块搭建系统：

$$
\begin{split}
s^2 Y(s) &= sY(s) + Y(s) + X(s) \\
&\Downarrow \\
Y(s) &= \cfrac{1}{s^2 - s -1} \cdot X(s)
\end{split}
$$

搭建的系统如下图所示（两种换建方法，其结果将是一样的）：

![integrator](integrator.png)
