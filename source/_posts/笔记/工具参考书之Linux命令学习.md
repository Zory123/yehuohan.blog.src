---
title: 工具参考书之Linux命令学习
date: 2017-06-06 14:21:13
tags:
 - linux
 - ubuntu
categories: 
 - 笔记
---


---
# ***写在前面***
 - 查看命令帮助：man (manual)，如 man ls；
 - 有相同命令时，可以先用man -f 查询，然后用man + 数字 + 命令名查询；
 - 命令参数前一横：一般为字符形式，如 -d；命令参数前两横：一般为单词形式，如 \-\-directory （***注意：这里说的是一般情况***）；
 - 输入命令时多用Tab，可以自动补全，尤其是zsh
 - 这里的命令均是`学了多少就记录多少`，一个命令不会详解其所有用法。

 
<!-- more -->


---
# ***文件管理***

## rm：删除文件或目录

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

## ls：列出目录内容

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

## du：查看目录或文件所占用磁盘空间的大小

```bash
du -s <dirname>
    # 只显示 <dirname>的大小，不显示子目录或子文
du -sh <dirname>
    # 以合适的单位显示<dirname>的大小
du -a <dirname>
    # 显示<dirname>及子目录和子文件的大小
```

## cp：复制文件或目录

```bash
cp [-abdfilpPrRsuvx][-S][-V][源文件目录][目录文件目录]
cp file dir/ff
    # 将file文件复制到dir目录下，并重命名为ff
cp -r floder/dir /temp/
    # 将目录dir及目录下的文件和子目录复制到temp下，即有temp/dir
```

## mkdir：建立目录

```bash
mkdir [-p][-m<目录属性>][目录名称]
```

## touch：改变文件或目录时间

```bash
touch [-acfm][-d<日期时间>][-r<参考文件或目录>][-t<日期时间>][文件或目录]
touch file
    # 建立空文件file
```

## cat：将文件显示到基本输出

```bash
cat [-AbeEnstTuv] filename
cat file
    # 显示file的内容，基本输出即指屏幕
-n 或 --number
    # 输出行号
```

## ln：链接文件或目录

```bash
ln -s file_src file_des
    # 建立符号连接，打开file_des时，即打开file_src,相当于快捷方式
    # -s 为软链接，保持同步变化，但不占硬盘空间，而硬链接同样保持同步变化，但占硬盘空间
```

## grep： 查找文件里符合条件的字符串

```bash
grep[-abcEFGhHilLnqrsvVwxy][-A][-B][-C][-d][-e][-f]
grep str file
    # 在file中查找str字符串
-n或--line-number
    # 显示行列
-i或--ignore-case
    # 忽略字符大小写
```

## find：查找文件或目录

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

## locate：查找文件

```bash
locate [-d<数据库文件>][--help][--version][范本样式...]
locate /etc/sh
    # 搜索etc目录下所有以sh开头的文件
updatedb 
    # 手动更新数据库/var/lib/locatedb
```

## which：查找环境变量中的文件

```bash
which [-n<文件名长度>][-p<文件名长度>][-w]
which ls
    # 查看命令ls的位置
```

## rename：批量重命名

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

## unzip：解压zip文件

```bash
unzip [-cflptuvz][-agCjLMnoqsVX][-P<密码>][-d][-x]
unzip file.zip -d ～/dir
    # 解压file文件，放~/dir目录中
```

## tar：备份还原文件

```bash
-c # 建立新的归档文件
-r # 向归档文件末尾追加文件
-x # 从归档文件中解出文件
-t # 查看归档包中的文件
-u # 更新原压缩包中的文件
   # 这五个是独立的命令，压缩解压只会用到其中一个
        
-v # 处理过程中输出相关信息
-C # 解压到指定文件夹，大写的C
-f # 后面要立刻接被处理的档案名，建议-f单独写一个选项
-j # 使用bzip2算法，后缀为tar.bz2（用得较多）
-z # 使用gzip算法，后缀为tar.gz（用得较多）
-J # 使用xz算法，后缀为tar.xz
-Z # 使用compress算法，后缀为tar.Z

tar -c -f tmp.tar file.c
    # 创建归档文件tmp.tar，tar只打包，不压缩
tar -r -f tmp.tar <dir>
    # 向tmp.tar中追加目录
tar -xj -f tmp.tar.bz2
    # 解压归档文件tmp.tar.bz2，使用bzip2压缩
tar -xz -f tmp.tar.gz -C <dir>
    # 解压归档文件tmp.tar.gz到指定目录，使用gzip压缩
tar -t -f tmp.tar.gz | grep foo
    # 查看归档文件，并查找含有关键foo的文件或目录
```

## cmp：比较两个文件是否有差异

```bash
cmp [-clsv][-i <字符数目>][--help][第一个文件][第二个文件]
cmp file1.txt file2.txt
    # 比较两个文件，相同则不输出任何消息
cmp - file.txt
cmp file.txt -
    # 将file.txt与标准输入（即从终端输入）比较。输入命令回车后，需要从终端输入要比较的内容，回车然后ctrl+d输入结束，开始比较
```

