---
title: Ubuntu16.04搭建LAMP架构服务器
categories:
  - 杂记
tags:
  - ubuntu
  - lamp
date: 2017-06-09 00:21:01
---


LAMP = Linux+Apache+Mysql/MariaDB+Perl/PHP/Python
<font color=red> 
***纯属好玩，不涉及高深技术*** 
</font>


<!-- more -->

# 安装Apache2
 - 安装代码

```bash
sudo apt-get install apache2
```

 - 更改默认目录

```bash
sudo vim /etc/apache2/apache2.conf
	# 将 <Directory /var/www/>
	# 改成 <Directory "你的目录">
	# 可以将/var/www 中的默认网页复制到 你的目录 中
sudo vim /etc/apache2/sites-available/000-default.conf
	# 将 DocumentRoot /var/www/html
	# 改成 DocumentRoot "你的目录"
sudo /etc/init.d/apache2 restart
	# 重启
```

- 测试
在浏览器中输入："http://localhost" 或 "http://127.0.0.1" ，
可以看到下图：
{% asset_img 01.png %}


# 安装PHP
 - 安装代码

```bash
sudo apt-get install php7.0
	# ubuntu16.04中没有php5了，直接装7吧
sudo apt-get install libapache2-mod-php7.0
	# 配置APACHE+PHP7的
sudo apt-get install libapache2-mod-php
	# 这个应该是配置APACHE+PHP5的，一块装吧
sudo /etc/init.d/apache2 restart
	# 重启
```
- 测试php文件

在 “你的目录”下建一个testphp.php
```php
hello php
<?php
phpinfo();
?>
```

- 测试效果
在浏览器中输入 "http://127.0.0.1/testphp.php" ，
可以看到：
{% asset_img 02.png %}


# 安装MySql
 - 在终端：

```bash
apt-get install mysql-server mysql-client
	# 安装时会要求输入mysql管理员密码，输入即可

apt-get remove --purge mysql-server
apt-get remove autoremove
	# 卸载时要带--purge，连同配置文件一同卸载，不然会出错
```

注意：
```
mysql-server ： 用来创建和管理数据库实例，提供相关接口供不同客户端调用;
mysql-client ： 操作数据库实例的的一个命令行工具，像图形化界面工具有phpmyadmin等;
mysqld       ： 即MySQL server
mysql        ： 即mysql-client客户端命令行工具
```

- 附mysql服务管理命令

```bash
/etc/init.d/mysql stop/restart/start

service mysql stop/restart/start
	# 两条令相同
```

管理mysql的自启，还要改/etc/init/mysql.conf文件，将start的级别注掉，stop的级别改成0123456，才能禁用自启

- 推荐自启管理工具

```bash
apt-get install sysv-rc-conf
```


