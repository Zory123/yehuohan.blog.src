---
title: U盘中的Boot
categories:
  - 杂记
date: 2017-06-08 23:32:50
tags: 
 - boot
 - refind
 - grub4dos
---


**记一下自己用的grub4dos和refind的使用记录。
grub4dos : 用于管理bios的启动；
refind   : 用于管理efi启动，简单方便实用，界面美观，配合efi shell，UEFI启动超级容易。
**

<!-- more -->


---
# grub4dos安装
 - grub4dos下载：http://grub4dos.chenall.net/
 - 安装方式：bootice 或 grubinst 或 bootlace.com
  - bootice： http://www.ipauly.com/， 除了安装外还有众多其它功能；
  - grubinst：安装方便；
  - bootlace.com：最好对dos命令比较熟悉，对硬盘分区命名等参数熟悉。


---
# grub4dos使用
## 设备命名
- 设备有ud, pd, nd, hd, cd, fd，

```
	hd ： 磁盘类
	cd ： 光驱类
	fd ： 软驱类
```

- 对应的16进制数值

```
	fd0   : 0x00
	pxe   : 0x21
	ud    : 0x23
	hd0   : 0x80
	hd32  : 0xa0
	hd127 : 0xff
```

- 其它规则

```
 ()         ： 空括号，表示当前设备
 (md)       ： 内存驱动器，实现了将整个内存作为一个磁盘驱动器来访问
 (hd0)      ： 第一块硬盘，0x80即是第一块硬盘，bootlace.com 0x80 即安装grldr到第一块硬盘
 (hd1)      ： 第二块硬盘，0x81即是第二块硬盘
 (hd-1)     ： 最后一个硬盘
 (hd0, 0)   ： 第一块硬盘第一主分区，主分区（包括扩展分区在内）最多4个（0~3）
 (hd0, 4)   ： 第一块硬盘第一逻辑分区，逻辑分区从4开始
 (hd0)+1    ： 将第一块硬盘的第1个扇区当作一个文件
 (hd0, 0)+2 ： 将第一块硬盘的第一个分区的前2个扇区当作一个文件
 (hd0)512+2 ： 将第一块硬盘的第512个扇区后的2个扇区当作一个文件
```
 

---
## grub4dos命令参数
配置文件有问题时，自己就可以敲命令启动了。

```bash
GRUB --config-file=str
	# 启动grub，str可以是命令(如str可以为 "reboot")，也可以是lst文件(如str可以为 (hd0,0)/menu.lst)
ls (hd0,0)/boot/
	# 列出boot下的目录和文件
ls /boot
	# 列出boot开头的目录和文件
ls dev
	# 列出所有驱动器（不包括分区）
debug on
find
	# 列出所有磁盘，包括分区（必须在debug on模式下）
find --set-root /ntldr
	# 查找包含/ntldr的设备，把第一个找到的设为当前设备
find --set-root uuid () xxxxxxxx
uuid xxxxxxxx
	# 设置uuid为xxxxxxxx的分区分根分区
uuid ()
uuid (hd0,0)
	# 显示设备的uuid
root
	# 显示当前设设备名称及相当信息
root (hd0,0)
	# 把(hd0,0)作为当前磁盘
map /pe.iso (0xff)
map --hook
	# 将pe.iso映射到(hd127)仿真磁盘，pe.iso要求连续存放，不能有碎片
map --mem /pe.iso (0xff)
	# 将pe.iso加载到内存，然后映射，pe.iso可以有碎片，要求内存容量比pe.iso大
map () (hd0)
map (hd0) ()
map --rehook
	# 磁盘交换，即把当前设备变成第一块硬盘
uuid
	# 列出所有设备的uuid
uudi (hd0,0)
	# 列出(hd0,0)的uuid
configfile /menu.lst
	# 加当menu菜单配置文件
halt 
	# 关机
reboot
	# 重启
```

