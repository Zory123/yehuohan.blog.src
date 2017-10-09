---
title: c/c++:define usage
categories:
  - Gist
mathjax: false
date: 2017-08-09 13:23:36
tags:
 - c/c++
---

> File : define usage.h
> Type : c/c++
> Brief : define usage

<!-- more -->

---

```c++

/*
1.  宏是作文本替换
2.  替换的终止条件是：文件中不再含有宏
3.  当宏参数是另一个宏的时候，凡宏定义里有用'#'或'##'的地方宏参数是不会再展开，
    所有#或##的宏需要增加一层转换宏
*/

#define TEST        hello
#define _TO_STR(s)  #s              // 转换宏
#define TO_STR(s)   _TO_STR(s)
// TO_STR(TEST)第一次展开为：_TO_STR(hello)，然后再展开为 #hello，
// 之后hello即使是宏也不会再展开，而是为成字符串"hello"

#define     LCD_RST  PTA6
#define     _PTXn_T(ptxn,type)   (ptxn##_##type)
#define     PTXn_T(ptxn,type)    _PTXn_T(ptxn,type)
// PTXn_T(LCD_RST,OUT) 的第一次展开就会变成 ：_PTXn_T(PTA6,OUT)
// 第二次展开就会变成：PTA6_OUT 


// 3、得到指定地址上的一个字节或字 
#define  MEM_B( x )  ( *( (byte *) (x) ) ) 
#define  MEM_W( x )  ( *( (word *) (x) ) ) 

// 4、求最大值和最小值 
   #define  MAX( x, y ) ( ((x) > (y)) ? (x) : (y) ) 
   #define  MIN( x, y ) ( ((x) < (y)) ? (x) : (y) ) 

// 5、得到一个field在结构体(struct)中的偏移量 
#define FPOS( type, field )   ( (dword) &(( type *) 0)-> field ) 

// 6、得到一个结构体中field所占用的字节数 
#define FSIZ( type, field ) sizeof( ((type *) 0)->field ) 

// 7、按照LSB格式把两个字节转化为一个Word 
#define  FLIPW( ray ) ( (((word) (ray)[0]) * 256) + (ray)[1] ) 

// 8、按照LSB格式把一个Word转化为两个字节 
#define  FLOPW( ray, val ) \ 
  (ray)[0] = ((val) / 256); \ 
  (ray)[1] = ((val) & 0xFF) 

// 9、得到一个变量的地址（word宽度） 
#define  B_PTR( var )  ( (byte *) (void *) &(var) ) 
#define  W_PTR( var )  ( (word *) (void *) &(var) ) 

// 10、得到一个字的高位和低位字节 
#define  WORD_LO(xxx)  ((byte) ((word)(xxx) & 255)) 
#define  WORD_HI(xxx)  ((byte) ((word)(xxx) >> 8)) 

// 11、返回一个比X大的最接近的8的倍数 
#define RND8( x )       ((((x) + 7) / 8 ) * 8 ) 

// 12、将一个字母转换为大写 
#define  UPCASE( c ) ( ((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c) ) 

// 13、判断字符是不是10进值的数字 
#define  DECCHK( c ) ((c) >= '0' && (c) <= '9') 

// 14、判断字符是不是16进值的数字 
#define  HEXCHK( c ) ( ((c) >= '0' && (c) <= '9') ||\ 
                       ((c) >= 'A' && (c) <= 'F') ||\ 
                       ((c) >= 'a' && (c) <= 'f') ) 

// 15、防止溢出的一个方法 
#define  INC_SAT( val )  (val = ((val)+1 > (val)) ? (val)+1 : (val)) 

// 16、返回数组元素的个数 
#define  ARR_SIZE( a )  ( sizeof( (a) ) / sizeof( (a[0]) ) ) 

// 17、返回一个无符号数n尾的值MOD_BY_POWER_OF_TWO(X,n)=X%(2^n) 
#define MOD_BY_POWER_OF_TWO( val, mod_by ) \ 
           ( (dword)(val) & (dword)((mod_by)-1) ) 

// 18、对于IO空间映射在存储空间的结构，输入输出处理 
#define inp(port)         (*((volatile byte *) (port))) 
#define inpw(port)        (*((volatile word *) (port))) 
#define inpdw(port)       (*((volatile dword *)(port))) 

#define outp(port, val)   (*((volatile byte *) (port)) = ((byte) (val))) 
#define outpw(port, val)  (*((volatile word *) (port)) = ((word) (val))) 
#define outpdw(port, val) (*((volatile dword *) (port)) = ((dword) (val))) 

// ANSI标准说明了五个预定义的宏名。它们是： 
//_LINE_ 
//_FILE_ 
//_DATE_ 
//_TIME_ 
//_STDC_ 
```
