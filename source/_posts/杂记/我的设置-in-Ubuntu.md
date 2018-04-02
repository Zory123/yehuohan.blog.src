---
title: 我的设置 in Ubuntu
tags:
  - linux
  - ubuntu
categories:
  - 杂记
date: 2017-06-07 00:38:29
---


---
# *安装与启动*
 - 我使用efi启动，用一个efi-loader（如refind）加载ubuntu的grubx64.efi，配置文件件为grub.cfg，cfg内容如下。其中2490e456-7285-4e1f-923d-f2dbca786508是ubuntu根目录"/"挂载磁盘的uuid，即hd1,msdos10的uuid。用grubx64.efi加载ubuntu的/boot/grub/grub.cfg来启动ubuntu。

```bash
search.fs_uuid 2490e456-7285-4e1f-923d-f2dbca786508 root hd1,msdos10
set prefix=($root)'/boot/grub'
configfile $prefix/grub.cfg
```

 - 我的是双系统win8.1+ubuntu，efi启动，refind引导)：
   引导文件：http://pan.baidu.com/s/1qWLjvn2
   安装教程：http://www.rodsbooks.com/refind/installing.html

<!-- more -->

---
# *安装五笔*
 - 使用 fcitx 五笔拼音，（主要用五笔）
   
```bash
sudo apt-get install fcitx-table-wbpy
```

  - 去掉四码自动上屏：配置当前输入法 ， 双击“五笔拼音” , 选择“wupy.conf",编辑，去掉自动上屏选项

---
# *更改Home文件夹为英文*
 - 将桌面、下载、模板、公共、文档、音乐、图片、视频里的文件夹数据备份，然后全删
 - 终端：

```bash
   cd ~/
   mkdir Desktop Download Template Public Document  Music Picture Video
   vim ~/.config/user-dirs.dirs
```

 - 按下面所示修改：

```bash
　　XDG_DESKTOP_DIR="$HOME/Desktop"
　　XDG_DOWNLOAD_DIR="$HOME/Download"
　　XDG_TEMPLATES_DIR="$HOME/Template"
　　XDG_PUBLICSHARE_DIR="$HOME/Public"
　　XDG_DOCUMENTS_DIR="$HOME/Document"
　　XDG_MUSIC_DIR="$HOME/Music"
　　XDG_PICTURES_DIR="$HOME/Picture"
　　XDG_VIDEOS_DIR="$HOME/Video"
```

---
# *添加触摸板控制*
 - ubuntu下笔记本的Fn不能关闭触控版了，自己添加快捷键
 - 打开：系统设置，键盘，快捷键，自定义快捷键
 - 按下面所示添加：
```
synclient touchpadoff=1 	//--关闭触摸板(16.04目前无效)
synclient touchpadoff=0 	//--开启触摸板(16.04目前无效)
或:
gconftool-2 --toggle /desktop/gnome/peripherals/touchpad/touchpad_enabled
	// 开关触控板(16.04目前无效)
```

添加完后如图：

{% asset_img 01.png %}

- 或用python脚本：
（<font color=red>原文：http://www.linuxidc.com/Linux/2014-04/100612.htm</font>）

```bash
#!/usr/bin/env python

import os

def check_touchpad_state(dev_num):
    dev_state = os.popen('xinput list-props  %s' % str(dev_num))
    for lines in dev_state.readlines():
        if 'Device Enabled' in lines:
            sig = lines[-3:-1].strip()
            signal = int(sig)
            print ('signal now :%d' % signal)
            return signal
            
    
def get_dev_num(dev_name = 'SynPS/2 Synaptics TouchPad'):
    dev_state = os.popen('xinput list')
    for lines in dev_state.readlines():
        if dev_name in lines:
            print (lines)
            station = lines.find('id=')
            dev_num = lines[station + 3: station+5]
            dev_num = int(dev_num)
            print ('dev_num: %d' % dev_num)
            return dev_num
    dev_state.close()

def change_state(state_value, dev_num):
    print ('state_value = ', state_value)
    state = not state_value
    if state == True:
        state = 1
    #else:
        #state = 0
    #print ('state = ', state, str(state))
    tem = os.popen("xinput set-prop %s 'Device Enabled' %s" % (str(dev_num), str(state)))
    tem.close()
    
def main():
    dev_num = get_dev_num()
    state = check_touchpad_state(dev_num)
    change_state(state, dev_num)
    
    
if __name__ == '__main__':
    main()
```

