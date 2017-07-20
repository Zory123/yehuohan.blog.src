---
title: 命令学习 in Ubuntu
date: 2017-06-06 14:21:13
tags:
 - linux
 - ubuntu
categories: 
 - 笔记
---


---
# ***写在前面***
- 查看命令帮助：man (manual)，如 man rm
- 有相同命令时，可以先用man -f 查询，然后用man + 数字 + 命令名查询。
- 比较通用的命令参数：	
 - [--help]
 - [--version]
- 命令参数前一横：一般为字符形式，如 -d
- 命令参数前两横：一般为单词形式，如 --directory
 (<font color=red>注意：这里说的只是一般情况</font>))

 
<!-- more -->


---
# ***文件管理***

## **rm：删除文件或目录**
```bash
rm [-dfirv][--help][--version][file_dir]
rm file
	# 移除文件
rm -d dir
rm --directory dir
	# 移除空目录
rm -r folder/dir
rm -R folder/dir
rm -recursive folder/dir
	# 移除非空目录dir, -r 递归处理，将dir目录及目录下文件和子目录一并处理
-f -force
	# 强制删除
-v -verbose
	# 显示执行过程
```
## **ls：列出目录内容**
```bash
ls -a
	# 显示所有文件和目录，包括隐藏的
ls -l
	# 显示详细信息
ls -lh 
	# 用G M K等大单位来显示文件大小
ls -l --block-size=MB
	# 用M作为单位显示大小
ls -ld /etc/r*.d
ls -ld /etc/init.d
	# 详细显示r*.d(*是通配符，init.d是一个目录)目录信息，而不显示目录包含的文件信息
```

## **du：查看目录或文件所占用磁盘空间的大小**
```bash
du -s <dirname>
	# 只显示 <dirname>的大小，不显示子目录或子文
du -sh <dirname>
	# 以合适的单位显示<dirname>的大小
du -a <dirname>
	# 显示<dirname>及子目录和子文件的大小
```

## **cp：复制文件或目录**
```bash
cp [-abdfilpPrRsuvx][-S][-V][源文件目录][目录文件目录]
cp file dir/ff
	# 将file文件复制到dir目录下，并重命名为ff
cp -r floder/dir /temp/
	# 将目录dir及目录下的文件和子目录复制到temp下，即有temp/dir
```

## **mkdir：建立目录**
```
mkdir [-p][-m<目录属性>][目录名称]
```

## **touch：改变文件或目录时间**
```bash
touch [-acfm][-d<日期时间>][-r<参考文件或目录>][-t<日期时间>][文件或目录]
touch file
	# 建立空文件file
```

## **cat：将文件显示到基本输出**
```bash
cat [-AbeEnstTuv] filename
cat file
	# 显示file的内容，基本输出即指屏幕
-n 或 --number
	# 输出行号
```

## **ln：链接文件或目录**
```bash
ln -s file_src file_des
	# 建立符号连接，打开file_des时，即打开file_src,相当于快捷方式
```

## **grep： 查找文件里符合条件的字符串**
```bash
grep[-abcEFGhHilLnqrsvVwxy][-A][-B][-C][-d][-e][-f]
grep str file
	# 在file中查找str字符串
-n或--line-number
	# 显示行列
-i或--ignore-case
	# 忽略字符大小写
```

## **find：查找文件或目录**
```bash
find ~/ -name filename
	# 在 ～/ 查找filename的文件或目录
find ~/ -iname '*file'
	# 忽略大小写,查找符合 *file 形式的文件或目录
find ~/ -name '[aA][bB]d'
	# 查找 abd或Abd或aBd或ABd
find -name 'src*'
	# 在当前目录查找以src开头的文件或目录
find -name '*src*'
	# 查打包含src的文件或目录
find -size 30M
	# 查找等于30M的文件
find -size +10M -size -30M
	# 查找小于30M但大于10M的文件
```

