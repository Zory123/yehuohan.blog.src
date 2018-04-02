---
title: windows下pip install utf-8问题
categories:
  - 杂记
mathjax: false
tags:
  - python
date: 2018-01-21 16:02:44
---

windows下使用`pip install`时，有时会遇到utf-8编码问。

<!-- more -->

- 原因

pip默认utf-8；

windows-cmd使用gbk，所以会报错；

Linux使用utf-8，所以不会报错；

 - 解决

在 `Python36\Lib\site-packages` 下创建 `sitecustomize.py`，内容如下：

```
import sys
sys.setdefaultencoding('gbk')
```

python会自动调用这个文件，即将默认编码改成gbk。

 - sitecustomize.py与vim的冲突

创建`sitecustomize.py`可以解决 `pip install` 的utf-8编码问题，但是会影vim插件，因为有些vim插件需要utf-8编码。

***实测解决办法：*** 安装时创建`sitecustomize.py`，安装完后删除即可。
