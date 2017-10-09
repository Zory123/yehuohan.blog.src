---
title: implement atan2 from atan
categories:
  - Gist
mathjax: true
date: 2017-08-15 17:42:53
tags:
 - python
---

> File : [atan2.py](atan2.py) *(直接右键另存为下载)*
> Type : python
> Brief : simple implementation of atan2 from atan

<!-- more -->

---

```python
from math import atan
from math import atan2
from math import pi

# atan2 implementation from atan
# atan2(sin, cos)
def myatan2(dy, dx):
    if dx == 0:
        if dy > 0:
            return pi/2
        elif dy < 0:
            return -pi/2
    else:
        re = atan(dy / dx)
        if dx > 0:
            return re
        elif dx < 0 and dy >= 0:
            return re + pi
        elif dx < 0 and dy < 0:
            return re - pi


if __name__ == "__main__":
    dx = 3
    dy = -4
    print("atan  : {0:8f} rad".format(atan(dy/dx)))
    print("atan  : {0:8f} deg".format(atan(dy/dx)*180/pi))
    print("atan2 : {0:8f} rad".format(atan2(dy,dx)))
    print("atan2 : {0:8f} deg".format(atan2(dy,dx)*180/pi))
    print("mytan2: {0:8f} rad".format(myatan2(dy,dx)))
    print("mytan2: {0:8f} deg".format(myatan2(dy,dx)*180/pi))
```

 - atan2的范围为 [$-\pi$,$\pi$]
 - atan的范围为 [$\cfrac{-\pi}{2}$,$\cfrac{\pi}{2}$]

![atan2](a2.gif)
