---
title: 软件应用之 QtCreator
categories:
  - 杂记
tags: qt
mathjax: false
date: 2017-07-03 17:52:50
---

QtCreator使用记录。

<!-- more -->

# 编译相关
 - 出现找不到obj之类的问题时，删除构建文件夹再试。
 - 添加CDB
 1、在[官方](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/index)下载CDB，选择"As a standalone tool set"中的在线下载包sdksetup.exe。
 2、打开sdksetup，只选择"Debugging Tools for Windows"下载即可。
 3、在下载的文件中找到X64 Debuggers And Tools-x64_en-us.msi和X64 Debuggers And Tools-x86_en-us.msi安装。
 4、之后就可以在QtCreator中配置CDB调试器了，此外，安装qt时，最好一并安装源码包。

 

# Pro文件配置
 - 库LIBS设置：相对路径使用$$PWD，别用点。
 - LIBS和INCLUDEPATH示例：

```
# INCLUDEPATH
win32:INCLUDEPATH += "C:/mylibs/extra headers"
unix:INCLUDEPATH += "/home/user/extra headers"
INCLUDEPATH += $$quote(C:/Program Files (x86)/Windows Kits/8.1/Include/winrt)
INCLUDEPATH += $$OPENCV_DIR/include

# LIBS
win32:LIBS += "C:/mylibs/extra libs/extra.lib"
unix:LIBS += "-L/home/user/extra libs" -lextra
LIBS += \
    -L$$"C:/Program Files (x86)/Windows Kits/8.1/Lib/winv6.3/um/x64" \
    -lUser32

CV_LIB_NAMES = core imgproc highgui calib3d feature2d flann
for(lib,CV_LIB_NAMES){
    CV_LIBS_DEBUG +=-lopencv_$${lib}d
}
LIBS += -L$$OPENCV_LIB_DIR $$CV_LIBS_DEBUG
```
 
 
# VS添加Qt
 - qt vs addin设置：
 1、在vs中打开QT -> option
 2、add qt的位置，如：D:\Qt\Qt5.7.0\5.7\msvc2015_64
 3、添加环境变量：
 
```
 D:\Qt\Qt5.7.0\5.7\msvc2015_64\bin;
 D:\Qt\Qt5.7.0\Tools\QtCreator\bin;
```

 - vs添加assistan工具
 1、vs添加工具：vs-工具-外部工具，添加assistant.exe
 2、Qt5插件中添加assistant.exe：vs-工具-自定义-命令-菜单栏-Qt5，添加命令，找到 工具-外部工具9（第9个外部工具）

