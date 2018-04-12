---
title: 'py:类的列表成员类型'
categories:
  - Gist
mathjax: false
date: 2018-01-24 15:24:53
tags:
---

> File : class_member.py
> Type : python
> Brief : python列表成员引用指向说明

<!-- more -->

---

一般而言：
 - `__init__`外的为类的静态成员
 - `__init__`内的为类的实例对象的成员

```python
class MyClass:
    static_elem = 123

    def __init__(self):
        self.object_elem = 456

c1 = MyClass()
c2 = MyClass()

# Initial values of both elements
>>> print c1.static_elem, c1.object_elem 
123 456
>>> print c2.static_elem, c2.object_elem
123 456

# Nothing new so far ...

# Let's try changing the static element
MyClass.static_elem = 999

>>> print c1.static_elem, c1.object_elem
999 456
>>> print c2.static_elem, c2.object_elem
999 456

# Now, let's try changing the object element
c1.object_elem = 888

>>> print c1.static_elem, c1.object_elem
999 888
>>> print c2.static_elem, c2.object_elem
999 456
```
