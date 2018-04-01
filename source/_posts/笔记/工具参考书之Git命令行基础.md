---
title: 工具参考书之Git命令行基础
date: 2017-06-05 23:34:57
tags: git
categories: 
 - 笔记
---

---
# Git原理初探
这里就不详细说了，百度谷歌随便搜。当然，搜到的解释都大同小异，基本会说到：

 - Git是一个分布式版本控制软件
 - Git的本质是一套内容寻址文件系统

当然，理解这些话就不用多说了。不理解且不想努力去理解的话，就看Git有没有自己需要的功能和作用。
我现在就是用Git作为一个管理工项目版本的软件来使用，同时，也作为一个备份工具来使用。以后，不管是工作项目有其他人加入，或是进行项目交接，都可以用Git来作为一个桥梁。 
首先在这里放一个不错的教程：
[oschina上的一个教程](http://git.oschina.net/progit/)


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

 - Linux下安装：
 Linux(以Ubuntu为例)安装很简单，就是一条命令的事：

```bash
sudo apt-get install git
```

 - Windows下安装：
 windows下使用Git的话，得先装一个类unix环境，如mingw等。可以按照下列教程链接来安装，然后同样一条命令就可以安装Git。
{% post_link 笔记/Windows搭建类UNIX环境-Msys2-MinGW-w64 %}

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
## 仓库的建立与提交

* init

```bash
git init            
# 在当前文夹初始化git，当前文件夹即为WorkSpace区，且会建立.git文件夹
git init test
# 在test初始化git，且test为WorkSpace区
```

* status

```bash
git status
# 查看WorkSpace区和Index区状态，显示WorkSpace中有哪些修改，显示Index中有哪些提交。
git status -s (or --short)
# 查看简略的状态信息
```

* add

```bash
git add <file> (or .)
# 添加WorkSpace中指定文件或目录（或所有修改的文件，不包括delete的）到Index。
# 有多个文件或目录用空格隔开，如 "git add /file1 /dirA /dirB/fileB"

git add -all (or -A)
# 添加WorkSpace中所有修改到Index，包括delete的。
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


* commit

```bash
git commit -m "comments" (or 'comments')
# 将Index中的内容提交到Local，并添加备注信息（使用单引号，可以输入多行comments）。

git commit -m "comments" [-- /file /dir]
# 只提交指定文件或目录到Local，多个文件或目录用空格隔开
```

```bash
git commit --amend
git commit --amend -m "comments"
# 修改最一次提交的备注信息。
```

* checkout

```bash
git checkout [-- <path/file>(or .)]
# 从Index区指定恢复指定文件file（或所有文件）到WorkSpace
# 即相当于扔掉WorkSpace中自上次执行git add以来的修改，此命令会扔掉WorkSpace中修改，使用请慎重。
# 若是没有执行git add，则不会扔掉任何修改。
# 注意，两横线"--"不能少，这表示后面代表的是路径或文件，而不是分支名，因为checkout来可以用于分支的切换。

git checkout <branck-name> [-- path/file(or .)]
# 从分支<branck-name>的Local区恢复指定文件到当前分支的WorkSpace
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

* revert

```bash
git revert <commit_id>
# 撤消commit_id的更改，并将撤消操作当作一个新的提交
# 用下例来解释revert具体过程：
git revert HEAD~2
# 第1步：撤消HEAD~2的更改，此时只有WorkSpace的区内容变了。
#       （相当于在WorkSpace里“减去”HEAD~2的更改，但不会减去HEAD~1和HEAD的更改）
# 第2步：将第1步的操作提交，即相当于执行依次 git add 和 commimt

git revert -e <commit_id>
git revert --edit <commit_id>
# 为revert操作添加注释

git revert --no-edit <commit_id>
# 不添加注释，而是使用默认的注释信息

git revert -n <commit_id>
git revert --no-commint <commit_id>
# 进行完撤消操作后(前面例子中和第1步)，不自动提交
```

## 查看相关信息

* log

```bash
git log
# 查看所有的提交记录。
# 注意：Windows下使用Msys2显示gbk编码内容时会乱码，需要转码，如:
git log | iconv -f -gbk -t utf-8
```

```bash
git log [options] [-- <path/file>]
# log基本用法，<path/file> : 可以是一个目录 或 文件

git log
# 查看提交日志
git log <path/file>
# 查看关于file每次提交的记录
git log -p <path/file>
# 查看每次修改file的详细内容

git log --pretty=format:"<...>"
git log --pretty=format:%s
# 按照指定的格式 <...> 显示提交记录
# <...> 格式如下：
# %H      提交对象（commit）的完整哈希字串
# %h      提交对象的简短哈希字串
# %T      树对象（tree）的完整哈希字串
# %t      树对象的简短哈希字串
# %P      父对象（parent）的完整哈希字串
# %p      父对象的简短哈希字串
# %an     作者（author）的名字
# %ae     作者的电子邮件地址
# %ad     作者修订日期（可以用 -date= 选项定制格式）
# %ar     作者修订日期，按多久以前的方式显示
# %cn     提交者(committer)的名字
# %ce     提交者的电子邮件地址
# %cd     提交日期
# %cr     提交日期，按多久以前的方式显示
# %s      提交说明
```

```bash
git reflog
# 显示Local所有分支的commit,包括已经通过reset --hard撤销的commit
```
* diff

```bash
# 两个diff的基本用法
git diff [options] <commit1> <commit2> [-- <path/file>]
git diff [options] <branch1> <branch2> [-- <path/file>]
# 省略commit2或branch2，则是与当前所在的WorkSpace区比较
# commit和branch全部省略，则与比较当前所在的WorkSpace区和Index区
# [-- <path/file>] : 此部分参数是为了比较某个文件 或 目录

git diff
# 查看WorkSpace区和Index区差异，即显示WorkSpace中未add到Index中的修改
git diff --stat 
# 列出WorkSpace区中相对Index区更改的文件列表
git diff <path/file>
# 查看WorkSpace区file有哪些修改
git diff HEAD^n [-- <path/file>]
# 查看WorkSpace区和HEAD^n版本的差异
git diff <commit_id1> <commit_id2> [-- <path/file>]
# 查看两个commit版本的差异
git diff --stat <branch1> <branch2> [-- <path/file>]
# 列出两个分支的不同的文件列表
git show <commit-id>
# 直接查看某次commit的修改内容
```

---
# Git远程仓库管理
远程仓库管理的命令，即关于Local与Remote之间的命令。

* clone

```bash
git clone <url>
git clone <url> test
# 从Remote克隆一个版本仓库到当前文件夹（或test文件夹）
git clone --depth 1 <url>
# 使用depth指定克隆深度，这里表示只克隆最后一次commint

git init --bare test.git
# 建立一个祼库，test.git文件夹即为.git的内容，没有WorkSpace区
git clone test.git test
# 从本地test.git克隆到test；
# test文件夹即相当于WorkSpace区，在test中可以进行status, add, commit, push, pull等操作，
# push即推送到test.git中，同样pull也是从test.git中拉取
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
# 注意，切换后，分支name的WorkSpace中未commit的更改会扔掉
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

---
# Git暂存管理

>这里的暂存(stash)不是前面所讲的暂存区/索引区(index)。

`stash`用于将当前WorkSpace区中的修改暂存起来，之后可以随时取出暂存的修改。

```bash
git stash
# 暂存当前WorkSpace区中的修改
git stash save "msg"
# 暂存当前WorkSpace区中的修改，且添加暂存信息msg
# 注：暂存后，当前WorkSpace就回到修改之前的状态
```

> stash的一些应用：
> - 切换到其它分支继续工作：不暂存直接切换，当前分支WorkSpace的修改全会扔掉；
> - `pull`当前分支，或`merge`其它分支到当前分支：当前分支有未`commit`的修改，是没法`pull`或`merge`的；

```bash
git stash list
# 查看所有的暂存
git stash show stash@{1}
# 查看1号暂存基本信息
# 省略 "stash@{1}" 则查看最后一次暂存
# zsh中"stash@{1}" 可以直接写成 "1"
git show stash@{0}
# 查看0号暂存详细信息
```

```bash
git stash apply stash@{1}
# 应用1号暂存到当前WorkSpace区(暂存示删除)
git stash drop stash@{1}
# 删除1号暂存
git stash pop stash@{1}
# 取出1号暂存到当前WorkSpace区（相当于先apply再drop）
# 以上三条命令，省略 "stash@{1}" 则表示对最后一次暂存操作

git stash clear
# 清除所有暂存
```
> 注意：`apply`或`pop`暂存时，若有冲突，需要手动修改

比如如下操作，`stash`当前WorkSpace中的修改，然后`pull`当前分支，之后再`pop`回当前WorkSpace。一般不会有什么冲，但若是`stash`的修改，和`pull`下来的更新，对同一处代码进行了修改，就会产生冲突，在代码文件中会出现如下内容（搜"<<<<<<<"即可找到所有的冲突）：

```text
<<<<<<< Updated upstream
    if IsTermType("xterm") || IsTermType("xterm-256color")
=======
    if IsTermType("xterm") || IsTermType("vt")
>>>>>>> Stashed changes
```

这时，就要手动从"Updated upstream"和"Stashed changes"中选一个了，因为git不知道，到底哪个修改才是你想要的。


---
# Git子模块管理

当一个项目比较大时，管理起来就很麻烦，比如一个项目的结构如下：

```text
project
    |-- docs       : 工程文档
    |-- pcb        : pcb工程
    |-- dsp        : 单片机程序
    |-- sim        : matlab仿真文件
    |-- misc       : 杂项文件
```

项目不但大，且内容也杂，commit的注释信息都不好写。这种时候，使用子模块`submodule`管理就方便多了。
首先理清几个要点(以用户`https://github.com/user`为例)：
 - project为父项目，docs, pcb, dsp, sim, misc等为子项目；
 - 父项目有独立的仓库，为`https://github.com/user/project`；
 - 子项目有独立的仓库，为`https://github.com/user/docs`，其它的类似；
 - 父项目**不记录**子项目的内容，只记录子项目的一个commit；

## add子模块

```bash
cd project
git submodule add https://github.com/user/docs
# 将docs添加为project的子项目，会新建.gitmodules文件docs文件夹
# 在.gitmodules中包含了子项目docs的路径和url
# docs文件夹是子项目对应commit的克隆（不一定是最新的版本）
```

添加子模块后，再push到github，可以看到docs文件夹后标标了一个commit-id，这即是子项目的一个commit-id，但不一定是子项目最新的commit版本，如下图：

![sub1](sub1.png)

此时将父项目clone下来（子项目也一并clone），子项目docs的对应的版本就是commit-id(`49fcdac`)对应的内容，即使docs有更新的版本。
在`project/docs`进行了更改，并push到子项目后，在project下执行`git diff`可以看到如下比较结果：

```diff
diff --git a/docs b/docs
index 49fcdac..28ea4cb 160000
--- a/docs
+++ b/docs
@@ -1 +1 @@
-Subproject commit 49fcdac59acfceb1ea60d7d73652a00ee1d2510a
+Subproject commit 28ea4cbe88d5a4fa7b730cde663aae6a174d322d
```

可以看到，父项目中只显示了子项目的最新版本commit-id的变化。


## clone父项目

```bash
git clone git@github.com:user/project.git --recursive
# 方法一：recursive参数会递归的clone整个项目，所有子项目也会clone下来

git clone git@github.com:user/project.git
cd docs
git submodule init
git submodule update
# 方法二：先clone父项目，在逐个更新submodule
```


## pull子项目

```bash
git submodule foreach [--recursive] <command>
git submodule foreach --recursive git pull
# 方法一：使用submodule foreach命令

cd docs
git pull
# 方法二：逐个pull子项目即可
```

## delete子项目

```bash
git rm --cache docs
# 删除对docs的track
rm -rdf docs
# 删除docs文件夹
vim .gitmodules
# 删除.gitmodules中的docs的信息，如果要删除所有子项目，则直接 rm .gitmodules即可
vim .git/config
# 删除config中的docs的信息
# 最后push即完成了子项目的删除
```