## **locate：查找文件**
```bash
locate [-d<数据库文件>][--help][--version][范本样式...]
locate /etc/sh
	# 搜索etc目录下所有以sh开头的文件
updatedb 
	# 手动更新数据库/var/lib/locatedb
```

## **which：查找环境变量中的文件**
```bash
which [-n<文件名长度>][-p<文件名长度>][-w]
which ls
	# 查看命令ls的位置
```

## **rename：批量重命名**
```bash
rename perlexpr file
	# file：要处理的文件
	# perlexpr：perl正则表达式(ub16.04的rename是用perl实现的,所以没有 rename from to file形式)

rename s/file/list/ file*
	# 将所有file开头的文件变成list开头。
	# "s/<str>/<rep>/"：替换，str替换成rep
rename tr/A-Z/a-z/ file*
	# 将所有file开头的文件，变成小写
	# "tr/<par>/<rep>/"：转化，par转成rep
```
## **unzip：解压zip文件**
```bash
unzip [-cflptuvz][-agCjLMnoqsVX][-P<密码>][-d][-x]
unzip file.zip -d ～/dir
	# 解压file文件，放~/dir目录中
```
## **tar：备份还原文件**
```bash
-c # 建立新的归档文件
-r # 向归档文件末尾追加文件
-x # 从归档文件中解出文件
-t # 查看归档包中的文件
-u # 更新原压缩包中的文件
   # 这五个是独立的命令，压缩解压只会用到其中一个
		
-v # 处理过程中输出相关信息
-C # 解压到指定文件夹，大写的C
-f # 对普通文件操作(似乎一直都要用f)
-z # 有gzip属性的
-j # 有bz2属性的
-Z # 有compress属性的

tar -cf tmp.tar file.c
	# 创建归档文件tmp.tar
tar -xf	tmp.tar
	# 解压归档文件tmp.tar
```

## **cmp：比较两个文件是否有差异**
```bash
cmp [-clsv][-i <字符数目>][--help][第一个文件][第二个文件]
cmp file1.txt file2.txt
	# 比较两个文件，相同则不输出任何消息
cmp - file.txt
cmp file.txt -
	# 将file.txt与标准输入（即从终端输入）比较。输入命令回车后，需要从终端输入要比较的内容，回车然后ctrl+d输入结束，开始比较
```

## **comm：比较两个已排过序的文件**
```bash
comm [-123][--help][--version][第1个文件][第2个文件]
	-1   # 不显示只在第1个文件里出现过的列。
	-2   # 不显示只在第2个文件里出现过的列。
	-3   # 不显示只在第1和第2个文件里出现过的列。
comm file1 file2
	# 比较两个文件
	# 结果： 仅file1出现的行; 仅file2出现的行; 两个文件均出现的行
```

## **file：辨识文件类型**
```bash
file [-beLvz][-f < 名称文件 >][-m < 魔法数字文件 >...][ 文件或目录 ...]
file text.txt
	# 查看文件类型
file -z tempfile
	# 尝试解文件
```

## **echo：显示字符串到标准输出**
```bash
echo [-ne][字符串]
echo -e 'hello world\n'
	# 对\n等字符转义，同c语言中的转义
echo $PATH
	# 显示变量名PATH
echo '
	# 从标准输入后再输出，输入单引号’后结束输入，开始输入（两个单引号‘’算一个命令）
```


---
# ***系统管理***
## **su：变更用户身份**
```
su [-flmp][--help][--version][-][-c<指令>][-s<shell>][用户帐号]
su root
su
	// 切换root用户，不带用户时，预设为root
	// root的"～/"是"/root",不是"/home/username"
```
## **sudo：以其他身份来执行指令**
```
sudo [-bhHpV][-s<shell>][-u<用户>][指令]
sudo [-klv]
sudo passwd
	// 初次设置root密码，不然不能用root
```
## **passwd：设置密码**
```
passwd [-dklS][-u<-f>][用户名称]
passwd
	// 修改当前用户密码
passwd newuser
	// 更改用户newuser的密码
```

