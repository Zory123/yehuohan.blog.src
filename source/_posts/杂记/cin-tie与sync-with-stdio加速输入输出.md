---
title: '[转]cin.tie与sync_with_stdio加速输入输出'
categories:
  - 杂记
mathjax: false
date: 2018-03-19 00:00:00
tags:
 - c/c++
---

[文章原链接：cin.tie与sync_with_stdio加速输入输出](http://www.hankcs.com/program/cpp/cin-tie-with-sync_with_stdio-acceleration-input-and-output.html)

<!-- more -->

## tie
 - `tie`是将两个stream绑定的函数，空参数的话返回当前的输出流指针。

```cpp
#include <iostream>
#include <fstream>

int main(int argc, char *argv[])
{
  std::ostream *prevstr;
  std::ofstream ofs;
  ofs.open("test.txt");

  // 直接输出到控制台stdout
  std::cout << "tie example:\n";

  // 空参数调用返回默认的output stream，也就是cout，输出到控制台stdout
  *std::cin.tie() << "This is inserted into cout\n";

  // cin绑定ofs，返回原来的output stream
  prevstr = std::cin.tie(&ofs);

  // ofs，输出到文件test.txt
  *std::cin.tie() << "This is inserted into the file\n";

  // 恢复
  std::cin.tie(prevstr);

  ofs.close();
  system("pause");
  return 0;
}
```

## sync_with_stdio

 - 这个函数是一个“是否兼容stdio”的开关，C++为了兼容C，保证程序在使用了std::printf和std::cout的时候不发生混乱，将输出流绑到了一起。

## 加速C++ IO

 - 我们可以在IO之前将`sync_with_stdio`解除绑定，这样做了之后要`注意不要同时混用cout和printf之类。`

 - 默认的情况下`cin`绑定的是`cout`，每次执行 `<<` 操作符的时候都要调用flush，这样会增加IO负担。可以通过`tie(0)`（0表示NULL）来解除`cin`与`cout`的绑定，进一步加快执行效率。

```
#include <iostream>
int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    // IO
}
```
