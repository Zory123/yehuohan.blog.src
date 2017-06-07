---
title: ubuntu建立qt的默认打开方式
categories:
  - 杂记
date: 2017-06-08 00:50:17
tags:
---


更改文件的默认方式很容易，右键属性就可以了。
然而有时候程序装在了"～/"下时，右键属性时，就找不到所需要的程序了，比如qt。

<!-- more -->

# 设置右键菜单可以选择使用qtcreator打开
设置pro文件默认打开方式为qtcreator的方法如下：

- 建立软链接：

```bash
sudo ln -s ~/Qt5.6.0/Tools/QtCreator/bin/qtcreator /usr/local/bin/qtcreator
```

- 建立qtcreator.desktop

```bash
sudo vim /usr/share/applications/qtcreator.desktop
```

复制以下内容：

```bash
[Desktop Entry]
Name = Qt Creator
Comment = Open qt pro file
Exec = qtcreator %U
Terminal = false
StartupNotify = true
X-MultipleArgs = false
Type = Application
Categories = Utility;
Icon = /home/yehuohanxing/MyApps/Qt560/qt_logo.png
```
软件图标位置，可以自己选一个png图像，把png图像的绝对路径放这就可以
或者一步到位：


```bash
sudo cp ~/.local/share/applications/DigiaQt-qtcreator-community.desktop ./qtcreator.desktop
# 将其中的Exec改成 : Exec = qtcreator %U
```

到此，可以直接在终端中使用

```bash
qtcreator
```

命令来打开程序，如果开发的程序需要root权限运行，就可以用

```bash
sudo qtcreator
```
这样在Qt Creator中调试程序就是以root权限运行的。比如，开发串口程序时需要打开 /dev 下的设备文件，就需要root权限了。


# 设置在终端中直接调用qt程序命令

若是qt安装在$HOME下时，需要自己添加路径到PATH，才能在终端中直接调用qtcreator等程序

```bash
vim ～/.bashrc

//添加下面的内容
export PATH="$PATH:$HOME/Qt560/5.6/gcc_64/bin"
export PATH="$PATH:$HOME/Qt560/Tools/QtCreator/bin"

```

