---
title: 软件应用之 IAR
categories:
  - 杂记
date: 2017-06-17 22:19:01
tags: IAR
mathjax : true
---


IAR使用技巧记录。

<!-- more -->

---
# IAR相关设置
 - 中心字体乱码 或 有中文时不能显示为Courier New字体
改 Tools-Options-Editor，选择 system，去掉 Auto-detect charater encoding

 - Go to Definition是灰色的
Tools-Options-Project，勾选Generate browse information


---
# map memory
 - readonly code memory : 代码量(Flash)
 - readonly data memory : 常量(RAM)
 - readwrite data memory : 变量(RAM)


---
# IAR常用环境变量

| 变量           | 说明                       |
| :---:          | :---:                      |
| \$CUR_DIR\$    | 当前目录                   |
| \$CUR_LINE\$   | 当前行                     |
| \$EXE_DIR\$    | 输出可执行文件目录         |
| \$FILE_BNAME\$ | 无扩展名的文件名           |
| \$FILE_BPATH\$ | 无扩展名的完整路径         |
| \$FILE_DIR\$   | 已激活文件的目录，无文件名 |
| \$FILE_FNAME\$ | 无路径的已激活文件名       |
| \$FILE_PATH\$  | 已激活文件的完整路径       |
| \$PROJ_DIR\$   | 项目目录                   |
| \$PROJ_FNAME\$ | 无路径的项目名             |
| \$PROJ_PATH\$  | 项目文件的完整路径         |