## **chmod：变更文件或目录权限**
```
chmod [-cfRv][--help][--version][mode][文件或目录]
　　-R 表示对当前目录下的所有文件和子目录进行相同的权限更改
　　mode 权限设置字串,格式为[ugoa] [+-=] [rwx]
	　　u user,表示文件的拥有者
	　　g group,表示与此文件拥有者属于一个组群的人
	　　o other,表示其他用户，拥有者和组群之外的人
	　　a all,表示包含以上三者即文件拥有者(u)、群组(g)、其他(o)
	　　+ 表示增加权限
	　　- 表示取消权限
	　　= 表示唯一设置权限
	　　r 表示有读取的权限
	　　w 表示有写入的权限
	　　x 表示有执行的权限
    mode = 数字abc，chmod可以用数字来表示权限
		a,b,c各为一个数字，分别表示User、Group、及Other的权限。
		r=4，w=2，x=1  (即二进制权值)
		若要rwx属性则4+2+1=7
		若要rw-属性则4+2=6
		若要r-x属性则4+1=5
chmod u+w file			# u增加写入权限
chmod u=w file			# u设置为只有定入权限
chmod 777 file			# 所有用户拥用rwx权限
```
## **chown：变更文件或目录拥有者或所属群**
```
chown [-cfhRv][--dereference][--help][--version][拥有者<所属群>][文件或目录]
chown me file					# file所有者改为me
chown -R hello:staff /folder	# folder目录及目录下所有目录和文件的所有者改为hello,群组为staff
								# -R 递归操作当前目录下的所有目录和文件
```

## **shutdown：系统关机命令**
```
shutdown [-efFhknr][-t秒数][时间][警告信息]
shutdown -h 	#关闭系统，即关机
shutdown -r		# 重启
reboot			# 重启
```

## **export:设置或显示环境变量**
```
export [-fnp][变量名称]=[变量设置值]
export PATH="$PATH:$HOME/dir"      # 添加路径$HOME/dir到PATH中,只是临时添加，不是更改配置文件
```

## **free：显示内存状态**
```
free -b(k)(m)(g)		# 以byte(kb)(mb)(gb)显示内存状态
free -s 5 -c 10			# 每隔5秒显示一次，共显示10次
```

## **kill：删除执行中的进程**
```
kill [-s <信息名称或编号>][程序]
kill [-l <信息编号>]
[程序]可以是程序的 PID 或是 PGID,也可以是工作编号;
PID可以使用htop查看;
kill 2950			# 结束PID为2950的程序
```

## **pkill：直接杀死运行中的程序**
```
pkill firefox		# 结束firefox程序
					# firefor是程序名，也即是“命令名”
					# 要结束一个程序的单个进程，使用 kill PID
```

## **xkill：杀死图形程序**
```
xkill			# 运行后，鼠标光标会会变成“X”型，点击相应的程序图形窗口就可以结束程序
```

## **pgrep：查找进程id**
```
pgrep chro -l			# 查找关键字chro的进程id，并显示进程名称
```

## **ps：报告程序状况**
```
ps：process status
ps -A | grep chrome		# 在所有运行的程序中查找chrome
```

## **pstree：以树状图显示程序**
```
pstree：process status tree
pstree					# 以树状图显示程序
pstree -a				# 显示所有程序及其相关信息
```

## **screen：多重视窗管理程序**
```
screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s ][-S <作业名称>]

screen -S newwork		# 新建一个视窗
screen -ls				# 列出所有视窗
screen -r work			# 恢复work视窗
```

## **alias：设置指令的别名**
```
alias name = 'command line'		# 基本用法
alias mv='mv -i'				# mv就自带参数-i
alias -p						# 列出现有的所有别名
```

