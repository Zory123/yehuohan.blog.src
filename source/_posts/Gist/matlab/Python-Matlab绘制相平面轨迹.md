---
title: Python-Matlab绘制相平面轨迹
categories:
  - Gist
mathjax: true
date: 2017-12-19 11:20:00
tags:
 - python
 - matlab
---

> File : [python实现-phase.py](phase.py)
> File : [matlab实现-phase.m](phase.m)
> File : [simulink实现-phase.slx](phase.slx)
> Type : Python & Matlab
> Brief : 绘制相平面轨迹

<!-- more -->

---

示例二阶方程为：

$$
\ddot{x} + \dot{x} + 0.5x = 0
$$

三种实现的结果相同。

- python 实现

```python
import matplotlib.pyplot as plt
import math

x = 0           # x初始
dx = 10         # dx初值
time = 0        # 仿真时间
dt = 0.001      # 积分步长
size = 20000
p_dx = [0 for x in range(size)]
p_x = [0 for x in range(size)]

for k in range(size):
    ddx = - dx - 0.5 * x
    dx += ddx * dt
    x += dx * dt
    p_dx[k] = dx
    p_x[k] = x
    time += dt

print("Time: {}".format(time))
plt.plot(p_x, p_dx)
plt.show()
```

- matlab 实现

```matlab
x = 0;          % x初值
dx = 10;        % dx初值
n = 1;          % 下标
time = 0;       % 仿真时间长度
dt = 0.001;     % 积分步长

for i = 1:20000
    ddx = -dx - 0.5 * x;
    dx = dx + ddx * dt;
    x = x + dx * dt;

    p_dx(n) = dx;
    p_x(n) = x;
    n = n + 1;
    time = time + dt;
end

figure(1);
plot(p_x, p_dx);

```

 - simulink实现

![phase.xls](p1.png)
