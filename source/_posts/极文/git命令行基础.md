---
title: git命令行基础
date: 2017-06-05 23:34:57
tags: git
categories: 
 - 极文
---

---
# Git原理初探
这里就不详细说了，百度谷歌随便搜。当然，搜到的解释都大同小异，基本会说到：

 - Git是一个分布式版本控制软件
 - Git的本质是一套内容寻址文件系统

当然，理解这些话就不用多说了。不理解且不想努力去理解的话，就看Git有没有自己需要的功能和作用。
我现在就是用Git作为一个管理工项目版本的软件来使用，同时，也作为一个备份工具来使用。以后，不管是工作项目有其他人加入，或是进行项目交接，都可以用Git来作为一个桥梁。 


<!-- more -->


## Git工作流程
利用Git来工作，那我们就必须要清楚Git的工作流程。不然，项目文件被自己莫名其妙地删光了都没地哭去。
一般来说，在我们计算机上，为了让一个工程项目比较好管理和分类，我们会将关于项目的所有资料都放在一个目录中，我们将这个目录暂称为目录A。然后，当我们的项目有一个阶段性成果，或是想要对项目进行较大地改动时，我们会将目录A进行备份，传统做法就是将目录A全部打包压缩，然后重命名，带上“BAK+时间”之类的字样，随着备份文件的增多，我们将所有的压缩包又重新放在一个目录下，我们估且称之间目录B。最后，为了备份更保险，我们将目录B全部上传到一个网盘中。
{% asset_img 01.png %}
现在我们来了解一下使用Git工作的基本目录结构，首先，我们要对以下4个术语有一个基本认识：

 - 工作区(WorkSpace)
    工作区，顾名思义，就是我们的工程目录。我们进行的工程的创建、修改和维护都在此目录中。也即前述的目录A。

 - 索引区/暂存区(Index)
    索引区可以理解为是对工程项目修改的记录，在备份前，我们得需要知道哪些地方修改了。索引区就是记录一次备份有哪些地方修改了。

 - 本地仓库(Local)
    本地仓库就是我们存放项目备份的地方，也是前述的目录B。索引区和本地仓库全部放在工作区下的.git目录中。
    通过目录前的介绍，可以知道，即是离线状态，git也能对工程项目进行管理。

 - 远程仓库(Remote)
   远程仓库毫无疑问，就是相当于前述中的网盘了。而Git使用是专用的Git服务器平台。

4个术语的基本关系如下图:
{% asset_img 01.jpg %}

