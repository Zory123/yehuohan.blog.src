---
title: 软件应用之 AltiumDesigner
categories:
  - 杂记
date: 2017-06-17 00:24:49
tags: Altium Designer
---

Altium Designer使用记录，主要是快捷键操作等技巧。

<!-- more -->


---
# 快捷键
```
~                            : 显示正在使用命令的相关快捷键
Ctrl + MouseLeftMove(SCH)    : 拖曳
Ctrl + MouseLeftClick        : 高亮显示点击的连线网络
Ctrl + MouseLeftDoubleClick  : 取消高亮显示点击的边线网络
Shift + S                    : 单层模式（只显示单层）
Shift + C                    : 去掉过滤，取消选择
Ctrl + D                     : 快速设置需要显示或隐藏的元素(Layer,Fill...etc)
Ctrl + L                     : 快速设置Layer显示等
Ctrl + UpDownLeftRight-Arrow : 用小键盘移动元件
Ctrl + MouseLeftMove(PCB)    : 以最小间隔移动，且不会受到“自动吸附到网格”的影响
Ctrl + G                     : 自定义设置网格间距
Ctrl + Shift + MouseWheel    : 切换当前图层
```

---
# 技巧
 * PCBFile布线前，先设置好基本的Rules；
 * 放置元件时慎用X、Y镜像，元件的焊接点若不是对称的，可能造成元件管脚和板对不上；同时，会造成3D模型的显示与设想的不一致；
 * 改过布线后，要Rebuild Polygon plane；
 * Polygon plane连拉GND后，DNG之间的连线不一定需要通过走线连接；
 * Polygon plane连拉GND后，DNG之间的Connections就不会显示了；
 * Polygon plane连拉GND后，将两元器件或其中一个(如单片机)管脚引出，打一个via，就能使元器件间管脚通过Polygon plane连接；
 * 移动元器件时，若元器件挡信的Keet-out Layer，可以在Ctrl+D中设置Pads透明
 * 总线式布线：通俗的讲就是多条网络同事布线的问题。具体方法是，按住SHIFT，然后依次用光标移到要布线的网络，点击鼠标左键即可选中一条网络，选中所需的所有网络以后，单击工具栏汇的总线布线图标，在被选网络中任意单击即可开始多条网络同时布线。布线过程中可以按键盘上左右尖括号<>调节线间距。
 * 等长布线（即走S型线）：走线属于不同Net时，可以Add Class；走线都属于同一个Net，则可以建多个temp-Net，布好等长线后，再复制到目标Net。



---
# 参数
 - 孔径优选系 

| type           | 1     | 2     | 3     | 4     | 5     |
| ---            | ---   | ---   | ---   | ---   | ---   |
| 孔径           | 24mil | 20mil | 16mil | 12mil | 8mil  |
| 焊盘直径       | 40mil | 35mil | 28mil | 25mil | 20mil |
| 内层热焊盘尺寸 | 50mil | 45mil | 40mil | 35mil | 30mil |

 - 板厚与最小孔径

| type     | 1     | 2     | 3     | 4     | 5     |
| ---      | ---   | ---   | ---   | ---   | ---   |
| 板厚     | 3.0mm | 2.5mm | 2.0mm | 1.6mm | 1.0mm |
| 最小孔径 | 24mil | 20mil | 16mil | 12mil | 8mil  |