## comm：比较两个已排过序的文件

```bash
comm [-123][--help][--version][第1个文件][第2个文件]
    -1   # 不显示只在第1个文件里出现过的列。
    -2   # 不显示只在第2个文件里出现过的列。
    -3   # 不显示只在第1和第2个文件里出现过的列。
comm file1 file2
    # 比较两个文件
    # 结果： 仅file1出现的行; 仅file2出现的行; 两个文件均出现的行
```

## file：辨识文件类型

```bash
file [-beLvz][-f < 名称文件 >][-m < 魔法数字文件 >...][ 文件或目录 ...]
file text.txt
    # 查看文件类型
file -z tempfile
    # 尝试解文件
```

## echo：显示字符串到标准输出

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

## su：变更用户身份

```bash
su [-flmp][--help][--version][-][-c<指令>][-s<shell>][用户帐号]
su root
# 切换root用户，不带用户时，预设为root
# root的"～/"是"/root",不是"/home/username"
```

## sudo：以其他身份来执行指令

```bash
sudo [-bhHpV][-s<shell>][-u<用户>][指令]
sudo [-klv]
sudo passwd
    # 初次设置root密码，不然不能用root
```

## passwd：设置密码

```bash
passwd [-dklS][-u<-f>][用户名称]
passwd
    # 修改当前用户密码
passwd newuser
    # 更改用户newuser的密码
```

## gpasswd：管理组

```bash
gpasswd[-a user][-d user][-A user,...][-M user,...][-r][-R] groupname
# -a：添加用户到组
# -d：从组删除用户
# -A：指定管理员
# -r：删除密码

gpasswd -A peter group 
# 添加peter为group组的管理员
gpasswd -a mary group
# 添加mary到group组
```

## chmod：变更文件或目录权限

```bash
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
chmod u+w file          # u增加写入权限
chmod u=w file          # u设置为只有定入权限
chmod 777 file          # 所有用户拥用rwx权限
```

## chown：变更文件或目录拥有者或所属群

```bash
chown [-cfhRv][--dereference][--help][--version][拥有者<所属群>][文件或目录]
chown me file                   # file所有者改为me
chown -R hello:staff /folder    # folder目录及目录下所有目录和文件的所有者改为hello,群组为staff
                                # -R 递归操作当前目录下的所有目录和文件
```

## shutdown：系统关机命令

```bash
shutdown [-efFhknr][-t秒数][时间][警告信息]
shutdown -h     #关闭系统，即关机
shutdown -r     # 重启
reboot          # 重启
```

## export:设置或显示环境变量

```bash
export [-fnp][变量名称]=[变量设置值]
export PATH="$PATH:$HOME/dir"      # 添加路径$HOME/dir到PATH中,只是临时添加，不是更改配置文件
```

## free：显示内存状态

```bash
free -b(k)(m)(g)        # 以byte(kb)(mb)(gb)显示内存状态
free -s 5 -c 10         # 每隔5秒显示一次，共显示10次
```

## &：后台运行程序

```bash
command &
# 在后台运行命令command，但标准输出仍会显示到当前终端
# command命令运行结束后，自动结束
sh tmp.sh & > /dev/null
# 后台运行tmp.sh，并将输出结重定向到空设备，即不显示输出
ctrl+z
# 将终端的运行的命令放到后台，并且暂停运行
# 如在终端打开了chrome，这时终端不能用且不能关了，用ctrl+z就可将chrome放入后台运行
```

## jobs：显示后台任务状态

```bash
jobs
# 显示与当前终端相关连的后台任务
# 可以看到任务的工作号，即1,2,3...
jobs -l
# 同时显示后台任的工作号和PID
bg %n
# 继续运行暂停(suspended)的任务，任务工作号为n
fg %n
# 将后台运行的任务放到前台运行，任务工作号为n
```

## kill：删除执行中的进程

```bash
kill [-s <信息名称或编号>][程序]
kill [-l <信息编号>]
# [程序]可以是程序的 PID 或是 PGID,也可以是工作编号;
kill 2950           # 结束PID为2950的程序
kill %n             # 结束工作号为n的程序

kill -s SIGTERM 2950 # 请求正常结束程序，此为默认选项
kill -15 2950        # 请求正常结束程序，此为默认选项
kill -l 15           # 查看信号15的名称，会输出“TERM”，即SIGTERM信号

kill -s SIGKILL 2950 # 强制结束程序
kill -9 2950         # 强制结束程序
kill -l SIGKILL      # 醒看信号SIGKILL的编号，会输出9
```

## pkill：直接杀死运行中的程序

```bash
pkill firefox       # 结束firefox程序
                    # firefor是程序名，也即是“命令名”
                    # 要结束一个程序的单个进程，使用 kill PID
```

