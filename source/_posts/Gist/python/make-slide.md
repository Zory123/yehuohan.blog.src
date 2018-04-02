---
title: make slide
categories:
  - Gist
mathjax: false
tags:
  - python
date: 2017-08-09 11:04:47
---

> File : [make_slide.py](make_slide.py) *(直接右键另存为下载)*
> - Type : python
> - Brief : commands converting markdown-file to slide-html

<!-- more -->

---


```python
import os
import sys

# 转换函数
def convert_slide(markdown):
    os.system('pandoc {0} -o {0}.html -t revealjs -s -V theme=beige'.format(markdown))

# 获取md文件
def get_mdfile(diretory):
    retlist = []
    for item in os.listdir(diretory):
        if item[-2:] == 'md' and item[0] != '.':
            retlist.append(item)
    return retlist


if __name__ == "__main__":
    mdfile = '' 
    if len(sys.argv) == 1:
        for ele in get_mdfile(os.getcwd()):
            print(ele)
        mdfile = input('Select the markdown file above : '.format(os.getcwd()))
    elif len(sys.argv) == 2:
        mdfile = sys.argv[1]
    else:
        exit()

    print('Convering {} ......'.format(mdfile))
    convert_slide(mdfile)
```