## Git服务器平台
常用的Git服务器平台有Github,Gitlab,oschina,coding.net等。Git平台选用哪个看自己，自己觉得哪个适合自己就用哪个，这里不详细介绍各个平台，只基本的对上述四个进行比较。
 
 - [Github](https://github.com/)
    基本上说上Git平台，首先想到就是这个，好多开源项目都托管在Github。但Github私有仓库需要收费，而且因为是国外的，速度不比国内的Git平台。

 - [Gitlab](https://about.gitlab.com/)
    Gitlab也是国外的，但支持无限的公有仓库和私有仓库。

 - [OsChina](http://git.oschina.net/)
    OsChina是国内的，一个帐号可以创建1000个项目，包括公有仓库和私有仓库。对于要求速度和私有仓库的，OsChina是个不错的选的。

 - [Coding.net](https://coding.net/)
    Coding.net与OsChina有点类似，也是国内的，速度快，同样支持1000个项目。

使用哪个就看自己的需要吧，如果需要建立私有仓库，选一个国内的还是不错的。 


---
# Git安装与配置
## Git安装
Git现在也有不少Gui程序，我还建议使用git命令行工具，不是为了所谓的装逼。使用git命令行更加容易理解git的工作原理和流程，而且，使用git命令行可定制空间更大。

 - Linux下安装：Linux安装很简单，就是一条命令的事：

```bash
sudo apt-get install git
```

 - Windows下安装：windows下使用Git的话，得先装一个类unix环境，如mingw等。可以按照下列教程链接来安装，然后同样一条命令就可以安装Git。
[Windows下搭建类UNIX环境 : Msys2+MinGW-w64](http://blog.csdn.net/yehuohan/article/details/52090282)

## Git坏境设置
这里说是Git环境设置主要是关于在windows的编码设置，因为windows使用gbk编码，而git服务器是utf-8编码，不设置编码的转换，容易乱码。

 - 用户信息高设置

```bash
    git config --global user.name <name>
    git config --global user.email <email>
    # 这是设置用户和邮箱等基本信息
```

 - git编码设置

```bash
    git config --global i18n.commitEncoding utf-8
    git config --global i18n.logOutputEncoding gbk
    echo 'LESSCHARSET=utf-8' >> /etc/profile 
    git config --global core.quotepath false
    # 设置提交到远程Git仓库时使用utf-8编码。windows下git输出log时使用gbk编码，同时，windows下git输出status不会乱码。Linux下可以不用此项设置。
```

## 建立Git仓库
假定已经注册好一个git平台的帐号，这里以oschina为例。建立一个git仓库前，首先要设置SSH密钥，这样进行git上传时，本地计算机和git平台间才能使用ssh安全连接。

### 设置SSH密钥
设置SSH密钥基本过程就是，在本地计算机生成rsa公钥和私钥，然后将rsa公钥填入git平台帐号。
首先行成rsa密钥，一个命令即可：

```bash
ssh-keygen -C <comment> -t rsa
    # 公钥：id_rsa.pub
    # 私钥：d_rsa
```

将生成的公钥填入git平台帐号即可。然后更改私钥名称。建立一个配置文件，然后写入以下内容即可：

```bash
# 文件：~/.ssh/config
Host git.oschina.net
IdentityFile ~/.ssh/id_rsa_oschina
```

最后，测试SSH是否可以使用，键入命令：

```bash
SSH -T git@git.oschina.net
```

 出现"Welcome to Git@OSC, yourname"即代表可以连接。

### Git仓库的建立与使用
按照以下命令，即可以完在从Git仓库建到上传的过程：

```bash
mkdir project       # project目录就是工作区
cd project          # 切换到project目录，进行git仓库建立
git init            # 初始化git，会建立.git文件夹
git add .           # 将所有的更改添加到Index索引区
git commit -m "msg" # 将所有的更改提交到Local本地仓库，Log信息为msg
git remore add origin_oschina git@git.oschina.net:<yourname>/project.git
                    # 建立Remote远程仓库，为origin_oschina
git push origin_oschina master:master
                    # 将本地master分支提同步到远程仓库的master分支
```

然后，有时候project有一些缓存文件或是临时文件，不需要进行git管理，这就需要".gitignore"文件来添加不需要管理的文件和目录，".gitignore"文件的基本规则如下：

```bash
## rules
/                   # 斜杆表示project目录
*                   # 通配符
?                   # 通配单个字符
[]                  # 包含单个字符的匹配列表
!                   # 表示不忽略匹配到的文件或目录

## example
*.log				# 忽略所有匹配*.log的文件和目录，包括子目录
*cache				# 忽略所有匹配*cache的文件和目录，包括子目录
/*                  # 忽略所有的文件和目录
!/README.md         # 跟踪README.md文件
!/src/              # 跟踪src下的所有文件和目录
!/inc/
/inc/*
!/inc/*.h
!/inc/*.hpp         # 只跟踪inc下的*.h和*.hpp文件
!/doc/
/doc/*
!/doc/files/        # 只跟踪doc/files目录
```

---
# Git本地命令
这里只是将常用的命令形式列出来，以达使用Git命令行工作的基本要求，注意是命令形式，不是详解每个命令。
本地命令主要讲WorkSpace, Index和Local之间的操作，包括添加修改，提交修改，回退版本等。
此外，开始阶段使用Git的时候，最好还是压缩备份，免得因为不熟悉命令操作，而造成不必要的后果。

* help

```bash
git help <command>
# 这个肯定是第一个要学会的，遇到问题就help。
```

* config

```bash
git config <--type>
# 设置工作环境变量
# --system: 配置文件在 /etc/.gitconfig
# --global: 配置文件在 ~/.gitconfig
# --local: 配置文件在 Project_Dir/.git/.gitconfig

git config --list
# 查看已有的配置信息
```

* init

```
git init            
# 初始化git，会建立.git文件夹
```

* status

```bash
git status
# 查看WorkSpace区和Index区状态，显示WorkSpace中有哪些修改，显示Index中有哪些提交。
```

* add

```bash
git add <file> (or .)
# 添加WorkSpace中指定文件（或所有修改的文件，不包括delete的）到Index。
```

```bash
git add -all (or -A)
# 添加WorkSpace中所有修改到Index，包括delete的。
```

* commit

```bash
git commit -m "comments" (or 'comments')
# 将Index中的内容提交到Local，并添加备注信息（使用单引号，可以输入多行comments）。
```

```bash
git commit --amend
git commit --amend -m "comments"
# 修改最一次提交的备注信息。
```

* checkout

```bash
git checkout -- <file>(or .)
# 从Index区指定恢复指定文件file（或所有文件）到WorkSpace
# 即相当于扔掉WorkSpace中自上次执行git add以来的修改，此命令会扔掉WorkSpace中修改，使用请慎重。
# 若是没有执行git add，则不会扔掉任何修改。
# 注意，两横线"--"不能少，这表示后面代表的是路径或文件，而不是分支名，因为checkout来可以用于分支的切换。
```

* reset

```bash
git reset <commit_id> [-- <path/file>(or .)]
# 从Local区中指定的提交版本commit_id恢复指定文件file（或目录）到Index
# 即相当于扔掉Index中git add添加的修改，此命令 !只! 会改变Index中的内容。
# 若省略commit_id，则是为最后一次的commit的id
```

```bash
git reset <mode> <commit_id>
# mode这里讲三个，分别为"--mixed, --soft, --hard"，其中"--mixed"为默认方式，
# "--mixed": Local区恢复到指定的commit_id版本，同时Index中的提交全部扔掉，但WorkSpace中的修改会保留
# "--soft" : Local区恢复到指定的commit_id版本，Index中的提交和WorkSpace的修改均会保留
# "--hard" : Local区恢复到指定的commit_id版本，同时Index和WorkSpace的修改全部扔掉，变成commit_id版本的内容
# 附： Local恢复到指定的commit_id版本后，在commit_id之后的提交也全部扔掉了

# "commit_id" : 可以通过git lot来查看，也可以使用 "HEAD^n" 表示，若省略，则为最后一次commit的id
# "HEAD"	  : 表示最后一次commit的id
# "HEAD^, HEAD~, HEAD^1, HEAD~1" : 均表示上 1 次commit的id
# "HEAD^n, HEAD~n" : 均表示上 n 次commit的id
# 附： windows下使用HEAD^表示时，需要用双引号括起来：
git reset --hard HEAD"^"2 (or "HEAD^2")
```

本地git命令间的基本关系：
{% asset_img 02.jpg %}

* log

```bash
git log
# 查看所有的提交记录。
# 注意：Windows下使用Msys2显示gbk编码内容时会乱码，需要转码，如:
git log | iconv -f -gbk -t utf-8
```

```bash
git log <path/file>
# 查看关于file每次提交的记录
git log -p <path/file>
# 查看每次修改file的详细内容
# <path/file> : 可以是一个目录 或 文件
```

```bash
git reflog
# 显示Local所有分支的commit,包括已经通过reset --hard撤销的commit
```
* diff

```bash
git diff
# 查看WorkSpace区和Index区差异，即显示WorkSpace中未add到Index中的修改
git diff <path/file>
# 查看WorkSpace区file有哪些修改

git diff HEAD^n [-- <path/file>]
# 查看WorkSpace区和HEAD^n版本的差异
git diff <commit_id1> <commit_id2> [-- <path/file>]
# 查看两个commit版本的差异
git diff <branch1> <branch2> [-- <path/file>]
# 查看两个分支的差异

# [-- <path/file>] : 此部分参数是为了比较某个文件 或 目录
```

* rm

```bash
rm <file>
# 删除文件，和git没有任何关系
git rm
# 删除git对file的追踪，同时删除WorkSpace中的file文件
git rm –cached <file>
# 删除git对file的追踪，但是不删除WorkSpace中的file文件
# 注意：如果想去除对文件或目录的追踪，除了更改.gitignore，还需要用git rm --cached删除追踪关系
```


---
# Git远程仓库管理
远程仓库管理的命令，即关于Local与Remote之间的命令。

* clone

```bash
git clone <url>
#从Remote克隆一个版本仓库到本地。
```

* remote

```bash
git remote add <name> <url>
# 添加远程库，例如：
git remote add origin_oschina git@git.oschina.net:username/project 
# 会使用OsChina的帐号username，添加一个远程序project，而origin_oschina就是远程库的名称。
```

```bash
git remote -v
# 显示所有远程库的名称和地址。

git remote rm <name>
# 删除远程主机。

git remote rename <name> <new name>
# 重命名远程主机。
```

* push

```bash
git push origin master:test
# 将本地master分支的更新，推送到远程主机origin的test分支。
# 如果省略test，则是从本地master分支推送远程master分支（最好养成写全本地分支与远程分支的习惯）。
```

```bash
git push --delete origin  master
git push origin :master
# 两条命令等价，均表示删除远程主机origin的master分支。
# 注意：删除的远程分支不能是默认分支
```

* fetch & merge

```bash
git fetch origin master
# 取回origin的master分支最新版本到origin/master分支上

git checkout origin/master
# 切换到fetch到的分支上，这时WorkSpace区就是origin/master的WorkSpace区的内容

git log -p test origin/master
# 查看具体的文件内容改变

git checkout test
# 回到本地test分支，会发现test的WorkSpace的内容仍在

git merge origin/master 
# 将origin/master合并到test分支，这时test的WorkSpace就变成origin/master的WorkSpace区内容
```

* pull

```bash
git pull origin master:test
# 取回远程主机origin/master分支，与本地test分支合并。
# 注意：此命令，会直接扔掉当前WorkSpace区的修改，即直接将origin/master合并到本地test分支上，使用请慎重
```


---
# Git分支管理

```bash
git branch
# 列出本地已经存在的分支，并且在当前分支的前面加"*"号标记。

git branch -r
# 列出远程支。

git branch -a
# 列出本地分支和远程分支。
```

```bash
git branch <name>
# 创建名为name的新分支
# 注意，创建后当前分支没有切换到name。

git checkout <name>
# 切换到分支name
```

```bash
git branch -d <test>
# 删除分支test
git branch --remotes -d <origin/test>
# 删除远程分支origin/test

git branch -m <name> <new name>
# 重命名分支。
```

---
# Git标签管理
标签（tag）是特定提交（commit)一个指针，也就是每个tag对应一个特定的commit。
Release是源码托管商对git的tag功能的增强，通过git提供的tag功能，可以给项目进行版本标识，添加编译好的二进制文件等。

```bash
git tag
# 查看所有标签

git tag <tagname> <commit_id>
# 创建轻量标签

git tag -a <tagname> -m <msg> <commit_id>
git tag -a v1.0.2 -m "Release version v1.0.2" HEAD~1
# 创建附注标签，保存更多的附注信息
# commit_id省略，则为最后一次提交

git tag -d <tagname>
# 删除标签
```

```bash
git show <tagname>
# 显示<tagname>的详细信息

git checkout <tagname>
# 切换到标签

git push origin <tagname>
# 推送标签到Remote区
git push origin --tags
# 将Local中的所有标签推送到Remote中
```