---
# ***设备管理***
## **mount：挂载命令**
```
mount [-t vfstype][-o options][挂载设备][目录]
mount /dev/sda1 mymount
	// 把sda1(第一块硬盘第一分区)挂载到mymount目录
mount -o rw /dev/sda1 mymount
	// 读写方式挂载
mount -o loop /file mymount
	// 将文件（如ISO文件）挂载成设备
mount -t fat32 /dev/sda1 mymount
	// 指定要挂载的设备类型为fat32
```
## **df：显示磁盘相关信息**
```
df [-ahHiklmPT][--block-size=<区块大小>][-t][-x][--no-sync][--sync][文件或设备]
df	-T -h
	// 显示磁盘信息，包括分区类型，大小以G M K 等大单位显示
```
## **lspci：查看pci设备信息**
```
lspci 
	// 显示pci简略信息
lspci -v
	// 显示pci设备详细信息，-vv更详细，-vvv非常详细
```
## **blkid:查看块设备（包括交换分区）的信息**
```bash
sudo blkid 
	# 列出当前系统中所以已挂载文件系统的类型
blkid /dev/sda1
	# 查看指定设备信息
sudo blkid -s LABEL
	# 查看设备的LABEL
sudo blkid -s UUID
	# 查看设备的UUID
```

## **lsusb：查看usb设备**
```bash
lsusb
	# 列出所有usb信息
lsusb -v
	# 显示pci设备详细信息，-vv更详细
```


---
# ***软件管理***

百度百科解释：
-*aptitude与 apt-get 一样，是 Debian 及其衍生系统中功能极其强大的包管理工具。与 apt-get 不同的是，aptitude在处理依赖问题上更佳一些。举例来说，aptitude在删除一个包时，会同时删除本身所依赖的包。这样，系统中不会残留无用的包，整个系统更为干净。*-

-*Advanced Package Tool，又名apt-get，是一款适用于Unix和Linux系统的应用程序管理器。Apt-get成名的原因之一在于其出色的解决软件依赖关系的能力。*-

-*“dpkg ”为 “Debian” 专门开发的套件管理系统，方便软件的安装、更新及移除。用来安装.deb文件,但不会解决模块的依赖关系,且不会关心ubuntu的软件仓库内的软件,可以用于安装本地的deb文件 *-


## **aptitude**
```bash
aptitude search package
aptitude search "str1 str2" //xkeyword: str1 && str2 
aptitude search str1 str2 //   str1 || str2
	# 查找软件包，i为已经安装，p为未安装的
aptitude install package
	# 安装软件包
aptitude remove package
	# 删除软件包
```

## **apt-get**
```bash
apt-get install package
	# 安装软件包
apt-get install --reinstall package   
	# 重新安装包
apt-get -f install   
	# 修复安装，比如dpkg装完一个软件包后，提示一些库没有，用此命令即可修复
apt-get remove package
	# 删除软件包(不包抱配置文件)
apt-get remove --purge pakage
	# 删除软件包(包抱配置文件)
add-apt-repository ppa:"ppa_name"
	# 添加ppa个人软件源，将其添加至当前apt（/etc/apt/sources.list.d）库中
apt-get update
	# 是同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引,即运行这条命令时，是我们想知道软件源中有哪些软件了
sudo apt-get autoclean 
	# 清理旧版本的软件缓存
sudo apt-get clean 
	# 清理所有软件缓存
sudo apt-get autoremove 
	# 删除系统不再使用的孤立软件
```

## **apt-cache**
```bash
apt-cache show package
	# 显示指定软件包的信息，包括版本号，安装状态和包依赖关系等
apt-cache search package
	# 按关键字查找软件包
apt-cache depends package
	# 显示指定软件包所依赖的软件包
```


