---
title: 'C++中public,protected,private与继承的关系'
categories:
  - 杂记
mathjax: false
date: 2017-09-30 00:02:39
tags:
 - c/c++
---

记下public, protected, private与类继承的基本关系。

<!-- more -->

## 访问权限区别

| 访问属性| 说明                                                       |
| :---      | :---                                                   |
| public    | 可以被对象实体直接访问                                 |
| protected | 只允许在本类和子类中访问，对象实体通过public员函数访问 |
| private   | 只允许在本类中访问，对象实体通过public员函数访问       |



## 继承方式与权限的关系

| 基类访问属性 | 继承方式                | 子类访问属性 |
| :---         | :---                    | :---         |
| public       | public                  | public       |
| public       | protected               | protected    |
| public       | private                 | private      |
| protected    | public                  | protected    |
| protected    | protected               | protected    |
| protected    | private                 | private      |
| private      | public,protectd,private | 子类无权访问 |
