---
title: 软件应用之 node.js
categories:
  - 杂记
mathjax: false
date: 2017-08-11 23:02:41
tags:
 - node.js
---

几个基于node.js的工具，记一下node.js以及相应工具的基本应用。

<!-- more -->

---
# Node.js

node.js是运行在服务端的JavaScript。

## node
Linux下接用包管理器即可下载node.js，windows可以到[官网](https://nodejs.org/en/)下载安装包，然后安装即可。
安装完后，如果nodsjs的安装路径不在环境变量中，添加即可，因为npm和node均在安装目录下，如windows安装在D盘，则npm和node位置为：

```bash
D:\nodejs\node.exe
D:\nodejs\npm.cmd
```

如果要运行一个js文件，用如下命令即可：

```bash
node file.js
```

## npm
npm是随node.js一起安装的包管理工具。Windows下使用之前，一般设置一下module和cache路径：

```bash
npm config set prefix "D:/nodejs/node_modules"
# 设置module路径，即将下载的包安装到module路径，这也为全局下载路径
npm config set cache "D:/nodejs/node_modules/npm-cache"
# 设置npm的cache路径
npm config list
# 查看用户修改的参数
npm config list -l
# 查看用户修改的参数，以及所有默认的参数
```

设置好module路径后，还需要将其（即D:/nodejs/node_modules）加入到环境变量中，因为包执行文件就在module路径下，如安装了一个hexo-cli，则其执行文件在：

```bash
D:/nodejs/node_modules/hexo.cmd
```


---
# hexo

hexo是一个昨用Markdown生成静态博客的工具，hexo-cli是对hexo功能的命令封装，通过命令行(cli)调用。

```bash
npm install -g hexo-cli
# 安装hexo-cli
# -g表示全局安装，即安装在自己设置的module路径
# 没有-g参数，则安装在执行命令所在的目录
hexo init ./blog
# 初始化博客，博客源文件在blog下
hexo generate
# 生成静态网页，即将markdown生成html
hexo server
# 本地预览博客网页 
# 这样会启一个端口为4000用于预览的服务器，打开http://localhost:4000可预览
```


---
# GitBook

GitBook是一个基于node.js的命令行工具，可使用Github/Git和Markdown来制作精美的电子书。
[gitbook入门教程](http://www.chengweiyang.cn/gitbook/gitbook.com/edit.html)

```bash
npm install -g gitbook-cli
# 安装gitbook-cli
gitbook init ./docs
# 在docs初始化书籍目录
gitbook serve ./docs
# 本地预览书籍，书籍目录为docs
```


---
# docsify
[docsify](https://docsify.js.org/#/zh-cn/) 是一个使用markdown动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 .md 转成 .html 文件，所有转换工作都是在运行时进行。

```bash
npm install -g docsify-cli
# 安装docsify
docsify init ./docs
# 初始化文档，在dosc中写文档
docsify serve ./docs
# 本地预览文档，打开 http://localhost:3000 可预览
```


