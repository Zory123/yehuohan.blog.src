---
title: Linux自动挂载权限问题
categories:
  - 杂记
mathjax: false
tags:
  - linux
date: 2017-09-28 19:56:50
---

查到的关于Linux自动挂载设备时的权限问题的资料。
（顺便一说ArchWiki是个好东西，[fstab](https://wiki.archlinux.org/index.php/Fstab)写行特详细）

<!-- more -->

## 基本介绍
 - /ect/fstab是系统启动时设备的挂载参数。
 - /etc/mtab是当前系统中已经挂载的设备信息，是一个动态文件，会随着mount和umount的执行而发生改变。

## fstab
fstab挂载的格式如下：

```
<file system>	<dir>	<type>	<options>	<dump>	<pass>
```
 - file system : 可以是/dev/sdax，可以是UUID=xxxx，可以是LABEL=CDEF
 - dir : 挂载点，如/media/EApps
 - type : 挂载设备的类型，linux下ext4等，windows下ntfs等
 - option: 挂载选项，常用参数如下表所示

|             |                                          |
| :---:       | :---:                                    |
| auto        | 自动挂载，可以使用mount -a挂载           |
| noauto      | 只能使用mount命令挂载                    |
| rw/ro       | 设置权限，rw为读写，ro为只读             |
| exec/noexec | 是否具有执行权限                         |
| suid/nosuid | 是否允许进行uid和gid设置                 |
| dev/nodev   | 是否挂载特殊设备                         |
| user        | 允许指定任意用户挂载                     |
| users       | 允许users组中用户挂载                    |
| nouser      | 禁止指定普通用户挂载（只有root可以挂载） |
| owner       | 允许设备所有者挂载                       |
| sync        | I/O同步进行                              |
| async       | I/O异步进行                              |
| defaults    | 使用文件系统的默认参数                   |

 - dump: 是否备份文件系统

|       |            |
| :---: | :---:      |
| 0     | 不备份     |
| 1     | 每天备份   |
| 2     | 不定期备份 |

 - pass: 开机时文件系统的检查顺序，0-不检查，/分区

|       |                                            |
| :---: | :---                                       |
| 0     | 不检查                                     |
| 1     | 根分区                                     |
| 2     | 其它分分，按顺序检查，数字越小，优先级越高 |

## 实例

mtab的格式与fstab的格式是一样，设备的参数是否达到的期望的效果，打开mtab一看就知道，什么参数少，比对着mtab和fstab添加就行。
一个自动挂载windows下分区的实例如下：具有rwx权限，支持中文编码
```
UUID=18D39914A9D3   /media/EApps   ntfs  defaults,user,rw,exec,iocharset=utf8,umask=000,nls=utf8   0   0
```

几点说明：
 - nls=utf8       : include unicode for non-English users.
 - iocharset=utf8 : for non-ASCII characters in file names to be interpreted properly.
 - exec放到defaults后面，不然会defaults的中的参数覆盖。
