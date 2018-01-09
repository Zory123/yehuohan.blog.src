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

## 类型定义
 * 宏定义
 大写+下划线连接，例如：BIT_SET

 * struct, enum, class：

```cpp
// 大写开头
typedef struct _StrOk
{
	int var;
	_Str(int _var):var(_var){}
}StrOk;

// 小写带后缀
typedef struct str_ok_s
{
    int val;
}str_ok_t;
```


## c变量和函数定义
 - 下划线连接小字字母，可以添加前缀

```
int     data_len;
void    set_data();

void    ty_set_data();
void    ty_is_equal();
```

## c++类的成员变量与成员函数
 - 小写字母和下划线连接

```
int     s_num;      // static
int     m_size;     // member
int*    p_array;    // pointer
void    init_ui();
```

 - 小写字母开头和大写字母分段

```
int     sNum;       // static
int     mSize;      // member
int*    pArray;     // pointer
void    initUi();
```

其实混合风格也不错，自己能坚持下就行：

```
int     s_num;      // static
int     m_size;     // member
int*    p_array;    // pointer
void    initUi();
```

---
# Doxygen基本规范
 - 主页(mainpage)
 写在一个主头件中，并将README.md作为subpage。
 
 - 模块(group)
 将所有defgroup写在一个文件（如：一个模块的主头文件中）中，使用addtogroup添加模块内容。
 
 - 文件列表(file)
 只在头文件添加。

