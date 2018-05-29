---
title: Arch Linux安装记录
categories:
  - 笔记
tags:
  - linux
  - arch
date: 2017-06-11 23:36:58
---

记录Arch Linux的安装过程。

<!-- more -->

---
# 写在开头

纯命令安装Arch，如果具备以下条件，安装过程会相对顺利：
 - 对linux的基本命令比较熟悉；
 - 有安装其他linux发行版的经验；
 - 了解引导的基本知识；
 - 在虚拟机安装一遍Arch，并记下自己的步骤。

## ArchWiki参考教程

> 注意：以下ArchWiki的教程，有些是中文，可以自己选择（左侧栏里选）语言。中文是根据英文翻译过来，一般会注明最后更新时间，看英文还是中文，自己把握。

 - [Install guide](https://wiki.archlinux.org/index.php/Installation_guide)
 Arch安装全过程，不过具体某一项时，需要查看相应的教程。

 - [Network configuration](https://wiki.archlinux.org/index.php/Network_configuration)
 有线网配置教程。

 - [Wireless network configuration](https://wiki.archlinux.org/index.php/Wireless_network_configuration)
 无线网配置教程。

 - [General recommendations](https://wiki.archlinux.org/index.php/General_recommendations)
 安装完Arch后，对Arch的配置（如安装桌面环境等）教程。

 - [Xorg](https://wiki.archlinux.org/index.php/Xorg)
 Xorg相关教程


---
# Arch启动盘
最简单的方法，就是直接刻录到U盘中，然后用U盘启动就行。
这里我只记下自己的方法：

 - 安装环境
 UEFI启动，硬盘使用MBR分区（没写错，就是MBR，不是GPT）。

 - 多系统：
 已经安装了Windows，且有一个ESP分区了，所在Arch也就直接使用ESP即可。

 - 启动方法：
 我使用 [refind](http://www.rodsbooks.com/refind/) 引导。将Arch.iso解到任一硬盘分区的根目录（移动硬盘也可以），然后，在refind中添加Arch的引导即可。我使用的[refind配置](https://github.com/yehuohan/USBBootFiles/blob/master/EFI/boot/refind.conf)。


---
# 安装Arch

> 这里的“安装Arch”，是指按照此部分教程安装完后，会得到一个只有控制台的Arch Linux系统。同时，此部分开始的的教程，均是基于已经正确进入Arch安装环境的前提下。

## 键盘布局
控制台键盘默认布局为us（一般不用担心键盘布局），使用下列命令更改（[二位字母编码表](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)）：

```bash
loadkeys <layou>
# 更改布局
```

## 查看硬盘、内存基本信息

<span id = "硬盘信息"></span>
 - 查看硬盘分区

```bash
df -h
# 显示磁盘相关信息
blkid
# 查看块设备（包括交换分区）的信息
lsblk
# 列出所有可用块设备信息，包括硬盘，闪存盘，CD-Rom等
lsblk -f
# 列出块设备的文件系统信息
fdisk -l
# 列出设备的分区表情况
# 以上命令，均可查看硬盘情况

free -h
# 查看内存使用情况
```

 - 查看是否以UEFI启动

```bash
ls /sys/firmware/efi/efivars
# 如果提示efivars不存在，则不是UEFI启动。
```

<span id = "网络"></span>
## 网络连接

这里先提供几种网络接入方法：
 - 如是公司或家里的有线网：
 那就很简单了，直接插上网线就行；

 - 如果是Wifi：
 按照无线网配置即可；

 - 如果是校园网（需要登录校园网帐号的那种）：
  - 使用另一台电脑开wifi热点；
  - 使用手机的USB网络共享功能，即相当于将手机当成“网线”，然后手机连接并登录校圆网（推荐这种方法）。

### 查看网卡信息

 - 查看网络连接设置

```bash
ip link
# 一般有线网设备以 "e" (ethernet，以太)开头，无线网设备以 "wl" (wireless)开头
# 如果没有显示无线设备，看下是不是关了（如：有些电脑可以使用Fn+F5打开或关闭无线网）
# 或者在Windows系统连接一下无线网（多系统的话），再重启进入Arch安装环境

lspci
# 查看所有PCI设备，包括了网卡设备

lsusb
# 查看所有USB设备，如果是外接USB网卡，就可以此命令查看
```

 - 启用网卡设备
 不管是有线还是无线，都需要启用网卡后，才能接开始配置。

```bash
ip link set <dev-name> up
# 启动网卡设备，dev-name为有线或无线网卡设备名称
# 启动后，用 ip link 查看时，会有 "UP" 的标记

ip link set <dev-name> down
# 停用网卡设备，dev-name为有线或无线网卡设备名称，重启即先down再up
```

### 有线网配置

有线网配置只需要获取的IP就行；如果是静态IP，则参考[有线网配置教程](https://wiki.archlinux.org/index.php/Network_configuration)。

```bash
dhcpcd <dev-name>
# 为dev-name自动获取IP地址，dev-name为有线网卡设备名称
# dhcp是动态主机配置协义，负责管理和分配IP地址等

kill <pid>
# 结束进程，pid为进程的PID
# 使用dhcpcd后，会返加一个pid，需要重新获取IP地址，则先结速dhcpcd即可

ping -c 3 www.google.com
# 检测网络是否正常
```

### 无线网配置

无线网配置相对复杂一点，情况太多，这里只说下我的配置过程，具体情况参照[有线网配置教程](https://wiki.archlinux.org/index.php/Network_configuration)。

```bash
iw dev
# 查看无线设备
iw dev <dev-name> link
# 查看无线网 dev-name 的加接状态
iw dev <dev-name> scan
# 扫描wifi热点
wpa_passphrase <your_SSID> <your_KEY> > /ws.conf
# 生成连接配置，并保存在ws.conf，SSID和KEY为热点名称和密码
wpa_supplicant -B -i wlp13s1 -c /ws.conf
# 使用连接配置来连接无线网

dhcpcd <dev-name>
# 为dev-name自动获取IP地址，dev-name为无线网卡设备名称
# 使用kill可结束dhcpcd
ping -c 3 www.google.com
# 检测网络是否正常

wifi-menu
# 自动配置wifi（使用终端UI），手动配置没成功时，可以尝试下
```

## 时间与时区

```bash
timedatectl
# 查询和更改系统时钟设置
timedatectl status
# 查看当前Time状态
timedatectl set-ntp true
# 远程NTP服务器时间同步
```

## 硬盘分区

先确定好分区情况，我的分区设置如下：

```
/dev/sda1 : ESP分区，fat32格式，refind引导所在分区
/dev/sdb1 : / 分区，ext4格式
/dev/sdb2 : swap分区，如果是多Linux系统，则swap分区共用
```

 - 分区
 先查看[硬盘相关信息](#硬盘信息)，使后使用相应软件分区。

  - cfdisk
  硬盘分区工具，支持GPT和MBR，可以直接创建EFI分区，推荐此工具，拥有简单的UI，相对比较直观，分区不易出错。
```bash
cfdisk /dev/sdb
# 对sdb硬盘进行分区操作
```
  - fidsk, cfdisk, sfdisk, parted : 均支持GPT和MBR
  - gdisk, cgdisk, sgdisk : 只支持GPT

 - 格式化分区

```bash
mkfs.ext4 /dev/sdb1
# mkfs即make file system，创建文件系统，将sdb1格式化成ext4，这里sdb1作为'/'目录

mkswap /dev/sdb2
# 格式化Swap分区

swapon /dev/sdb2
# 激活Swap分区

mkfs.fat -F32 /dev/sda1
# 格式化成Fat32，作为ESP分区；mkfs.vfat与mkfs.fat等价
# 如果是多系统，已经有ESP分区，则不需要格式化，直接使用即可
```

 - 挂载分区

```bash
mount /dev/sdb1 /mnt
mkdir /mnt/boot
mkdir /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
# 将sdb1挂载到/mnt，这时，/mnt就相当于新系统的根目录，ESP分区也挂载到新系统的boot/efi目录下
# 如果还其分区，也挂载到相应位置即可
```

## 开始安装系统

此部分需要联网下载，大概200~300Mb的样子。

```bash
vim /etc/pacman.d/mirrorlist
# 更改镜像源，将其中China的放在文件开头，其它的可以删了（有一个HongKong的可以留着）

pacstrap -i /mnt base base-devel
# 安装ArchLinux基本系统
```

## 生成分区表

```bash
genfstab -U -p /mnt >> /mnt/etc/fstab
# 生成fstab文件，保存系统分区表
```
到了这，系统已经基本安装完了，接下来就要配置系统，至少现在Arch还不知道如何启动。


---
# 配置Arch

现在开始配置安装完的Arch Linux。

## 切换root用户

```bash
arch-chroot /mnt /bin/bash
# 转到新系统的root用户，使用bash，即此后的命令都是对以/mnt作为根目录的系统操作

alias vim=vi
# 新系统中暂时没有vim，添加一个吧
alias ll='ls -l'
# 查看目录，控制台下方便点
```

## 设置时区

```bash
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 设置时区，Shanghai即为东八时区（北京时间）

hwlock --systohc --utc
# 设置成UTC时间标准，即本地时间 = Bios时间 + 时区数(北京为+0800)
hwlock --systohc --localtime
# 设置使用本地时间标准，即本地时间 = Bios时间
```

## 本地化

```bash
vim /etc/locale.gen
# 设置本地化类型为UTF-8编码，添加：
zh_CN.UTF-8 UTF-8
en_US.UTF-8 UTF-8

locale-gen
# 生成locale信息
echo LANG=en_US.UTF-8 > /etc/locale.conf
# 添加本地化文件locale.conf，用英文，使用zh_CN会导致tty中文乱码
```

## 主机名

```bash
echo myhostname > /etc/hostname
# 设置主机名称，myhostname会出现在终端的提示符中
vim /etc/hosts
# 添加对应的信息，如下：

# /etc/hostname: static lookup table for host names
#<ip-address>   <hostname.domain.org>   <hostname>
127.0.0.1       localhost.localdomain   myhostname
::1             localhost.localdomain   myhostname
```

## 网络配置

用[前面](#网络)的方法即可。
不过有趣的是，新安装的Arch系统里没有iw等无线网式具，需要先安装

```bash
pacman -S iw wpa_supplicant dialog
# 安装式具
```
但是，安装软件就需要先联网，所以，如果只联网。。。好像循环了。。。应该可以从Arch安装环境中拷吧（我没试过）
好了，我反正用手机USB共享的网络，既然有网了，当然得学会pacman的的基本用法：

```bash
pacman -S <packge-name>     # 安装软件(install)
pacman -U <pkg-file>        # 安装本地包(unpack)，其扩展名为 *.tar.gz, *.tar.xz
pacman -U <http://pkg-file> # 安装远程包

pacman -Sy                  # 同步(synchronize)软件数据库，先比较是否为最新的，是的话不再下载数据库
pacman -Syy                 # 强制同步软件数据库，无论是否为最新的，都重新下载数据库
                            # 将数据库理解成一个软件列表，从中可以知道有哪些软件
pacman -Su                  # 更新(update)整个系统，即比对数据库，有更新版本的软件，则更新
pacman -Syu                 # 先同步数据库，然后再更新系统
pacman -Syyu                # 先强制同步数据库，然后再更新系统
pacman -Sy <packge-name>    # 先同步数据库，然后安装软件
pacman -Ss <keywords>       # 在数据库和已安装软件包中查询(search)软件
pacman -Si <keywords>       # 显示软件包信息(information)
pacman -Sw <keywords>       # 下载(download)软件包，但不安装
pacman -Sc                  # 清理(clean)未安装的软件包缓存
                            # 包文件位于 /var/cache/pacman/pkg（有软件包缓存时，下次重新安装则不用再下载）
pacman -Scc                 # 清理所有缓存软件包

pacman -Qs <packge-name>    # 查询已安装的软件包
pacman -Qi <packge-name>    # 查询已安装软件包的信息

pacman -R <packge-name>     # 删除(remove)单个软件包，保留该软件包全部的依赖
pacman -Rs <packge-name>    # 删除(remove)单个软件包，删除该软件包的依赖（如果该依赖没有与其它软件存在依赖关系）
pacman -Rsc <packge-name>   # 删除(remove)单个软件包，删除该软件包的依赖，和所以依赖该软件包的程序
```

## Root密码

```bash
passwd root
# 设置root密码
```

## Initramfs

```bash
mkinitcpio -p linux
# 初始化Initramfs(init ram fs)
```

## 安装引导程序

UEFI引导可以使用[grub](https://wiki.archlinux.org/index.php/GRUB)、[refind](https://wiki.archlinux.org/index.php/GRUB)等。

 - 使用grub

```bash
pacman -S grub efibootmgr
# 安装引导程序grub和创建efi启动项程序efibootmgr

grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grubname
# 安装efi程序到/boot/efi/grub，grubname为存放grub.efi文件的目录名称

grub-mkconfig -o /boot/grub/grub.cfg
# 生成引导配置文件grub.cfg

efibootmgr
# 显示efi启动项
```

 - 使用refind
refind也可以使用pacman安装，不过最好到[官方网站](https://wiki.archlinux.org/index.php/GRUB)下载最新版，并按照官方教程复制所需要的文件到指定目录。然后用efibootmgr添加启动项。

```bash
efibootmgr -c -l /boot/efi/refind/refind_x64.efi -L 'refind boot manager'
# 创建refind启动（需要自己添加refind文件）
```

 - 生成引导初始化文件

若是不小心将vmlinuz等文件给删了，可以使用下列命令重新生成：

```bash
pacman -S linux
# 安装linux内核，也可以使用其它的，如linux-lts, linux-zen等
mkinitcpio -p linux
```


## 创建用户

```bash
pacman -S zsh
# 安装zsh，新用户使用zsh
cp /etc/sudoers /etc/sudoers_bak
vim /etc/sudoers
# 修改sudoers文件，启用wheel组(去掉'#%wheel ALL=(ALL) ALL'前的#即可)

useradd -m -G wheel -s /bin/zsh username
# 创建用户，同时创建与username同名的用户组，所属的附加组为wheel组，使用zsh
useradd -m -g usergroup -G wheel -s /bin/zsh username
# 创建用户，属于usergroup组（需要先创建用户组），所属的附加组为wheel组，使用zsh
passwd username
# 设定密码
su root
chsh -s /bin/zsh
# root用户也可使用zsh
```

## 重启

```bash
exit
# 退出chroot
cd /
umount -R /mnt
reboot
```

Arch系统的安装就结束了，接下来就是个性化的配置了。

---
# 基本软件安装

## shell和vim

```bash
sudo pacman -S vim git
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## yaourt

```bash
sudo vim /etc/pacman.conf
# 添加：

[archlinuxcn]
#The Chinese Arch Linux communities packages.
SigLevel = Optional TrustAll
Server   = http://repo.archlinuxcn.org/$arch

sudo pacman -Sy
sudo pacman -S yaourt
# 安装yaourt，yaourt命令类似于pacman
suso pacman -S zsh-completions
# yaourt自动补全
```


---
# 安装桌面环镜

从头到尾安装桌面环境，包括：
 - 显卡驱动(Display Driver)
 - 显示服务(Display Server)
 - 显示管理器(Display Manager)
 - 桌面环境(Desktop Environment)
 - 窗口管理器(Window Manager)


## 显卡驱动

```bash
lspci -v | grep VGA
# 查看显示型号

sudo pacman -S <显卡驱动>
# 根据自己的显卡，查找相应的显卡驱，开源驱动（也有闭源的，推荐使用开源的）如下：
# 通用   : xf86-video-vesa
# AMD    : xf86-video-amdgpu
# ATI    : xf86-video-ait
# Intel  : xf86-video-intel
# Nvidia : xf86-video-nouveau
# VMWare : xf86-video-vmware
```


## 显示服务

X窗口管理系统（X11）是一种显示协议提供的GUI环境的基本框架，如屏幕绘制、鼠标键盘交互等；而Xorg是X11的开源实现。

 - 安装Xorg-server

```bash
sudo pacman -S xorg-server
# 安装xorg服务
sudo pacman -S xorg-server-utils
# 鼠标加速
sudo pacman -S xf86-input-synaptics
sudo pacman -S xf86-input-libinput
# 触摸板,synaptics和libinput选一个（推荐libinput）
sudo pacman -S xorg-xinput
# 实时配置触板的命令行工具
```

现在安装好了X11，启动X11可以使用登录管理器（也即 显示管理器），也可以使用xorg-init（即 通过startx命令启动X11）。
推荐用登录管理器，xorg-init也可以同时安装。

 - 安装xorg-init

```bash
sudo pacman -S xorg-xinit xorg-twm xorg-xclock xterm
# 安装xorg-init和twm窗器管理器
cp /etc/X11/xinit/xintrc ~/.xinitrc
# 桌面环境配置文件
startx
# 测试xorg
```

## 显示管理器

显示管理器即是登录管理器，登录时的界面，常用的显示管理器有sddm,LightDM等，这里安装sddm。

```bash
sudo pacman -S sddm
# 安装sddm
sddm --example-config > /etc/sddm.conf
# (使用root用户)创建sddm配置文件，初始创建的为默认配置
# sddm默认使用tty1开启形会话，可以配置成tty7，但tty1还是没法进行命令交互
# 不过tty2~tty6还是可以作为文本控制台用

sudo systemctl enable sddm.service
# 开机启动sddm
ls -l /etc/systemd/system/display-manager.service
# 查看当前使用的是那个登录管理器
pacman -S gst-libav phonon-qt5-gstreamer gst-plugins-good
git clone https://github.com/3ximus/aerial-sddm-theme
sudo mv aerial-sddm-theme /usr/share/sddm/themes
# 一个不错的sddm主题，可能需要安装qt5-multimedia和qt5-svg

```


## 桌面环境

桌面环境最好安装通用的，常用的如KDE, xfce等，安装示例：

```bash
sudo vim /etc/locale.conf
# 修改： LANG=zh_CN.UTF-8
# 修改本地化为中文
sudo pacman -S xfce4 xfce4-goodies
# 安装xfce桌面，goodies为一些基本工具软件，同时默认安装xfwm4窗口管理器
exec startxfce4
# 修改xinitrc，通过startx启动X11
# 如果使用显示管理器，如sddm，则可以选择要使用的桌面环境
```


## 窗口管理器

窗口管理器负责绘制窗口的边框和背景等，处理窗口的移动、最大/小化等行为。桌面环境是窗口管理器的超集，使用窗口管理器和其它一些常用软件组成一个完整的桌面工作环境。
所以说，只安装窗口管理器，而不安装桌面环境也是可以的。（还是推荐一个桌面环境，这样好多软件，如文件管理器等，就不用自己挨个找了）
窗口管理器可以用桌面环境默认自带的，也可以自己选择，如平铺式有i3, awesome等。

### 安装i3

```bash
sudo pacman -S i3 dmenu
# 安装i3窗口管理器，dmenu为i3程充启动器
cp /etc/i3/config ~/.i3/config
# 创建i3配置文件，.i3没有则自己mkdir
# 如果使用xorg-init，则添加 "exec i3" 到.xinitrc，通过startx则可以启动ie
```

### 安装awesome

```bash
sudo pacman -S awesome
mkdir -p ~/.config/awesome/
cp /etc/xdg/awesome/rc.lua ~/.config/awesome/
# 安装awesome，并创建配置文件rc.lua
# 如果使用xorg-init，则添加 "exec awesome" 到.xinitrc，通过startx则可以启动ie
```

---

# 我的设置 Of ArchLinux
现在才是像其它Linux发行版安装完后，开始进行配置了。

## Font

```bash
sudo pacman -S ttf-dejavu
# 英文等宽字体
sudo pacman -S wqy-microhei
# 中文字体，包括等宽中文，用于终端和i3窗口管理器
yaourt -S ttf-dejavu-sans-mono-powerline-git
# 打补丁的dejavu字体，包含powerline图标字体

sudo pacman -S noto-fonts noto-fonts-cjk
# (可选)Google Noto字体
sudo pacman -S adobe-source-han-sans-cn-fonts
# (可选)安装思源体简体中文部体，中文效果比文泉好些
sudo pacman -S ttf-ubuntu-font-family
# (可选)ubuntu上的字体
yaourt -S ttf-ms-win10-zh_cn
# (可选)win10字体
yaourt -S fontconfig-infinality-ultimate
# 字体渲染优化

# 手动安装consolas安体
cd /usr/share/fonts
mkdir consolas
# copy consolas-font to /usr/share/fonts/consolas
cd consolas
sudo chmod 664 *.ttf
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv
```
附：[consolas字体](https://github.com/yehuohan/dotconfigs/tree/master/font)

## 对调Esc和CapsLock
（方便Vim使用）

 - Console环境

```bash
cd /usr/share/kbd/keymaps/i386/qwerty/
cp us.map.gz custom.map.gz
# 修改custom中的Esc和CapsLock键位映射
vim /etc/vconsole.conf
# 添加以下内容可以变tty下的键盘布局：
KEYMAP=custom
```

 - X11环境

```bash
vim .Xmodmap
# 添加以下内容：
clear Lock
keysym Caps_Lock = Escape
keysym Escape = Caps_Lock
add Lock = Caps_Lock

vim .zprofile
# zsh用.zprofile，bash用.xprofile
# 添加以下内容：
add xmodmap ./.Xmodmap
```

## 输入法

```bash
sudo pacman -S fcitx-im
# 安装fcitx集成包，提供对Gtk+/Qt的支持，包括gtk2/3和qt4/5
sudo pacman -S fcitx-table-extra
# 添加对五笔的支持
sudo pacman -S fcitx-configtool
# fcitx图形界面配置程序
# 配置fcitx字体为中文字体wqy-microhei，不然乱码

# 配置对X11环境支持，添加以下内容：
# 使用登录管理器(如sddm)启动X11，则编辑.xprofile（zsh则为.zprofile）
# 使用startx启动X11，则编辑.xinitrc
vim ~/.xprofile
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

## 触控板

 - [参数配置解释](https://wiki.archlinux.org/index.php/Touchpad_Synaptics)
 - [手势管理](https://github.com/bulletmark/libinput-gestures)

```bash
sudo pacman -S xf86-input-libinput
cp /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/30-touchpad.conf
# 配置触控板，/usr/share中的为默认配置，/etc/中的用户自定义配置

sudo vim /etc/X11/xorg.conf.d/30-touchpad.conf
# 触控板配置内容如下：
Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"
        Option "Tapping" "on"
        Option "TapButton1" "1"
        Option "TapButton2" "3"
        Option "TapButton3" "2"
        Option "VertEdgeScroll" "on"
        Option "VertTwoFingerScroll" "on"
        Option "HorizEdgeScroll" "on"
        Option "HorizTwoFingerScroll" "on"
        Option "NaturalScrolling" "on"
EndSection
```
## 独显Nvidia
 [开源独显Nouveau](https://wiki.archlinux.org/index.php/Nouveau)
 [Nouveau支持查询](https://nouveau.freedesktop.org/wiki/CodeNames/)
 [Nouveau支持功能查询](https://nouveau.freedesktop.org/wiki/FeatureMatrix/)
 [闭原独显Nvidia](https://wiki.archlinux.org/index.php/NVIDIA)
 [Bumblebee](https://wiki.archlinux.org/index.php/Bumblebee)

 这里简单写下Bumblebee的安装流程：

```bash
sudo pacman -S bumblebee mesa xf86-video-intel nvidia
# bumblebee        : 提供守护进程以及程序的主要安装包。
# mesa             : 开源的OpenGL标准实现。
# xf86-video-intel : Intel 驱动。
# nvidia           : NVIDIA 驱动，注意，如果使用nvidia-lts版，内核也要使用linux-lts版。
# 最好卸了Nouveau驱动
sudo gpasswd -a <user> bumblebee
# 安装,并添加用户到bumblebee用户组
systemctl enable bumblebeed.service
# 启用bumblebee，然后重启继续
# bumblebee的作用是禁用nvidia独立显卡,
# 需要使用独显时，使用”optirun 程序名“开启nvidia来运行需要加速的程序。

optirun glxspheres64
optirun glxspheres32
# 运行glxspheres64测试程序，optirun用于使用独显运行程序
# 测试(x64或x32)，会打开一个动画窗口
sudo pacman -S bbswitch
# Bumblebee会自动检测bbswitch，可以自动关闭N卡
lspci | grep VGA
# 查看独显示状态，(rev ff)表示关闭，否则为打开状态
# 运行glxspheres64时，则不为(rev ff)

# 附：安装cuda等，一条命令就搞定，很是方便
sudo pacman -S cuda cudnn
# 安装CUDA, CUDNN，安装在/opt/cuda，里面有samples可以运行
sudo pacman -S python-tensorflow-cuda
# 安装tensorflow
# 注意：同样会安装numpy等包，如果已经用pip安装，需要先删了，不然会提示文件冲突
```

## i3wm配置
i3的配置比较容易，找一份详细的配置和教程，仔细看一看就可以配置自己所想要的。
[i3wm ArchWiki](https://wiki.archlinux.org/index.php/I3)
[我的i3wm置文件](https://github.com/yehuohan/dotconfigs/tree/master/cf-i3)
[awesome-font图标字体，直接复制使用](http://fontawesome.io/cheatsheet/)

```bash
yaourt -S i3-gaps-git
# 换用i3-gaps，可以设置透明i3bar
sudo pacman -S i3lock
# 锁屏
pacman -S rofi
# 可用于窗口切换和程序启动，可代替dmenu
sudo pacman -S feh
# 壁纸
sudo pacman -S compton
# 透明效果设置
sudo pacman -S conky
yaourt -S ttf-font-awesome
# 用conky代替i3status，并安装图标字体
sudo pacman -S scrot
# 截图软件
sudo pacman -S alsa-utils volumeicon pulseaudio ffmpeg
# 音量管理，浏览器在线播放也需要
sudo pacman -S networkmanager network-manager-applet nm-connection-editor
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
# 网络管理及托盘图标
sudo pacman -S xfce4-power-manager
sudo pacman -S mate-power-manager
# 电源理软件，包括对屏幕亮度调节，xfce4或mate的任选一个
sudo pacman -S xfce4-terminal
# xfce4的终端
```

## 其它设置

 - mtp

```bash
sudo pacman -S gvfs-mtp
# 安装mtp，支持移动设备挂载；
# 安装后xfce-thunar可以自动识别windows-ntfs硬盘和手机u盘等设备。
```

 - ntf-3g

```bash
sudo pacman -S ntfs-3g
# Linux内核目前只支持对微软NTFS文件系统的读取；
# NTFS-3G是微软NTFS文件系统的一个开源实现，同时支持读和写；
# NTFS-3G 开发者使用 FUSE 文件系统来辅助开发，同时对可移植性有益。
```

---

# 常见问题

## 关机出现“watchdog0: watchdog did not stop!”

[相同问题：watchdog did not stop on reboot](https://bbs.archlinux.org/viewtopic.php?pid=1195597#p1195597)
[对systemd关机过程的说明：cgroup : option or name mismatch, new: 0x0"", old: 0x4 "systemd"](https://bbs.archlinux.org/viewtopic.php?pid=1372562#p1372562)

根据以上查到的资料，这是正常的。

## Inter i5 8250U + Nvidia MX150的关机问题

我自己电脑遇到的关机问题，感觉像MX150使用nouveau驱动的问题（201804时遇到的，可能后来的更新会修复错误），主要表现如下：
 - 未禁用nouveau前，每次进xorg+i3wm，关机都会出现问题，关机时会卡在一个地方，出现不同的错误提示，遇到过的有以下几个(具体的没记下，只记得一些大概的文字)：
    - `watchdog: BUG: soft lockup - CPU#1 stuck for 22s`
    - `[drm:drm_atomic_helper_wait_for_dependencies [drm_kms_helper]] *ERROR* [CRTC:26:pipe A] flip_done timed out`
 - 禁用nouveau，安装 nvidia+bumblebee，xorg使用intel集显驱动，关机正常。
