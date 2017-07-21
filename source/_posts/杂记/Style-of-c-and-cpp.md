---
title: Style of c and cpp
categories:
  - 杂记
mathjax: false
date: 2017-07-21 20:41:15
tags:
---

Basic Style of c and cpp.

<!-- more -->



---
# 文件
 * 命名：小写
 * 分类：用文件夹(如：inc, src, driver等)，或用前缀(如：ui_xxx, def_xxx)
 

---
# 程序编写

## 排版分段
 * 注释块
 使用doxygen
 
 * 程序块分段
使用以下格式

```
//===...===// (共占80个字符)
/* Marco */
...
/* Marco End */
//===...===//
```

## 全局定义
 * 宏定义
 大写+下划线连接，例如：BIT_SET
 * 结构体
基本格式如下：

```
typedef struct _Str
{
	int var;
	_Str(int _var):var(_var){}
}Str;
```

## c变量与函数
 *  基本风格一：下划线连接小字字母
 data_len, set_data()
 
 * 基本风格二：大小字母连接
 dataLen, setData();
  
  
## c++类
 * 成员变量与函数基本风格一：
  - 变量
  以m开头，以下划线连接，m_xxx
  - 函数
  小写字母和下划线连接，init_ui(), set_ui()
	
 * 成员变量与函数基本风格二：	
  - 变量
  以m开头，以下划线连接，mXXX
  - 函数
  小写动词+大写字母，initUi(), setUi()
  
## 临时变量
 * 指针
 pVar或var_ptr

 
---
# Doxygen基本规范
 - 主页(mainpage)
 写在一个主头件中，并将README.md作为subpage
 
 - 模块(group)
 将所有defgroup写在一个文件（如：一个模块的主头文件中）中，使用addtogroup添加模块内容
 
 - 文件列表(file)
 只添加头文件

