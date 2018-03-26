---
title: Style of c and cpp
categories:
  - 杂记
mathjax: false
date: 2017-07-21 20:41:15
tags:
---

Basic style of c and cpp.

<!-- more -->

---
## 目录结构
 - 文件：小写+下划线(如 ui_dw, ui_gw)
 - 目录：小写+连接符(如 inc, inc-cpp, inc-c)

---
## 程序编写

### 排版分段
 - 注释块：使用doxygen；
 - 程序块分段：

```
//===...===// (共占80个字符)
/* Marco */
...
/* Marco End */
//===...===//
```

### 类型定义
 - 宏定义：大写+下划线(如 BIT_SET，BIT_CLR)
 - struct, enum, class： 大写开头+大写字母分段

```cpp
typedef struct StrOk
{
	int var;
	Str(int _var):var(_var){}
}StrOk;
```

 - struct, enum, class： 小写开头+下划线母分段

```cpp
typedef struct str_ok_s
{
	int var;
	str_ok_s(int _var):var(_var){}
}str_ok_t;
```

### c变量和函数定义
 - 小写字母+下划线，以前缀分类

```
int     data_len;
void    set_data();

void    ty_set_data();
void    ty_is_equal();
```

### c++类的成员变量与成员函数
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

 - 其实混合风格也不错，自己能坚持下来就行

```
int     s_num;      // static
int     m_size;     // member
int*    p_array;    // pointer
void    initUi();
```

---
## Doxygen基本规范
 - 主页(mainpage)：写在一个主头件中，并将README.md作为subpage；
 - 模块(group)：将所有defgroup写在一个头文件（如：一个模块的主头文件中）中，使用addtogroup添加模块内容；
 - 文件列表(file)：只在头文件添加。

