
---
title: arch-linux安装记录
categories:
  - 杂记
date: 2017-06-11 23:36:58
tags:
 - linux
 - arch
---

简单记录arch-linux的安装过程。

<!-- more -->



---
# ArchLinux 
 * Some command used of installing ArchLinux
 * refs: 
```
[archwiki]:
    https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)
[arch新手指南]:
    https://wiki.archlinux.org/index.php?title=ArchLinux_%E6%96%B0%E6%89%8B%E6%8C%87%E5%8D%97_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)&oldid=36497
```

---

---
# 安装系统命令

## 查看信息
 * df -h
 查看磁盘使用情况

 * free -h
 查看内存使用情况

## 网络检测

 * 
[网络设置](https://wiki.archlinux.org/index.php/Network_configuration_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)
 
### 基本测试
 * ping <url> -c 3
 测试与目标主机的连通性，检测网络是否正常

 * ip link
 查看网卡设备，e开头的为有线网卡，w开头的是无线网卡

 * systemctl 
 系统服务管理命令

 * systemctl --type=service | grep dhcp
 查找含'dhcp'的服务，dhcp是动态主机配置协义，负责管理和分配IP地址等

 * systemctl stop dhcpcd@ens33.service
 关闭有线网卡ens33的dhcp服务 

 * dhcpcd ens33
 重启有线网卡ens33的dhcp服务获取ip地址

 * iw, wpa_supplicant, netctl
 无线网配置相当命令


## 设置键盘和时间
 * loadkeys us
 设置为美式键盘

 * timedatectl
 查询和更改系统时钟设置
 * timedatectl status
 查看当前Time状态 
 * timedatectl set-ntp true
 远程NTP服务器时间同步


## 硬盘分区与挂载
 * lsblk
 列出所有可用块设备信息，包括硬盘，闪存盘，CD-Rom等

 * lsblk -f
 列出块设备的文件系统信息

 * fdisk -l
 列出设备的分区表情况

 * cfdisk
 硬盘分区工具，支持GPT和MBR，可以直接创建EFI分区，推荐此工具，拥有简单的UI，相对比较直观，分区不易出错。

 * fidsk, cfdisk, sfdisk, parted均支持GPT和MBR
 * gdisk, cgdisk, sgdisk只支持GPT

 * mkfs.ext4 /dev/sda1
 mkfs即make file system，创建文件系统，将sda1格式化成ext4，这里sda1作为'/'目录

 * mkswap /dev/sda2
 格式化Swap分区

 * swapon /dev/sda2
 激活Swap分区

 * mkfs.fat -F32 /dev/sda3
 格式化成Fat32，作为ESP分区；mkfs.vfat与mkfs.fat等价

 * mount /dev/sda1 /mnt
 * mkdir /mnt/boot
 * mkdir /mnt/boot/efi
 * mount /dev/sda3 /mnt/boot/efi
 将sda1挂载到/mnt，这时，/mnt就相当于新系统的根目录，相应的分区也要挂载到新系统的boot/efi等目录下

## 安装系统 
 * vim /etc/pacman.d/mirrorlist
更改镜像源，将其中China的放在文件开头，国内用China的镜像源没问题吧 

 * pacman -Ssy 
更新源 

 * pacstrap -i /mnt base base-devel
安装ArchLinux基本系统


## 配置系统
### 分区表
 * genfstab -U -p /mnt >> /mnt/etc/fstab
 生成fstab文件，保存系统分区表

### 切换root用户
 * arch-chroot /mnt /bin/bash
 转到新系统的root用户，使用bash，即之后的命令都是对以/mnt作为根目录的系统操作
 (在此之后的命令，都是以/mnt作为根目录的系统中操作)
 此后，没有vim则用vi，或'alias vim=vi'

### 时区
 * ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
 设置时区，Shanghai即为东八时区（北京时间）

 * hwlock --systohc --utc
 设置成UTC时间标准，即本地时间 = Bios时间 + 时区数(北京为+0800)

 * hwlock --systohc --localtime
 设置使用本地时间标准，即本地时间 = Bios时间

### 本地化
 * vim /etc/locale.gen
 设置本地化类型为UTF-8编码
 添加：

```
zh_CN.UTF-8 UTF-8
en_US.UTF-8 UTF-8
```

 * locale-gen
 生成locale信息

 * echo LANG=en_US.UTF-8 >> /etc/locale.conf
 添加本地化文件locale.conf，用英文，使用zh_CN会导致tty中文乱码

### 主机名
 * echo myhostname >> /etc/hostname
 设置主机名称
 * vim /etc/hosts
 添加对应的信息：

```
# 
# /etc/hostname: static lookup table for host names
#

#<ip-address>   <hostname.domain.org>   <hostname>
127.0.0.1       localhost.localdomain   myhostname
::1             localhost.localdomain   myhostname
```

### 网络配置
 * [网络没置](https://wiki.archlinux.org/index.php/Network_configuration_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)
 * dhcpcd ens33
 重启有线网卡ens33的dhcp服务获取ip地址
 * systemctl enable ens33.service
 开机自动启动服务

#### 有线网配置
 * lspci -v
 查看'Ethernet controller'的'Kernel driver'，如e1000
 * demsg | grep e1000
 查看驱动是否加载成功
 dmesg显示系统的启动信息，可以在里面查找与硬件和模块初始化相关的内容

#### 无线网配置
 * pacman -S iw wpa_supplicant dialog
 无线网卡三个配置软件包


### Initramfs
 * mkinitcpio -o linux
 初始化Initramfs(init ram fs)

### Root密码
 * passwd root
 设置root密码

### 安装引导程序
 我的方案，使用grub引导arch linux，使用refind管理efi启动。
 [grub install](https://wiki.archlinux.org/index.php/GRUB_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
 [refind install](http://www.rodsbooks.com/refind/)
 * pacman -S grub efibootmgr
 安装引导程序grub和创建efi启动项程序efibootmgr
 * grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grubname
 安装efi程序到/boot/efi/grub，efi的启动项名称为grubname
 * grub-mkconfig -o /boot/grub/grub.cfg
 生成引导配置文件grub.cfg
 * efibootmgr
 显示efi启动项
 * efibootmgr -c -l /boot/efi/refind/refind_x64.efi -L 'refind boot manager'
 创建refind启动，使用refind管理efi启动项（这个可以后续在弄，需要自己添加refind文件）

## 创建用户
 * cp /etc/sudoers /etc/sudoers_bak
 * vim /etc/sudoers
 修改sudoers文件，启用wheel(去掉'#%wheel ALL=(ALL) ALL'前的#即可)
 * useradd -m -g usergroup -G wheel -s /bin/bash username
 创建用户，属于usergroup组，所属的附加组为wheel组，使用zsh
 * passwd username 
 设定密码

### 重启
 * exit
 退出chroot
 * cd /
 * umount -R /mnt
 * reboot


 
 
---
 
---
# 安装完后的系统配置
## 配置zsh
 * sudo pacman -S zsh vim git
 * curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh
 * chsh -s /bin/zsh
 安装zsh

## 安装yaourt
 * sudo vim /etc/pacman.conf
 添加：
```
[archlinuxcn]
#The Chinese Arch Linux communities packages.
SigLevel = Optional TrustAll
Server   = http://repo.archlinuxcn.org/$arch
```
 * sudo pacman -Syu yaourt
 安装yaourt，yaourt命令类似于pacman

## 字体
 * cp Courier\*.ttf /usr/share/fonts/ttf/
 * cp msyh*.ttc /usr/share/fonts/msyh/   
 复制courier和微软雅黑字体
 linux下使用Courier 10 Pitch字体更好，Courier New适合在Windows下
```
# 复制后需要建立字体缓存
cd <font-dir>
# <font-dir>为courier或雅黑字体所在的目录
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv
```
 * sudo pacman -S adobe-source-han-sans-cn-fonts
 安装思源体简体中文部体，中文效果比文泉好些
 * sudo pacman -S wqy-zenhei
 安装文泉驿正黑，中文字体

## 输入法
 * sudo pacman -S fcitx-im
 安装fcitx集成包，提供对Gtk+/Qt的支持
 * sudo pacman -S fcitx-table-extra
 添加对五笔的支持
 * sudo pacman -S fcitx-configtool
 fcitx图形界面配置程序

## 安装fbterm
Fbterm是tty的替代品，不需要xorg也能使用的终端模拟器。
 * sudo pacman -S fbterm
 安装fbterm
 * sudo gpasswd -a username video
 gpasswd是用管理组命令，-a为添加用户到video组。
 非root用户需要加入video组才能运行fbterm。
 * sudo chmod u+s /usr/bin/fbterm
 设置非root用可以使用键盘快捷方式
 * ~/.fbterm
 配置文件，第一次运行fbterm自动生成
 * sudo pacman -S fcitx-fbterm
 安装fbterm下的fcitx输入法，配置‘input-methon=fcitx-fbterm’

## 图形界面
### 显卡驱动(Display Driver)
 * lspci -v | grep VGA
 查看显示型号 
 * sudo pacman -S <显卡驱动>
 根据自己的显卡，查找相应的显卡驱，例如：
 通用   :   xf86-video-vesa
 AMD    :   xf86-video-amdgpu
 ATI    :   xf86-video-ait
 Intel  :   xf86-video-intel
 Nvidia :   xf86-video-nouveau
 VMWare :   xf86-video-vmware

### 显示服务(Display Server)
X窗口管理系统(X11)是一种显示协议提供的GUI环境的基本框架，如屏幕绘制、鼠标键盘交互等；而Xorg是X11的开源实现。
 * sudo pacman -S xorg-xinit xorg-server xterm
 or 'sudo pacman -S xorg-xinit xorg-server xorg-twm xorg-xclock xterm'
 安装xorg服务
 * sudo pacman -S xorg-server-utils
 鼠标加速
 * sudo pacman -S xf86-input-synaptics
 触摸板
 * cp /etc/X11/xinit/xintrc ~/.xinitrc
 桌面环境配置文件
 * startx 
 测试xorg
 * 启动时自动启用X(可以理解为自动执行 startx)
```
# vim ~/.bash_profile for bash user
# or 
# vim ~/.zprofile for zsh user
# add
[ -z "$DISPLAY" -a "$(fgconsole)" -eq 1 ] && exec startx
```

### 桌面环境(Desktop Environment)
桌面环境最好安装通用的，常用DE如KDE, xfce等。
 * 修改本地化为中文
```
sudo vim /etc/locale.conf
# 修改： LANG=zh_CN.UTF-8
```
 * sudo pacman -S xfce4 xfce4-goodies
 安装xfce桌面，goodies为一些基本工具软件


### 窗口管理器(Window Manager)
窗口管理器负责绘制窗口的边框和背景等，处理窗口的移动、最大/小化等行为。
桌面环境是窗口管理器的超集，使用窗口管理器和其化一此常用软件组成一个完整的桌面工作环境。
所以说，只安装窗口管理器而不安装桌面环境也是可以的。
窗口管理器可以用桌面环境默认自带的，也可以自己选择，如平铺式WM有i3, awexome等。
 * sudo pacman -S xfwm4
 其实，安装xfce4时会默认安装xfwm4窗口管理器
```
# 修改xinitrc
# 通过startx启动，将配置改成：
exec xfwm4 & exec startxfce4
```

 * sudo pacman -S i3 dmenu
 安装i3窗口管理器，dmenu为i3程充启动器
 * cp /etc/i3/config ~/.i3/config
 创建i3配置文件，.i3没有则自己mkdir
 * exec i3
 添加到.xinitrc
 i3配置简单易上手

 * sudo pacman -S awesome
 * mkdir -p ~/.config/awesome/
 * cp /etc/xdg/awesome/rc.lua ~/.config/awesome/
 安装awesome，并创建配置文件rc.lua
 * exec awesome
 添加到.xinitrc
 awesome配置相对复杂点

### 显示管理器(Display Manager)
显示管理器即是登录管理器，登录时的界面。
常用的显示管理器有sddm,LightDM等
 * sudo pacman -S sddm
 安装sddm
 * sddm --example-config > /etc/sddm.conf
 (使用root用户)创建sddm配置文件，初始创建的为默认配置
 * sudo systemctl enable sddm.service
 开机启动sddm
 * ls -l /etc/systemd/system/display-manager.service
 查看当前使用的是那个登录管理器

 * vim ~/.xprofile
```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```


## vmware中安装vmtool
 * sudo pacman -S open-vm-tools
 * sudo systemctl enable vmware-vmblock-fuse








