---
title: Ubuntu16.04配置ftp服务器
categories:
  - 杂记
tags:
  - linux
  - ftp
date: 2017-06-09 00:31:28
---


---
# 安装vsftpd
使用下列命令安装

```bash
sudo apt-get install vsftpd
```

安装完后，ftp的配置文件在

```
/etc/vsftpd.conf
```

<!-- more -->

可以使用下列命令来打开，关闭，重启ftp服务

```bash
sudo /etc/init.d/vsftpd start
sudo /etc/init.d/vsftpd stop
sudo /etc/init.d/vsftpd restart
```

使用下列命令，可以看到系统中多了ftp用户组和ftp用户

```bash
cat /etc/group
cat /etc/passwd
```

ftp服务器的目录位置在 /srv/ftp， 这也是匿名用户访问时的根目录。
可以使用下列命令来间接更改目录

```bash
cd /srv
sudo rm -d ftp
cd ~/
mkdir ftp
sudo ln -s ftp /srv/ftp
```

---
# 配置vsftpd.conf
编辑/etc/vsftpd.conf文件:

```bash
# 允许匿名用户和本地用户登录，本地用主户即/etc/passwd中的用户
anonymous_enable=YES
local_enable=YES

# 禁止全局写命令
write_enable=YES

# 禁止匿名用户上传和创建文件夹
anon_upload_enable=NO
anon_mkdir_write_enable=NO

# 只允许userlist的用户登录
userlist_enable=YES
userlist_deny=NO
userlist_file=/etc/vsftpd.user_list

# 注意：使用了vsftpd.user_list后，要在其中加入anonymous才能使用匿名用户登录，如以下内容，表示只有匿名用户和名为ftp的用户，以及本地用户ubuntu可以登录
anonymous
ftp
ubuntu

```


---
# 匿名用户登录
在/srv/ftp下建立pub用于匿名用户上传的文件，并更改其权限

```bash
cd /srv/ftp
sudo mkdir pub
sudo chown ftp:ftp pub
```

然后用手机或电脑以匿名用户登录到ftp服务器，在浏览器中 或者 在文件浏览器的“连接服务器” 中输入下列地址，即可看到ftp服务器的目录(如果只是想看下，可以先使用匿名用户登录试下)

```bash
ftp://localhost
#或
ftp://127.0.0.1
```

可以看到根目录即是/srv/ftp目录：
{% asset_img 01.png %}
然后，进入到pub目录，上传一个文件夹或文件，这里我用的机上传了一个文件夹make_by_meizu，然后在ubuntu终端中查看手机上传的文件夹的详细信息：
{% asset_img 02.png %}
可以看到make_by_meizu的用户即用户组为ftp:ftp，所以ftp匿名用户即是以默认建立的ftp用户登录的，所以匿名用户要在pub上传文件或目录，pub的用户要为ftp。

---
# 本地用户登录
这里用ftp命令使用本地用户登录：

```bash
ftp localhost
ubuntu		#  输入本地用户名，匿名用户时，输入 anonymous，密码不输即可
xxxxx		#  输入本地用户密码
ls /		#  显示根目录
```