```bash
kernel [--no-mem-option][--type=TYPE]FILE [ARG...]
	# 尝试载入主引导影像文件。其它项将被作为内核的命令行参数而传递给内核。
	# 使用此命令以前，内核所用到的模块应该被重新载入。
	# 参数 --type 用于说明内核的类型，包括 "netbsd", "freebsd", "openbsd", "linux", "biglinux" 和 "multiboot"。
	# 参数 --no-mem-option 用于说明不必自动传递 Linux 的内存参数。
initrd FILE[FILE...]
	# 加载Linux格式的初始化虚拟盘, 并设置必要的参数。

/*从iso启动Kali实例，镜像在/iso/kali/kali-linux-2016.1-amd64.iso*/
find --set-root /iso/kali/kali-linux-2016.1-amd64.iso 
kernel /iso/kali/vmlinuz boot=live config boot=live username=root hostname=kali boot=live username=root hostname=kali findiso=/iso/kali/kali-linux-2016.1-amd64.iso 
initrd /iso/kali/initrd.img
	# "/iso/kali/vmlinuz"：从kali镜像中提取的vmlinuz文件
	# "boot = live ...findiso=/iso/..."：从镜像引导文件中提取的参数
	# "/iso/kali/initrd.img"：从kali镜像中提取的initrd.img文件
	# 若镜像已经解，可以直接加载镜像中已经有的引导，或直接加载引导文件
	
chainloader [--force]FILE
	# 加载扇区链式加载器,注意：在命令行下使用该命令后还需再执行 boot 命令才会真正启动。
chainloader /ntldr
	# 加载ntldr启动文件
chainloader (hd0,0)+1
	# 加载(hd0,0)的第一扇区
chainloader --force /bootmgr
	# 加载bootmgr,忽略启动标识有效性，强制启动

boot -1		(或boot -int18)
	# 根据Bios顺序启动下一设备
```

# grub4dos配置

地址：https://github.com/yehuohan/_bak_winly-grub4dos-rEFInd，具体见里面的readme.txt



---
---这里是分割线---
---


---
# 安装refind
- 官网：http://www.rodsbooks.com/refind/
- 在官网中可以下载到refind，还有各种详细的帮助说明，只是全是英文的。
- 先了解uefi：http://bbs.wuyou.net/forum.php?mod=viewthread&tid=299643&extra=page%3D1
- 可以用bootice安装：http://www.ipauly.com/，直观方便，
- 也可以用命令安装：

```bash
bcdedit /set {bootmgr} path \EFI\refind\refind_x64.efi
	# windows下，efi路径为一个fat32分区的\EFI\refind\refind_x64.efi

efibootmgr -c -l \\EFI\\refind\\refind_x64.efi -L rEFInd
	# linux下，"\\EFI\\refind\\refind_x64.efi"为挂载到/boot下的分区中的efi文件
```


---
# 使用efi shell
 - 记住最简的使用规律：找到efi文件，然后load(加载)
 - efi shell的使用：

```bash
*.efi
    #efi shell是一个命令行环境，有efi文件，直接输入 *.efi 就可以加载启动

fs0:
	# 一般是进入到shell.efi所在设备目录
ls
	# 列出目录和文件
la -a
	# 列出所有目录和文件，包括隐藏的
cd	
	# 改变目录，cd ..向上一级目录
cp
	# 复制
rm
	# 删除
type
	# 显示文件内容
mkdir
	# 创建目录
touch
	# 建立文件
edit
	# 文本编辑器，可以更改文本配置文件，Ctrl+S是保存，Ctrl+Q是退出
hexedit
	# hex编辑
```

---
# refind配置
- /efi/boot/refind_x64.efi：启动rEFInd引导管理
- /efi/tools/shell.efi：启动efi shell环境

地址：https://github.com/yehuohan/_bak_winly-grub4dos-rEFInd/，具体见里面的readme.txt
