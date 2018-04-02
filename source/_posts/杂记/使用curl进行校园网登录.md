---
title: 使用curl进行校园网登录
categories:
  - 杂记
mathjax: false
tags:
  - shell
date: 2017-09-30 00:22:13
---

在linux终端下且使用校园网时，校园网登录就成了一个比较烦的事。大多是通过另一台电脑开wifi，或是手机连校园网，然后给电脑当有线网卡使。如果校园网是网页登录的话，通过curl直接登录校园网是一个不错的选择。

<!-- more -->

这里记下我使用curl登录校园网的过程，不同的校园网不一样，可以借鉴方法。

 - 首先要找到需要提交的数据，可以直接用curl下载网页，然后找在网页中找form，看提交的内容是什么：

```bash
# 下载网页，在login.htm中找需要提交的内容即可
curl 222.222.xx.xx > login.htm
```

 - 或者直接利式具截获提交的数据，我用Wireshake截获的数据如下：

![login](login.png)

 - 接下来就是利用curl登录了：

```bash
# username为用户名，password为用户密码
# v6ip是自己的IPv6地址，最后的222.222.xx.xx自然是登园网登录网址了
curl -d "DDDDD=username&upass=password&v6ip=xxx.xxx&0MKKey=123456789" 222.222.xx.xx
```

 - 相同的步骤来找注销需要提交的数据，我这里只需要打开一个网页即可：

```bash
curl 222.222.xx.xx/*.htm
```
