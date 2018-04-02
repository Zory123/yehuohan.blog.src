---
title: C++的构造、析构、拷贝构造和赋值函数
categories:
  - 杂记
mathjax: false
tags:
  - c/c++
date: 2017-09-29 21:50:32
---

简单记下C++中类的构造函数、析构函数、拷贝构造函数、赋值函数（即operator=）基本形式与区别。

<!-- more -->

## 结构体(struct)
说类(class)之前，说下结构体。在C++中，结构体是一种特殊形态的类，区别如下：
结构体和类的唯一区别就是，结构体和类具有不同的默认访问控制属性。
 - class： 对于未指定访问控制属性的成员，其默认属性为private；
 - struct: 对于未指定任何访问控制属性的成员，其默认属性为public；

在C++中，结构体同样具有构造函数、析构函数、拷贝构造函数、赋值函数等函数。而且，类(class)还可以与结构体(struct)相互继承。

下面以一个结构体为例，来简单记下构造等函数的基本写法：

```cpp
struct DataPack
{
    int size;
    char* name;
};
```

## 构造函数与析构函数

如果没有定义构造函数与析构函数，C++则会定义默认的构造函数析构函数，默认的形式如下：

```cpp
struct DataPack
{
    int size;
    char* name;

    DataPack(){}
    ~DataPack(){}
};
```
 - 构造函数用于在创建对象时，给对象的成员进行赋值，不需要赋值用默认的即可；
 - 析构函数用于在消毁对象时，释放对象中指针成员指向的内存；


## 拷贝构造函数与赋值函数

同样，C++会定义默认的拷贝构造函数和赋值函数，如果没有的话。正因为有默认的，以下一般性的代码才可以执行：

```cpp
DataPack pack;
DataPack newpack1 = pack;       // 对象初始化，调用拷贝构造函数
DataPack newpack2(pack);        // 对象初始化，调用拷贝构造函数
DataPack newpack3;
newpack3 = pack;                // 对象赋值，调用赋值函数(operator)
```

但默认的拷贝构造函数和赋值函数是浅拷贝，即将两个对象对应的成员进行简单的赋值，若是有指针成员，在对象析构时会发生错误，拿指针来说，两个对象经的指针指向同一块内存，析构时，这块内存就会被delete两次，这明显不行。所有就需要深拷贝了，如下所示：

```cpp
struct DataPack
{
    int size;
    char* name;

    // 浅拷贝构造函数
    DataPack(const DataPack& dp){
        this->size = dp.size;
        this->name = dp.name;
    }
    // 深拷贝构造函数
    DataPack(const DataPack& dp){
        this->size = dp.size;
        this->name = new char[this->size];
        memcpy(this->name, dp.name, this->size);
    }

    // 浅拷贝赋值函数
    DataPack& operator=(const DataPack& dp){
        this->size = dp.size;
        this->name = dp.name;
        return *this;
    }
    // 深拷贝赋值函数
    DataPack& operator=(const DataPack& dp){
        this->size = dp.size;
        delete this->name;              // 先释放原来的内存
        this->name = new char[this->size];
        memcpy(this->name, dp.name, this->size);
        return *this;
    }
};
```

### 拷贝构造函数的几点说明
 - 默认拷贝构造函数没有处理static数据成员；
 - 拷贝构造函数必须是引用传递，如果是值传递，则会无限的调用拷贝构造函数，因为值传递本身就是先要调用拷贝构造函数；如果是指针传递，则只是构造函数，而不是拷贝构造函数；
 - 拷贝构造函数中不受private限制，即可以直接访问private成员变量；
 - 对于一个类X, 如果一个构造函数的第一个参数是下列之一，且没有其他参数，或其他参数都有默认值，那么这个函数是拷贝构造函数.

```
(1) X&  (2) const X&  (3) volatile X&  (4) const volatile X&
```

### 赋值函数(operator=)的几点说明
 - 赋值函数的前提是对象已经初始化，所在赋值函数中，对象先会丢弃原有的值（指针则先要释放内存），再赋予新的值（指针则重新申请内存）；
