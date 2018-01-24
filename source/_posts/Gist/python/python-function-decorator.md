---
title: py:function decorator
categories:
  - Gist
mathjax: false
date: 2017-08-09 21:16:24
tags:
 - python
---

> File : func_decorator.py
> Type : python
> Brief : simple demo of python function decorator

<!-- more -->

---

```python
#===============================================================================
# simple demo of function decorator
# hello 需要以函数fn为参数，这样才能修饰函数
def hello(fn):
    def wrapper():
        print('hello , {}'.format(fn.__name__))
        fn()
        print('bye, {}'.format(fn.__name__))
    return wrapper

# foo将被解释成 foo = hello(foo)
@hello
def foo():
    print('this is foo')

def bar():
    print('this is bar')


#===============================================================================
# parameter of function decorator
def make_htmltag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = "class='{0}'".format(kwds['css_class']) if 'css_class' in kwds else ''
        def wrapped(*args, **kwds):
            return '<' + tag + css_class + '>' + fn(*args, **kwds) + '</' + tag + '>'
        return wrapped
    # real_decorator 才是真正修饰 fn 的 decorator
    return real_decorator

@make_htmltag(tag='b', css_class = 'bold_css')
@make_htmltag(tag='i', css_class = 'italic_css')
def get_hello():
    return 'hello world'


#===============================================================================
# decorator 作缓存
def memo(fn):
    # cache 为缓存字典
    cache = {}
    miss = object()
    def wrapper(*args):
        # 获取对应键 args 的值，没有则返回 miss
        # 若返回 miss，则 result 与 miss 引用同一对象
        result = cache.get(args, miss)
        # 判断 result 和 miss 的id，即引用的是否为同一对象
        if result is miss:
            # 引用同一对象
            result = fn(*args)
            # 缓存计算过的数据
            cache[args] = result
        return result
    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


#===============================================================================
if __name__ == "__main__":
    foo()
    # bar()效果和被 @hello 修饰的foo()是一样的
    bar = hello(bar)
    bar()

    # 相当于给 get_hello 返回的字符串添加 bold 和 italic
    print(get_hello())

    # 可以去掉 @memo 对比一下时间
    print(fib(100))
```