## **dpkg**
```bash
dpkg -i package.deb 
	# 安装软件包，安装deb包，但不能自己解模专依赖问题，只会提示你需要安装依赖的模块
dpkg -r package
	# 删除软件包
dpkg -r --purge pacakge
	# 连同软件包的配置文件一块删除
dpkg --info xxx.deb
	# 查看deb包的信息
dpkg -l
	# 查看系统中已安装软件包信息
dpkg --instdir=DIR
	# 指定安装目录
dpkg -L pacakge
	# 列出与该包相关联的文件
```

---
# ***程序相关***
## **pkg-config：用于提供库等路径**
```bash
pkg-config --libs opecv
	# 查看opencv的库位置，将会有如下输出：
-L/usr/local/lib -lopencv_shape -lopencv_stitching -lopencv_objdetect -lopencv_superres -lopencv_videostab -lippicv -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_video -lopencv_photo -lopencv_ml -lopencv_imgproc -lopencv_flann -lopencv_core
	# 可以看到-L和-l表示库的目录的和文件
pkg-config --cflags opencv
	# 查年opencv的cflags参数，将会有如下输出：
-I/usr/local/include/opencv -I/usr/local/include
	# 可以看到-I表示包含的目录

	# pkg-config是找一个*.pc的文件，可以查看opencv.pc的位置：
locate opnecv.pc
	# 我的在/usr/local/lib/pkgconfig/opencv.pc
```

---


---
# 终端快捷键

|快捷键	|功能|
|-------|---|
|Tab	|自动补全|
|Tab(连按两次)|显示可以自动补全的内容
|Ctrl+a	|光标移动到开始位置
|Ctrl+e	|光标移动到最末尾
|Ctrl+k	|删除此处至末尾的所有内容
|Ctrl+u	|删除此处至开始的所有内容
|Ctrl+d	|删除当前字符
|Ctrl+h	|删除当前字符前一个字符
|Ctrl+w	|删除此处到左边的单词
|Ctrl+y	|粘贴由Ctrl+u， Ctrl+d， Ctrl+w删除的单词
|Ctrl+l	|相当于clear，即清屏
|Ctrl+r	|查找历史命令
|Ctrl+b	|向回移动光标
|Ctrl+f	|向前移动光标
|Ctrl+t	|将光标位置的字符和前一个字符进行位置交换
|Ctrl+&	|恢复 ctrl+h 或者 ctrl+d 或者 ctrl+w 删除的内容
|Ctrl+S	|暂停屏幕输出
|Ctrl+Q	|继续屏幕输出
|Ctrl+Left-Arrow	|光标移动到上一个单词的词首
|Ctrl+Right-Arrow	|光标移动到下一个单词的词尾
|Ctrl+p	|向上显示缓存命令
|Ctrl+n	|向下显示缓存命令
|Ctrl+d	|关闭终端
|Ctrl+xx	|在EOL和当前光标位置移动
|Ctrl+x@	|显示可能hostname补全
|Ctrl+c	|终止进程/命令
|Shift+上或下	|终端上下滚动
|Shift+PgUp/PgDn	|终端上下翻页滚动
|Ctrl+Shift+n	|新终端
|alt+F2	|输入gnome-terminal打开终端
|Shift+Ctrl+T	|打开新的标签页
|Shift+Ctrl+W	|关闭标签页
|Shift+Ctrl+C	|复制
|Shift+Ctrl+V	|粘贴
|Alt+数字	|切换至对应的标签页
|Shift+Ctrl+N	|打开新的终端窗口
|Shift+Ctrl+Q	|管壁终端窗口
|Shift+Ctrl+PgUp/PgDn	|左移右移标签页
|Ctrl+PgUp/PgDn	|切换标签页
|F1	|打开帮助指南
|F10	|激活菜单栏
|F11	|全屏切换
|Alt+F	|打开 “文件” 菜单（file）
|Alt+E	|打开 “编辑” 菜单（edit）
|Alt+V	|打开 “查看” 菜单（view）
|Alt+S	|打开 “搜索” 菜单（search）
|Alt+T	|打开 “终端” 菜单（terminal）
|Alt+H	|打开 “帮助” 菜单（help）
