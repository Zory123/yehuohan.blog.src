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

```python
class Foo:
    """ 测试类 """
    plst = []
    slst = []

    def __init__(self):
        self.plst = []      # Foo类的每个对象，plst均会指向新的列表引用

def foo_str(foo):
    """ 输出 """
    return "plst:{} slst:{}".format(foo.plst, foo.slst)

if __name__ == "__main__":
    foo1 = Foo()
    foo2 = Foo()        # foo2.slst与foo1.slst指向相同的列表引用
    foo1.plst = [1,1]
    foo1.slst = [1,1]   # foo1.slst指向了新的列表引用
    foo2.plst = [2,2]
    foo2.slst = [2,2]   # foo2.slst指向了新的列表引用
    print("foo1: {}".format(foo_str(foo1)))
    print("foo2: {}".format(foo_str(foo2)))

    foo3 = Foo()
    foo4 = Foo()        # foo3.slst与foo4.slst指向相同的列表引用
    foo3.plst.append(3)
    foo3.slst.append(3) # foo3.slst指向的列表引用添加元素
    foo4.plst.append(4)
    foo4.slst.append(4) # foo4.slst指向的列表引用添加元素
    # foo3.plst和foo4.plst在__init__时就指向了新的列表引用，故值不相同
    print("foo3: {}".format(foo_str(foo3)))
    # foo3.slst和foo4.slst一直指向相同列表引用，故值为[3,4]
    print("foo4: {}".format(foo_str(foo4)))


```
