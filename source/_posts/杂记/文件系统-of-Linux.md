---
title: 文件系统 of Linux
categories:
  - 杂记
date: 2017-06-09 00:02:37
tags: linux
---

记录平时了解到的Linux中的一些文件目录的作用
<font color=red size=3>
- 掌握的:详细记录 
- 接触的:粗略记录 
- 不懂的:以后记录 
</font>


<!-- more -->


---
# **/ 下的目录**
 - "/"     : 根目录
 - "root"  : root用户相关文件，root登录时，"～/"就是此目录
 - "home"  : 普通用户存放目录，"~/"就是当前登录用户的个人目录
 - "bin"   : 存放普通命令的目录
 - "sbin"  : 存放需要一定权限的命令的目录
 - "mnt"   : 默认挂载目录
 - "boot"  : 存放系统引导文件
 - "etc"   : 存放配置相关文件
 - "dev"   : 接口设备文件目录，如硬盘sda1,sda2等
 - "usr"   : 存许应用程序和文件
 - "media" : ubuntu中用户默认挂载目录


# **/dev**
 * /dev/ttySn   : 串行端口终端，如ttyS0，ttyS1等
 * /dev/tty     : 控制终端
 * /dev/console : 即控制台，是与操作系统交互的设备，系统将一些信息直接输出到控制台上
 * /dev/ttyUSBn : USB设备端口

# **/etc**
- /etc/fstab                                : 包含了电脑上的存储设备及其文件系统的信息，如boot分区的挂载盘信息，若是挂载到boot的分区uuid变了，fstab中的信息相应也得改。
- /etc/apt/sources.list                     : 系统软件源，可以自己增加一些软件源。
- /etc/gnome/defaults.list                  : 保存了全局文件类型的打开方式
- ~/.local/share/applications/mimeapps.list : 保存了个人的打开方式（局部个人设置，当两着对于同一类型文件设定的内容不一致时，优先采用局部的个人设置）
- /etc/group                                : 户组的配置文件，内容包括用户和用户组，并且能显示出用户是归属哪个用户组或哪几个用户组 。
- /etc/passwd                               : 所有用户帐号的信息，[注册名：口令：用户标识号：组标识号：用户名：用户主目录：命令解释程序]
- /etc/init.d                               : 包含许多系统各种服务的shell脚本（SysVinit工具所包含的函数库）

```bash
/etc/init.d/mysql stop(restart,start)
service mysql stop(restart,start) 
	#  停止，重启，打开mysql
	#  service 命令即去/etc/init.d目录下寻找相应的服务
```

- /etc/init     : 包含的是Upstart（Ubuntu中Sysinit的替代版本）的配置文件，和/etc/init.d的作用几乎差不多。/etc/init可以看作/etc/init.d的演化版本。
- /etc/rc.local : rc.local脚本是在系统初始化级别脚本运行之后再执行的，可以在里面添加想在系统启动之后执行的脚本，如在里面添加nfs挂载/mount脚本。
- /etc/rcN.d    : 运行级别目录

```
# linux有0-6个级别:
0 : 关机，该运行级别用于系统管理员迅速关机，不能为默认的运行级别。
1 : 单用户模式，也称为维护模式。该运行级别下网络接口、文件共享等服务不能使用。
2 : 多用户模式，这是debian系统的默认运行级别，字符界面。
3 : 多用户模式，这是redhat系统的默认运行级别，字符界面。
4 : 系统未使用，保留。
5 : 多用户模式，提供GUI界面。。
6 : 重启，该运行级别用于系统管理员重启系统，不能为默认的运行级别。

# rcN.d目录下都是一些指向init.d目录下的service脚本的符号链接文件，系统会根据指定的运行级别进入对应的rcN.d目录
K开头的，系统将终止对应的服务
S开头的，系统将启动对应的服务

查看运行级别用     : runlevel
进入其它运行级别用 : init N，init0为关机，init 6为重启系统

```

* /etc/profile : 该文件登录操作系统时，为每个用户设置环境信息，当用户第一次登录时,该文件被执行。也就是说这个文件对每个shell都有效，用于获取系统的环境信息。
* /etc/bashrc  : 为每一个运行bash shell的用户执行此文件，当bash shell被打开时,该文件被读取。也就是说，当用户shell执行了bash时，运行这个文件。（附：     : ~/.bashrc 存储的是专属于个人bash shell的信息）


# **/usr**
 - /usr/local/bin    : 可以放用户自己的程序，程序或链接放到这后，在终端输入程序文件名就可以运行，[相关的一例](http : //blog.csdn.net/yehuohan/article/details/51333880)
 - /usr/local/lib    : 用户库文件位置
 - /usr/local/etc    : 用户配置文件位置
 - /usr /local/share : 用户其它的资源文件位置


# **/home**
 - ~/                       : 即用户主目录，/home/user/
 - ~/.bashrc                : 保存个人的一些个性化设置，如命令别名、路径等
 - ~/.config/user-dirs.dirs : 配置用户文件目录的文件
