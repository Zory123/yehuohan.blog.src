---
title: C++中enum和class重名问题
categories:
  - 杂记
mathjax: false
date: 2017-10-02 23:10:37
tags:
 - c/c++
---

C++中enum和class重名的时候，会有一个很坑人的提示。

<!-- more -->

直接上代码：

```cpp
typedef enum MyEnum
{
	Foo,
}MyEnum;

class Foo{
public:
	Foo() {}
	~Foo() {}
};

int main()
{
	Foo w;
	return 0;
}
```
问题很简单，**如果enum中的元素与class的重名了**，c++编辑器（我试过g++和vc）的错误提示是这样的：

```
error C2146: 语法错误: 缺少“;”(在标识符“w”的前面)
error C2065: “w”: 未声明的标识符
```

如果enum和class的声明不在同一个文件，而是通过头文件include来的，看到这样的提示，压根就不知道从哪查起。
特别是如果习惯了像下面那样使用enum的话，更加不会想到往enum查问题。

```
MyEnum fc = MyEnum::Foo
```

唉，说多了都是泪，都往文件编码查看问题了，就是没想到问题重名问题。