保存成py文件，增加x权限，链到/usr/local/bin中，再增加快捷键。

# *常用快捷键和技巧*
 - 记住吧，方便，常用

```
Meta				//win键，长按，显示快捷键信息
ctrl + h			//显示隐藏文件（.开头的文件）
shift + delete		//永久删除
Meta + D			//显示桌面
Meta + S			//打开工作区切换器
alt + print			//对窗口截图
shift + print		//对选区截图

Dash搜索：fcitx五笔输入时，输入法看不清，可能直接输入中文拼音字母
```

---
# *解决双系统时间同步问题*
 - 方法随便就能百度到，这里使用Ubuntu禁用UTC的方法，与windows系统保持一致,否则windows时间会变成错的。终端：

```bash
sudo gedit /etc/default/rcS
# 将 UTC = yes 改成 UTC = no
```

 - 对于ubuntu16.04只需要运行下面的命令：

```bash
sudo hwclock --systohc --localtime
```

 
 ---
# *安装NVIDIA驱动*
 - 关闭独立显示，降低发热量（默认双显卡均在工作状态）
 - 可以到[官网下载](http://www.nvidia.cn/Download/index.aspx?lang=cn)，安装显卡驱动需要重启才会生效
 - 在Nvidia官方的控制面板nvidia-settings里就可以切换显卡（alt+F2搜索nvidia-settings）
 - 或者用apt-get下载，打开终端：

```bash
sudo apt-get install nvidia-331 nvidia-settings nvidia-prime
	# 331是版本，可以先用aptitude search查看有什么版本，然后确定用什么版本，或到上述官网看支不支持自己的显示
sudo apt-get remove --purge nvidia-331
	# 用于卸载显示驱动的，版本要对应
sh ./nvidia.run --uninstall
	# 网管下载的驱动用此命令
```

 - 使用命令：

```bash
lspci | grep -i vga
	# 列出双显示卡工作情况， “rev ff”表示关闭 ， “rev+数字” 表示打开
```

---
# *解决硬盘UUID问题*
 - 一般提示为 “为 xxxx准备的磁盘尚未就绪或不存在”，原因是分区的UUID因格式化或重新分区等原因变了，导致ubuntu找不到分区了，改好就行。终端:

```bash
sudo blkid
	# 查看分区正确的UUID
sudo vim /etc/fstab
	# 将分区错误的UUID修改成正确的
	# 也可用gedit修改
sudo gedit /etc/fstab 
```

---
# *删除自带游戏*
 - 在软件中心卸载即可，自带游戏的英文名：
	* 对对碰：Mahjongg
	* 数独：sudoku
	或者，在Dash搜到要卸载的程序，然后右击---卸载

---
# *安装vim*
- 自带vi有点问题，（上下左右键不好角等），安装vim

```bash
sudo apt-get remove vim-common
	//卸载旧版本
sudo apt-get install vim
	//安装full版vim
```

- 下载配置文件，(这里是我的)[https://git.oschina.net/yehuohan/LinuxConfigs]，也可自己配置，或者下载其它的。
- 将CapsLock换走，免得占了一个黄金位置。
 
linux下：

```bash
# capslock作为esc
# 我试过的所有方法中，只有安装gnome-tweak-tool可以实现开机自动交制钱esc和capslock
sudo apt-get install gnome-tweak-tool
# 在“输入-大写锁定键行为”可以更改

# ctrl作为esc
sudo vim /etc/default/keyboard
# 添加：
XKBOPTIONS="ctrl:nocaps"	# 将capslock当成另一个ctrl键
# 或者
XKBOPTIONS="ctrl:swapcaps"	# 将capslock和ctrl对调
# 到底哪个，看自己习惯吧。
# 然后执行，出现对话框后，一般一路默认即可
sudo dpkg-reconfigure keyboard-configuration
```

windows下：(windows可以使用vim)

```
# 打开注册表，找到
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]
# 添加二进制键值，若没有的话：
键名：Scancode Map
对调ctrl和caps键值：（共12个字节）
00 00 00 00
00 00 00 00
03 00 00 00
1d 00 3a 00
3a 00 1d e0
对调esc和capslock键值：
00 00 00 00
00 00 00 00
03 00 00 00
3a 00 01 00
01 00 3a 00
00 00 00 00
# 键值具涵义就不讲了
```

---
# *解决zip中文乱码问题*
 - 终端：

```bash
sudo gedit /etc/environment
	# 添加下面两行
UNZIP="-O CP936"
ZIPINFO="-O CP936"
	# 上述方法不行，用下面命令解压
unzip -O gbk xxx.zip
```

---
# *解决MP3标签乱码问题*
 - 非utf-8编码的标签会用问题，终端：

```bash
vim ~/.profile
	# 添加下面两行，可以解决 Rhythmbox、Totem 等以 GStreamer 为后端的播放器的乱码问题
export GST_ID3_TAG_ENCODING=GBK:UTF-8:GB18030
export GST_ID3V2_TAG_ENCODING=GBK:UTF-8:GB18030
```

- 另一种办法就是直接更换播放器，比如有一个个人开发linux酷我播放器，网易云播放器个人感觉要比Rhythmbox好用点。

---
# *设置wifi热点*
 - 禁用wifi
 - 按下图添加，“点添加，选 wifi”

{% asset_img 02.png%}

 - 按下列图设置
{% asset_img 03.png%}.
{% asset_img 04.png%}.
{% asset_img 05.png%}.

 - 打开终端

```bash
sudo gedit /etc/NetworkManager/system-connections/ubuntu
	//ubuntu 为设我们设置的wifi名称
	//mode = infrastructure 改成 mode = ap
```

- 重启一下电脑最好，连接wifi，如果没有显示，连接到隐藏wifi即可

---
# *安装c语言开发环境*
- 安装build-essential，build-essential依赖于gcc，g++等，因此安装build-essential后，相应的gcc，g++等也都安装了。

```bash
sudo apt-get install build-essential
```

-  安装vim做为c/c++的文本编辑器，注意先卸载原来的。

```bash
sudo apt-get remove vim-common
sudo apt-get install vim-full
```

---
# *设置启动器*
## **设置点击图标最小化**
 打开终端：

```bash
gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-minimize-window true
```

## **设置启动器位置**
将 Ubuntu 16.04 LTS 的 Unity 启动器移动到桌面底部命令：

```
gsettings set com.canonical.Unity.Launcher launcher-position Bottom
```

恢复到原来的左侧命令：

```
gsettings set com.canonical.Unity.Launcher launcher-position Left
```

## **时间菜单栏双月问题(16-04版本)**

```
gsettings set com.canonical.indicator.datetime time-format 'custom'
gsettings set com.canonical.indicator.datetime custom-time-format '%m月%d日 %A%H:%M:%S'
```

---
# *安装google-chrome*
 - chromet自带flash相对方便点，先下载chrome安装包，执行下列命令

```bash
sudo apt-get -f install
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

附带fanqiang用工具[lantern](https://github.com/getlantern/lantern)和[XX-Net](https://github.com/XX-net/XX-Net)
 
 - 安装[微软雅黑字体V6.0(msyh.ttf)](http://download.csdn.net/download/yehuohan/9507606)，重登电脑将chrome的字体全设为msyh，解决字体发虚问题。

---
# *安装Qt的中文输入问题*
 - qt官网下载qt的安装包，以qt5.6.0为例，一般安装后qt creator不能输入中法，编写的gui程序也不能输入中文，解决方法如下：
 - 安装fcitx-frontend-qt5（16.04自带安装）
 - 将安装后的fcitx-frontend-qt5复制到qt安装目录
	通常，fcitx-frontend-qt5在下面的目录路径中（可用命令dpkg -L 包名看文件安装路径)：
	<font color=Red>/usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so</font>
	将该文件复制到qt安装目录:
	<font color=Red>/Tools/QtCreator/bin/plugins/platforminputcontexts</font>
	(没有的话就在 <font color=Red>/Tools/QtCreator/lib/Qt/plugins/platforminputcontexts</font>)
	和:
	<font color=Red>/5.6/gcc_64/plugins/platforminputcontexts</font>中,重新打开 QtCreator,终于可以输入中文了。

---
# *安装chmsee*
 - chmsee是chm文档的阅读器，ub14.04后只能下载deb安装了。先安装必要的库文件

```
sudo apt-get install libc6 libchm1 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk2.0-0 libpango1.0-0 libwebkitgtk-1.0-0 libxml2
```

- 然后安装[libgcrypt11](http://download.csdn.net/detail/yehuohan/9507662)：

```
sudo dpkg -i libgcrypt11_1.5.3-2ubuntu4.3_amd64.deb
```

- 最后安装[chmsee](http://download.csdn.net/detail/yehuohan/9507681)：

```
sudo dpkg -i chmsee_1.3.0-2ubuntu2_amd64.deb
```

- 打开chm中文文档乱码时，在设置中可以编码，改成 “简体中文GBK”

---
# *安装Courier New字体*

```bash
sudo apt-get install ttf-mscorefonts-installer
```

它的本质是安装 Courier New字体;
安装的时候会出现一个协议 ，按TAB键 ，可以选中<确定>按钮，按Enter 。


---
# *安装man中文帮助文档*

 - 下载[中文man帮助文档](http://download.csdn.net/detail/yehuohan/9515147)
 - 在解压后出来的文件夹中运行：

``` bash
./configure --prefix=/usr/local/zhman --disable-zhtw             
	// 安装到/usr/local/zhman下
make
make install
```

 - 在 “～/.bashrc" 中添加：

```bash
alias cman='man -M /usr/local/zhman/share/man/zh_CN'   
```

 - 之后在 "~/" 下运行：

```bash
source .bashrc 
```

 - 安装完毕，man命令查看英文帮助文档，cman命令查看中文帮助文档


---
# *设置qmake路径*

qt5.7安装在home下后，ubuntu默认的qmake路径是不匹配的。
在终端使用qmake，会显示

```bash
qmake: could not exec '/usr/lib/x86_64-linux-gnu/qt4/bin/qmake': No such file or directory
```

可以看到默认的qmake还是qt4。
编辑qmake的默认位置：

```bash
cd /usr/lib/x86_64-linux-gnu/qt-default/qtchooser
	# qtchooser可以进行qt版本和工具的配置运行
sudo vim defalut.conf
sudo mv default.conf default.conf_bak
	# 备份原本的conf，可以用ls看到，它是一个软链接，指向qt4-x86_64-linux-gnu.conf，现在要改成指向qt5的。
sudo ln -s /usr/share/qtchooser/qt5-x86_64-linux-gnu.conf default.conf
cd  /usr/share/qtchooser
sudo vim qt5-x86_64-linux-gnu.conf
    # 将里的面路径改成自己的， 如：
    #  /home/yehuohanxing/MyApps/Qt570/5.7/gcc_64/bin
    #  /home/yehuohanxing/MyApps/Qt570/5.7/gcc_64 
```

现在终端中执行qmke就可以了。


---
# *安装指纹识别驱动*

 - 跟个人电脑的硬件有关，我电脑支持指纹：

```bash
sudo add-apt-repository ppa:fingerprint/fingerprint-gui
sudo apt-get update
sudo apt-get install libbsapi policykit-1-fingerprint-gui fingerprint-gui

fingerprint-gui
    # 打开软件配置
    # 配置时，最一个Password的选项是将指纹加密文件放入U盘中的，不用配置
```


---
# *更改笔记本合盖、按电源键等设置*

 - 可以在“系统设置 -> 电源”中高设置；
 - 可以用systemd 处理某些电源相关的 ACPI 事件。 配置文件为 /etc/systemd/logind.conf， 其中：

```
# 事件
HandlePowerKey     : 按下电源键后的动作
HandleSleepKey     : 按下挂起键后的动作
HandleHibernateKey : 按下休眠键后的动作
HandleLidSwitch    : 合上笔记本盖后待机

# 值
ignore    ： 忽略
poweroff  ： 关机
reboot    ： 重启
halt      ： 关机
suspend   ： 待机挂起
hibernate ： 体眠
```

修改完后合使用下列命令生效：

```bash
sudo systemctl restart systemd-logind
```

---
# *安装zsh shell*
* 首先安装zsh

``` bash
sudo apt-get install zsh
```
* 改用zsh

``` bash
chsh -s /usr/bin/zsh
```

* 安装on-my-zsh(它是一个zsh的配置，正因为有这个配置，zsh使用起来才无比的方便，当然，也可以自己来配置zsh)

```bash
# 通过curl安装
curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh

# 通过wget安装
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh
```

* 相关教程
[zsh的TAB补全说明，当然还有其它的一些快捷用法说明](http://wulfric.me/2015/08/zsh/)
[zsh的配置说明，即～/.zshrc文件，讲得很详细](http://blog.csdn.net/ii1245712564/article/details/45843657)
[别一个zsh配置说明](http://www.cnblogs.com/ma6174/archive/2012/05/08/2490921.html)
