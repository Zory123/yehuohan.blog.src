---
title: 'Windows搭建类UNIX环境: Msys2+MinGW-w64'
categories:
  - 极文
date: 2017-06-09 00:36:01
tags: 
 - msys2
 - mingw-w64
---


---
# 安装Msys2
Msys2现在维护得更好，软件更新更方便，推荐使用Msys2，同时这里将不再介绍msys的安装过程。

 - 下载Msys2
 到[Msys2官网](http://www.msys2.org/) 下载最新版Msys2。
 可以下载exe安装包，也可以下载压缩包，解压出来的文件夹为msys64（这里使用64位)。
 
<!-- more -->

 - 安装软件
Msys2使用pacman管理软件。pacman的基本使用如下：

```bash
pacman -S <packge-name> 	# 安装软件
pacman -U <gz-file>			# 安装本地包，其扩展名为 pkg.tar.gz
pacman -Syu             	# 同步Msys2源，并更新 
pacman -Sy					# 仅同步源 
pacman -Su              	# 更新系统
pacman -Sy <packge-name>	# 同步源后再安装软件
pacman -R <packge-name> 	# 该命令将只删除包，不包含该包的依赖。
pacman -Rs <packge-name> 	# 在删除包的同时，也将删除其依赖。
pacman -Rd <packge-name> 	# 在删除包时不检查依赖。
pacman -Ss <keywords> 		# 这将搜索含关键字的包。
pacman -Qi <packge-name>	# 查看有关包的信息。
```

 安装Msys2后，或解压Msys2后，第一次运行下msys2_shell.cmd，提示第一次设置初始化完毕后，就可以运行Msys2.exe、mingw64.exe或mingw32.exe，主要区别：

```
# mingw32 优先使用 msys64/mingw32 下的工具;
# mingw64 优先使用 msys64/mingw64 下的工具;
# msys2   两个都不使用，只用自身 msys 的工具;
```

* 升级msys2
一般第一次打开msys2用“pacman -Syu”全面升级，然后会提示关闭终端，再次打开后再一次运行"pacman -Syu"。
若是不想升级可以直接用pacman安装自需要的软件，如vim，git，gcc(即MinGw)等。
 
- 安装Vim
使用命令：

```bash
pacman -S vim
```

即可以安装vim。安装完后在Msys2的~/下touch一个.vimrc，里面加入设置：

```bash
set bs=2
```

不然vim在插入模式下的退格不能用。

* 注意事项1：
Msys2的配置文件（~/.gitconfig, ~/.ssh/, ~/.vimrc等都在home下，注意别随便删除 ）。
* 注意事项2：
将Msys64/usr/bin加入windows环境变量中后，就可以在cmd中直接使用Msys2中安装的vim，git等软件（如以编写bat脚本，使用git管理软件版本）
 

---
# 安装MinGw-w64

可以通过pacman直接安装MinGw-w64，也可以下装安装包自，自己放置，pacman一条命令的事，这里讲下自己手动安装。
- 下载
  - 使用[mingw-w64-install.exe](http://sourceforge.net/projects/mingw-w64/files/mingw-w64/mingw-w64-release/)下载，图像界面，简单方便。
  - 也可以直接下载[编译好的版本](http://sourceforge.net/projects/mingw-w64/files/)，然后到下列路径下载相应的版本：
  	i686 => Home / Toolchains targetting Win32 / Personal Builds / mingw-builds
  	x86_64 => Home / Toolchains targetting Win64 / Personal Builds / mingw-builds
  	(这里以下载的x86_64-5.3.0-release-posix-sjlj-rt_v4-rev0.7z为例)

- 安装：
无论是exe安装还是自己解压缩，最好直接将到mingw64文件夹直接放在/Msys64/mingw64下，（原本就已经建好mingw64，直接合并即可），因为Msys2可以自动设置/Msys64/mingw32和/Msys64/mingw64的路径，不需要自己再往/etc/profile添加路径。此时，打开/Msys64/mingw64.exe后就可以使用gcc了。
{% asset_img 01.png %}
不过windows的cmd还不能直接用，因为还没添加windows环境变量。同时要注意，即使设置好mingw64的windows环境变量，Msys2也不会读取。
 
- 添加mingw64的windows环境变量：
添加 D:\msys64\mingw64\bin到PATH环境变量中，打开cmd就可使用gcc了，如：

```bash
gcc -v
	# 用此命令可以查看gcc版本。
```

- 添加MingW64的32位环境变量：
  添加X:\Msys64\mingw64\x86_64-w64-mingw32\lib32到环境变量PATH中。

- 编译32位程序：
```bash
gcc -m32 main.c -o main
	# 生成32位的main程序
windres --target=pe-i386
	# 对于32位程序资源文件的编译，需要添加pe-i386参数

```

- 添加"make"：
将D:\Msys64\mingw64\bin\mingw32-make.exe复制一份，重命名为make.exe，这样在windows下就可以使用make命令了。


---
# 附：编译vs使用的lib库
- 生成lib

```bash
	# generate def file
	gendef xxx.dll
	# generate lib file
	dlltool -D xxx.dll -d xxx.def -l xxx.lib
```

-  MinGw未生成.dll动态库
```bash
	# 在configure时使用下面的参数
	./configure --disable-static --enable-shared
```

- 直接使用.dll.a
mingw编译出来的静态库后缀名为.a，编译出来的动态库的导入库后缀名为.dll.a，而在windows下后缀名为.lib的库可能是静态库也可能是动态库的导入库。
mingw编译出来的动态库的导入库.dll.a可以直接在vc中直接使用，例如：

```
#pragma comment(lib, "xxx.dll.a")
```

---
# 附：相关说明
- MinGW32和MinGW-w64：
MinGW32先开发，只能编译32位程序；
MinGW-w64从MinGW32发展而来，支持编译64和32位位程序，同时可以进行交叉编译。

- MinGW-w64类型:
	x86_64 : 支持在x64和x86上运行
	i686   : 支持在x86上运行

- i386/i686/x86_64区别 
 - i386 适用于intel和AMD所有32位的cpu，以及采用X86架构的32的cpu。
 - X86_64 适用于intel和AMD采用X86架构的64位cpu，兼容32位。
 - I686 只是i386的一个子集,支持的cpu从Pentium 2 (686)开始,之前的型号不支持。

- 关于mingw-w64-x86_64:
 生成64位库只要用默认的参数编译即可,而生成32位库则要用-m32参数编译.

- 对于mingw-w64-i686:
 默认生成32位程序
		
- 对于seh sjlj dwrf区别
 - SJLJ (setjmp/longjmp): available for 32 bit and 64 bit
 - DWARF (DW2, dwarf-2): available for 32 bit only
 - SEH (zero overhead exception): will be available for 64-bit GCC 4.8.

- Msys说明
 MSYS是“Minimal SYStem”的缩写，是一个Bourne Shell命令行解释器，也是MinGW的补充，用来在MS Windows上移植一些开源的程序。

- Msys2说明
 MSYS2(Minimal SYStem 2)是一个MSYS的独立改写版本，主要用于 shell 命令行开发环境。同时它也是一个在Cygwin （POSIX 兼容性层） 和 MinGW-w64基础上产生的，追求更好的互操作性的 Windows 软件。