## xkill：杀死图形程序

```bash
xkill           # 运行后，鼠标光标会会变成“X”型，点击相应的程序图形窗口就可以结束程序
```

## pgrep：查找进程id

```bash
pgrep chro -l           # 查找关键字chro的进程id，并显示进程名称
```

## ps：报告程序状况

```bash
ps：process status
ps -A | grep chrome     # 在所有运行的程序中查找chrome
```

## pstree：以树状图显示程序

```bash
pstree：process status tree
pstree                  # 以树状图显示程序
pstree -a               # 显示所有程序及其相关信息
```

## screen：多重视窗管理程序

```bash
screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s ][-S <作业名称>]

screen -S newwork       # 新建一个视窗
screen -ls              # 列出所有视窗
screen -r work          # 恢复work视窗
```

## alias：设置指令的别名

```bash
alias name = 'command line'     # 基本用法
alias mv='mv -i'                # mv就自带参数-i
alias -p                        # 列出现有的所有别名
```

---
# ***设备管理***

## mount：挂载命令

```bash
mount [-t vfstype][-o options][挂载设备][目录]
mount /dev/sda1 mymount
    # 把sda1(第一块硬盘第一分区)挂载到mymount目录
mount -o rw /dev/sda1 mymount
    # 读写方式挂载
mount -o loop /file mymount
    # 将文件（如ISO文件）挂载成设备
mount -t fat32 /dev/sda1 mymount
    # 指定要挂载的设备类型为fat32
```

## df：显示磁盘相关信息

```bash
df [-ahHiklmPT][--block-size=<区块大小>][-t][-x][--no-sync][--sync][文件或设备]
df  -T -h
    # 显示磁盘信息，包括分区类型，大小以G M K 等大单位显示
```

## lspci：查看pci设备信息

```bash
lspci 
    # 显示pci简略信息
lspci -v
    # 显示pci设备详细信息，-vv更详细，-vvv非常详细
```

## blkid： 查看块设备（包括交换分区）的信息

```bash
sudo blkid          # 列出当前系统中所以已挂载文件系统的类型
blkid /dev/sda1     # 查看指定设备信息
sudo blkid -s LABEL # 查看设备的LABEL
sudo blkid -s UUID  # 查看设备的UUID
```

## lsblk：查看块设备

```bash
lsblk
# 列出块设备，会显示名称(sda,sdb)、大小、挂载点等信息
lsblk -f
# 列出文件系统、标签、UUDI等信息
lsblk -p
# 列出设备完整路径
```

## lsusb：查看usb设备

```bash
lsusb
    # 列出所有usb信息
lsusb -v
    # 显示pci设备详细信息，-vv更详细
```

## xrandr：管理显示器

```bash
xrandr
# 查看当前显示器状态
xrandr --output HDMI-1 --mode 1920x1080
# 设置通过HDMI连接的显示器分辨率
# 设置完后一般两显示为复制显示
xrandr --output LVDS-1 --primary
# 将笔记本自身显示器设为主显示器
xrandr --output HDMI-1 --right-of LVDS-1
# 设置HDMI在LVDS的右边扩展显示
xrandr --ourput HDMI-1 --off
# 关闭HDMI-1

# 附：arandr, lxrandr为xrandr的图形客户端
# 附：xrandr的设置为临时设置，在/etc/X11/xorg.conf
```

---
# ***程序相关***

## pkg-config：用于提供库等路径

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
# ***Arch软件管理***

## pacman

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

---
# ***Ubuntu软件管理***

百度百科解释：
-*aptitude与 apt-get 一样，是 Debian 及其衍生系统中功能极其强大的包管理工具。与 apt-get 不同的是，aptitude在处理依赖问题上更佳一些。举例来说，aptitude在删除一个包时，会同时删除本身所依赖的包。这样，系统中不会残留无用的包，整个系统更为干净。*-

-*Advanced Package Tool，又名apt-get，是一款适用于Unix和Linux系统的应用程序管理器。Apt-get成名的原因之一在于其出色的解决软件依赖关系的能力。*-

-*“dpkg ”为 “Debian” 专门开发的套件管理系统，方便软件的安装、更新及移除。用来安装.deb文件,但不会解决模块的依赖关系,且不会关心ubuntu的软件仓库内的软件,可以用于安装本地的deb文件 *-


## aptitude

```bash
aptitude search package
aptitude search "str1 str2"  # keyword: str1 && str2 
aptitude search str1 str2    #          str1 || str2
    # 查找软件包，i为已经安装，p为未安装的
aptitude install package
    # 安装软件包
aptitude remove package
    # 删除软件包
```

## apt-get

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

## apt-cache

```bash
apt-cache show package
    # 显示指定软件包的信息，包括版本号，安装状态和包依赖关系等
apt-cache search package
    # 按关键字查找软件包
apt-cache depends package
    # 显示指定软件包所依赖的软件包
```


## dpkg

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
