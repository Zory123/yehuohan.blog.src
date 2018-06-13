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

---
# 编译相关
 - 出现找不到obj之类的问题时，删除构建文件夹再试。


---
# Pro(qmake)配置

## ‘$$’操作符

 - 获取变量名内容，使用$$或$${}

```
hppfile = $$HEADERS
curpath = $${PWD}/debug_dir
message($$hppfile)
message($$curpath)
```

 - 传递built-in函数参数或获取结果，使用$$或$${}

```
PicFile = "pic.jpg"
Result = $$absolute_path($$PicFile)
PicName = "pic"
Result = $${absolute_path($${PicName}.jpg)}
message($$Result)
```

 - 获取qmake属性，使用$$[]

```
qtver = $$[QT_VERSION]
message($$qtver)
```

 - 获取系统环境变量，使用$$()

```
syspath = $$(PATH)
message($$syspath)
```

 - 在Makefile中获取变量名，使用${}

```
DESTDIR = $${OBJECTS_DIR}
#执行qmake时，就将pro文件中的OBJECTS_DIR赋给DESTDIR

DESTDIR = ${OBJECTS_DIR}
#执行make时，才将Makefile中的OBJECTS_DIR赋给DESTDIR
```

 - 在Makefile中执行的命令

```
# 用``括起来，在Makefile中就是执行shell命令
LIBS += `pkg-config --libs `
```

## 条件域

```
# <condition> {
#}
unix: DEFINES += IS_UNIX
win32 {
    DEFINES += IS_WIN32
}
CONFIG (debug, debug|release){
    DEFINES += IS_DEBUG
} else {
    DEFINES += IS_RELEASE
}
message($$DEFINES)
```


## 常用built-in函数

这里简单列几个常用的，具体参考： [Replace Functions](http://doc.qt.io/qt-5/qmake-function-reference.html)和[Test Functions](http://doc.qt.io/qt-5/qmake-test-function-reference.html)

```
# 按pattern获取文件名
Result = $$files($${PWD}"/dpm/src/*.cpp")

# 添加双引号，和直接用""一样
Result = $${PWD}$$quote(/test src/*.cpp))

# 移除相同元素
ARGS = 1 2 3 2 5 1
Result = $$unique(ARGS)

# 遍历元素
Result = core imgproc
for(lib, Result){
    Result +=-lcv_$${lib}d
}

# 改变大小写
Result = $$upper($$Result)
Result = $$lower($$Result)

# 替换字符串
Result = "en, hello qt"
Result = $$replace(Result, hello qt, hi qmake)
```

## LISB和INCLUDEPATH示例

```
# INCLUDEPATH
unix:INCLUDEPATH += "/home/user/extra headers"
win32:INCLUDEPATH += $$quote(C:/Program Files (x86)/Windows Kits/8.1/Include/winrt)

# LIBS
win32:LIBS += "C:/mylibs/extra libs/extra.lib"
unix:LIBS += "-L/home/user/extra libs" -lextra
LIBS += \
    -L$$"C:/Program Files (x86)/Windows Kits/8.1/Lib/winv6.3/um/x64" \
    -lUser32
```

---
# Windows下QtCreator使用

## VS添加Qt
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

## 添加CDB
 1、在[官方](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/index)下载CDB，选择"As a standalone tool set"中的在线下载包sdksetup.exe。
 2、打开sdksetup，只选择"Debugging Tools for Windows"下载即可。
 3、在下载的文件中找到X64 Debuggers And Tools-x64_en-us.msi和X64 Debuggers And Tools-x86_en-us.msi安装。
 4、之后就可以在QtCreator中配置CDB调试器了，此外，安装qt时，最好一并安装源码包。
