---
title: ubuntu16.04安装opencv3.1.0+Qt5.6.0
categories:
 - 笔记
date: 2017-06-09 00:11:05
tags: 
 - ubuntu
 - opencv
 - qt
---



---
# 安装依赖的库

```bash
sudo apt-get install build-essential
	# 必须的，gcc编译环境
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
	# 必须的,包括cmake等工具
	
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
	# 可选的，看个人需要，总共5M左右
```

<!-- more -->

---
# 下载源码
 - 在官网下载：http://opencv.org/downloads.html
 - 或着用git clone：

```bash
cd ~/opencv310
	# opencv310为自己建的，源码将放在这里
git clone https://github.com/Itseez/opencv.git
git clone https://github.com/Itseez/opencv_contrib.git
```

---
# 使用cmake安装
 - 解压源码包，得到opencv-3.1.0 （用git的话，即是opencv310）
 - 然后建立编译目标文件夹

```bash
cd opencv-3.1.0
mkdir build
```

 - 使用cmake或着用cmake-gui生成Makefile
  (1) cmake方式

```bash
cd opencv-3.1.0/build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
	# 生成后的Makefile在build文件夹中，而需要的CMakeLists.txt在 ".."中，即上一级文件夹中（opencv-3.1.0）
```

  (2) cmake-gui方式
  cmake-gui即cmake和图形界面版程序：
  先安装cmake-gui

```bash
sudo apt-get install cmake-qt-gui
```

然后打开cmake-gui：
{% asset_img 01.png %}
"/opencv-3.1.0" 和 "/opencv-3.1.0/build"换成自己的，然后先点  Configure 然后点 Generate。

<font color=red>
在Configure过程中，若出现
-- ICV: Downloading ippicv_linux_20141027.tgz...
。。。。
则下载 [ippicv_linux_20141027.tgz](http://download.csdn.net/detail/yehuohan/9511463)，替换掉 opencv-3.1.0/3rdparty/ippicv/downloads/linux-8b449a536a2157bcad08a2b9f266828b 下的同名文件即可，注意替换后，重新编译，或着一开始就放进去
</font>


---
# 安装OpenCv
在opencv3.1.0/build下，终端运行：

```bash
make -j7
	# 7个线程编译
sudo make install
	# 安装
```


---
# opencv程序编写实例
 - 建立文件夹test
 - 编写test.cpp

```c++
#include <opencv2/opencv.hpp>		// 注意：使用"/"，和windows不同
#include <iostream>
#include <string>
using namespace cv;
using namespace std;
int main()
{
	Mat img = imread("pic.jpg");
	if(img.empty())
	{
		cout<<"error";
		return -1;
	}
	imshow("mypic",img);
	waitKey();
	return 0;
}
```

---
## 1:用CMake生成OpenCv工程
 -  编写CMakeLists.txt

```bash
cmake_minimum_required(VERSION 2.8)					# CMake工具最低版本要求

project(test)										# 工程项目名,编译出来的可执行文件名字

aux_source_directory(. SRC_LIST)					# 源文件列表

#include_directories(./header/)						# 头文件目录

#link_directories(/usr/local/lib)					# 库文件的目录

add_executable(${PROJECT_NAME} ${SRC_LIST})			# 工程项目名和我们要编译的文件名

IF (UNIX)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")	# gcc添加支持c++11
ENDIF (UNIX)

IF (WIN32)
	set(OpenCV_DIR D:/opencv310/build)				# windows下设置OpenCv的路径，路径不是默认地址时，需要自行更改
ENDIF(WIN32)
find_package(OpenCV REQUIRED)						# 搜索指定的外部依赖库头文件和库文件

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})	# 链接到OpenCV库
```

 - 编译程序

```bash
# 目录结构：
# test - text.cpp			//cpp文件
#	   - CMakeLists.txt     //cmake生成文件
#	   - pic.jpg            //测试图像
cd test
cmake .
	# 生成makefile， “.”表示在当前目录生成
make
	# 编译
./test
	# 运行程序
```

---
## 2:用Qt作为IDE环境生成opencv工程
 - 配置qt的cmake构建方案（需要安装cmake）：
 1、打开Qt，找到 “工具->选项->构建和运行->构建套件"，如下图设置：
{% asset_img 02.png %}
 其中cmake安装好，Qt会自动配置好 "CMake" 参数的

 2、开始新建opencv工程
 新建工程 - 选择Non-Qt project 然后先Plain C++ Application
{% asset_img 03.png %}

 3、然后下一步
{% asset_img 04.png %}

4、 选择CMake
{% asset_img 05.png %}

5、只选择刚配置的构建套件
{% asset_img 06.png %}

6、点完成
{% asset_img 07.png %}

7、会出现下图对话框，点  “执行CMake"  就可以点 ”完成“ 了
{% asset_img 08.png %}

8、然后编定main.cpp和CMakeLists.txt文件，CMakeLists.txt要增加最后两行代码
{% asset_img 09.png %}
然后运行即可出结果，这里要注意的是，如果使用了"影子构建"（即项目构建生成的文件单独放在一个文件夹中，如build-untitled-Console_GCC_32bit_with_cmake-Default这样的文件夹），则生成的可执行文件也在build-untitled-Console_GCC_32bit_with_cmake-Default文件夹中，上述代码要想显示出图像，就需要将图片文件pic.jpg放在此文件夹中。

9、其实，也可以在Qt中直接 Open Project，然后选择打开CMakeLists.txt，就可以从第5步开始配置项目，过程一样的。


---
## 3:用Makefile生成opencv工程
 - main.cpp使用之前的即，建立如下Makefile文件

```bash
#Makefile

#使用g++编译，且以C++11标准
CXX = g++ -Wall -std=c++11

#opencv需要的参数
CFLAGS =`pkg-config opencv --cflags` `pkg-config opencv --libs`
#只使用上面这一名，会提示"libippicv.a"这个库找不到，所以自己添加上
UFLAGS = -L /usr/local/share/OpenCV/3rdparty/lib/ -l ippicv

#可执行文件名称
TARGET = main

#源文件
SOURCE = main.cpp

TARGET:
	$(CXX) -o $(TARGET) $(SOURCE) $(CFLAGS) $(UFLAGS)
```
- 然后make，即可编译，接着就可以运行了


---
## 4:用qmake生成opencv工程
qmake需要编写pro文件，如下test.pro：

```bash
# app工程
TEMPLATE = app

# 文件名称
TARGET = test

# 配置,添加pkg-config工具
CONFIG += \
	console \
	link_pkgconfig

# 添加opencv的库
PKGCONFIG += opencv

# 添加opencv第三方库ippicv
LIBS += -L /usr/local/share/OpenCV/3rdparty/lib -lippicv
	
# 源文件
SOURCES += \
	main.cpp
```

然后用如下命令

```bash
qmake test.pro
	# 会生成makefile
make
./test
	# 编译完成，即可运行
```

有了pro文件，也可以用qt creator打开工程，然后同样可以运行。
同时，也可以使用qt creator建立plain c++项目，使用qmake，然后改pro文件。
