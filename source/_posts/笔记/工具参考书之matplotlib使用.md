---
title: 工具参考书之Matplotlib使用
categories:
  - 笔记
mathjax: false
date: 2018-03-09 12:10:10
tags:
  - matplotlib
---


参考书籍：
[Matplotlib官方在线文档](https://matplotlib.org/)
[Matplotlib绘图实例](https://matplotlib.org/gallery.html)

---

[Matplotlib](https://matplotlib.org/)是一个Python的2D图形包，和[NumPy](http://www.numpy.org/)结合的非常好。

---
# 快速绘图

快速绘图，即直接调用[matplotlib.pyplot模块的函数](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)来绘图，为类似于的Matlab的函数式绘图。

## 基本绘图实例

```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Microsoft YaHei Mono'    # 设置中文字体
plt.plot([0,1,4,9,16,25], color='green', marker='*',
        linewidth=3, label="double")
plt.plot([0,5], [0,25], 'r-o',
        markersize=7, label="line")         # 绘制(x,y)数据点，x默为[0,1,2...]
plt.arrow(x=0, y=0, dx=0, dy=5, width=0.1)  # 绘制箭头
plt.annotate(r"$y=x^2$", xy=(3,8.5), arrowprops=dict(arrowstyle='->'),
        xytext=(4,10))                      # 添加注解
plt.text(0.5, 20, r"这是$\,FAST_{Plot}$")   # 添加文本
plt.grid(True, color='b')       # 显示网格
plt.box(True)                   # 显示方框坐标轴
plt.xlim(-0.5, 5.5)             # 获取或设置坐标范围
plt.ylim(ymin=-1, ymax=27)
plt.xscale('linear')            # 设置坐标刻度类型，即对轴坐标进行缩放
plt.yscale('linear')
plt.title("Fast Plot")          # 绘图标题
plt.xlabel("x step")            # 坐标轴标签
plt.ylabel("y value")
plt.xticks([])                  # 设置坐标刻度标签
plt.yticks([x**2 for x in range(0,6)],
        (r'$0^2$',r'$1^2$',r'$2^2$',r'$3^2$',r'$4^2$',r'$5^2$',))
plt.legend(loc='lower right')   # 添加图例
plt.show()                      # 显示绘图结果
```

![快速绘图](1.png)

## 子图绘图实例

```python
import matplotlib.pyplot as plt
plt.subplot(3, 3, 1)
plt.bar([1,2,3], height=[3,2,5])                            # 条形图
plt.subplot(332)
plt.hist([0,3,2,1,6,2,6], bins=[0,2,4,6,8], rwidth=0.8)     # 直方图
plt.subplot(333)
plt.scatter(x=[0,1,8,9,4,5], y=[4,7,1,8,7,5])               # 散点图
plt.subplot(334)
plt.stackplot([1,2,3,4,5], [7,8,6,11,7], [8,5,7,8,13])      # 堆叠图
plt.subplot(335)
plt.pie([7,8,6,11,2], autopct="%1.1f%%")                    # 饼状图
plt.subplot(336)
plt.matshow([[1,0,0], [0,1,0], [0,0,1]], fignum=False)      # 矩阵图
plt.subplot(337)
plt.contourf([1,2,3], [1,2,3], [[1,0,1],[1,2,0],[1,0,1]])   # 等高线
plt.subplot(338, projection='polar')
plt.polar([0,1,2,3,4,5,6], [0,2,0,1,3,1,3])                 # 极坐标图
plt.axes((0.8, 0.1, 0.1, 0.2))                              # 自定义子图位图
plt.show()
```

![子图绘图](2.png)

## 获取封装的对象

[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)其实是通过封装对象实现的函数式绘图，所以，[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)也提供了一些获取内部对象的函数，以及针对内部对象操作的函数（新出现的类名称在后面会讲到）：

 - `plt.figure`：创建一个新的`matplotlib.figure.Figure`对象
 - `plt.clf`：清空当前`figure`内容
 - `plt.close`：关闭当前`figure`
 - `plt.draw`：重绘当前`figure`
 - `plt.axes`：添加一个`matplotlib.axes.Axes`对象到当前的`figure`，且设为当前`axes`
 - `plt.subplot`：添加一个子图`matplotlib.axes.Axes`对象到当前`figure`
 - `plt.cla`：清空当前`axes`内容
 - `plt.gcf`：获取当前`figure`实例对象
 - `plt.gca`：获取当前`axes`实例对象
 - `plt.gci`：获取当前`matplotlib.cm.ScalarMappabl`实例对象
 - `plt.figlabels`：返回所有`figure`的标签
 - `plt.fignums`：返回所有`figure`的编号
 - `imread, imsave, imshow`：图像文件的读取、保存和显示


---
# 基本框架

想要深入的学习matplotlib绘图，了解[matplotlib内部模块和类](https://matplotlib.org/py-modindex.html)是很有必要的，同时，使用面向对象式的编程，来使用matplotlib绘图也是很有必要的。

## 底层backends

 - matplotlib.backend_bases.FigureCanvasBase：对绘图表面（类似于“绘图纸”）的概念进行封装
 - matplotlib.backend_bases.RendererBase：执行绘图动作（类似于“画笔”）
 - matplotlib.backend_bases.Event：处理键盘与鼠标事件

backend_bases需要处理底层的绘图显示和事件处理操作，例如在用户面界上绘图，可以使用Qt、Wx、Tk等作为底层，相应的底层操作封装在了backends.backend_qt5agg、backends.backend_wxagg、backends.backend_tkagg中；而绘制PDF、PNG等文件的底层操作，则封装到了backends.backend_pdf、backends.backend_agg中。

## 中间层artist

 - [matplotlib.artist.Artist](https://matplotlib.org/api/artist_api.html#module-matplotlib.artist)：使用`RendererBase`在`FigureCanvasBase`上绘图（类似于“画师”）

通常我们并不需要关心底层后端的操作细节，而是使用`Artist`绘图。
`Artist`分为简单类型和容器类型两种，简单类型的`Artist`为标准的绘图元件，如：

 - [matplotlib.lines.Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)
 - [matplotlib.patches.Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle)
 - [matplotlib.text.Text](https://matplotlib.org/api/text_api.html#matplotlib.text.Text)

而容器类型则可以包含许多简单类型的`Artist`，使它们组织成一个整体，如：

 - [matplotlib.figure.Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)
 - [matplotlib.axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes)
 - [matplotlib.axis.Axis](https://matplotlib.org/api/axis_api.html#module-matplotlib.axis)

下面是`Artist`类的常用属性：

```
alpha     : 透明度，值在0到1之间，0为完全透明，1为完全不透明
animated  : 布尔值，在绘制动画效果时使用
axes      : 此Artist对象所在的Axes对象，可能为None
clip_box  : 对象的裁剪框
clip_on   : 是否裁剪
clip_path : 裁剪的路径
contains  : 判断指定点是否在对象上的函数
figure    : 所在的Figure对象，可能为None
label     : 文本标签
picker    : 控制Artist对象选取
transform : 控制偏移旋转
visible   : 是否可见
zorder    : 控制绘图顺序
```

属性都通过相应的`get_*`和`set_*`函数进行读写，也可以使用`set()`和`get()`函数对多个属性进行读写。

### Figure

[matplotlib.figure.Figure](https://matplotlib.org/api/figure_api.html#module-matplotlib.figure)是一个最大的Artist，包含了一个图的所有元素。例如：背景是一个[Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle)对象，使用`Figure.patch`属性表示；可以使用`add_subplot`或`add_axes`来添加`Axes`；一个简图关系如下所示（[图片来源](https://blog.csdn.net/matrix_laboratory/article/details/50698239)）：

![Figure](3.png)

### Axes

[matplotlib.axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes)包含了许多组成`Figure`的元素，如[Axis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Axis)、[Tick](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Tick)、[Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)等，以及包含了众多的绘图函数，如`plot`、`bar`、`pie`等。`Axes.patch`属性用于表示`Axes`的背景，当使用笛卡尔坐标时，`patch`属性是一个[Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle)对象；当使用极坐标时，`patch`属性则是[Circle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle)对象。
可以简单地把`Axes`当一个图表，而一个`Figure`可以包含多个图表。即用`Axes`绘制图表，在`Figure`中摆放图表。

### Axis

[matplotlib.axis.Axis](https://matplotlib.org/api/axis_api.html#module-matplotlib.axis)是坐标轴容器，包括坐标轴上的刻度线、刻度文本、坐标网格、坐标轴标题等内容。

## 顶层pyplot

[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)就是前面讲面的函数式绘图了，使用绘图更加便捷。


---
# 面向对象式绘图

 - 纯面向对象式的绘图

使用[matplotlib.backends.backend_agg](https://matplotlib.org/api/backend_agg_api.html#module-matplotlib.backends.backend_agg)做为后端，再结合NumPy，一个纯面向对象的编程实例如下：

```python
import numpy as np
import matplotlib.figure as mfig
import matplotlib.backends.backend_agg as mbk

fig = mfig.Figure()
canvas = mbk.FigureCanvas(fig)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='polar') # 添加极坐极图表

theta = np.linspace(0, 1.5*np.pi, 1000, dtype = np.float)
r = np.exp(theta)
ax.plot(theta, r, color='green')        # 绘制对数螺线

fig.savefig('fig1.png')                 # 保存成fig1.png
```

![fig1](fig1.png)

 - 结合pyplot的面向对象式绘图

纯面向对象绘图，需要保存图表到文件，不能即时的显示绘制的图表，不太方便。结合pyplot，可以使得面向对象式绘图更方便，一个实例如下：

```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure('fig')    # 添加Figure
ax = fig.add_subplot(111, projection='polar') # 添加极坐极图表

theta = np.linspace(0, 1.5*np.pi, 1000, dtype = np.float)
r = np.exp(theta)
ax.plot(theta, r, color='green')        # 绘制对数螺线

plt.show()                              # 显示绘图
```

---
# 用户交互

用户交互主要是指，在显示绘图后，通过`鼠标`、`键盘`等事件，或者`按钮`、`选择框`等控制，与用户进行信息交互。

## 事件交互

要进行鼠标、键盘等事件交互，需要将事件回调函数，连接到事件管理器，可以使用[matplotlib.backend_bases.FigureCanvasBase](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.Event)的`mpl_connect`和`mpl_disconnect`函数来连接或断开事件回调函数。更具的可以参考[事件交互官方资料](https://matplotlib.org/users/event_handling.html)。一个简单的实例如下：

```python
import matplotlib
import matplotlib.pyplot as plt

def on_key(event:matplotlib.backend_bases.KeyEvent):
    if event.key == 'escape':
        plt.close(event.canvas.figure)      # 关闭接收事件Figure

fig = plt.figure('fig')    # 添加Figure
key_id = fig.canvas.mpl_connect('key_press_event', on_key)  # 连接事件回调函数
# fig.canvas.mpl_disconnect(key_id)                         # 断开事件回调函数
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(range(10), color='red')
plt.show()
```

## 所有可用事件

| 事件                   | 类                                                                                                        | 说明
| :-                     | :-                                                                                                        | :-
| `button_press_event  ` | [MouseEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent)       | 鼠标按钮被按下
| `button_release_event` | [MouseEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent)       | 鼠标按钮被释放
| `draw_event          ` | [DrawEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.DrawEvent)         | 画布绘图
| `key_press_event     ` | [KeyEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent)           | 按键被按下
| `key_release_event   ` | [KeyEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent)           | 按键被释放
| `motion_notify_event ` | [MouseEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent)       | 鼠标移动
| `pick_event          ` | [PickEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent)         | 画布中的对象被选中
| `resize_event        ` | [ResizeEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.ResizeEvent)     | 图形画布大小改变
| `scroll_event        ` | [MouseEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent)       | 鼠标滚轮被滚动
| `figure_enter_event  ` | [LocationEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent) | 鼠标进入新的图形
| `figure_leave_event  ` | [LocationEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent) | 鼠标离开图形
| `axes_enter_event    ` | [LocationEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent) | 鼠标进入新的轴域
| `axes_leave_event    ` | [LocationEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent) | 鼠标离开轴域
| `close_event         ` | [CloseEvent](https://matplotlib.org/api/backend_bases_api.html#matplotlib.backend_bases.CloseEvent)       | 关闭Figure

## 界面交互

界面控件在[matplotlib.widgets](https://matplotlib.org/api/widgets_api.html#module-matplotlib.widgets)模块中，一个控件需要与一个`Axes`绑定。一个简单实例如下：

```python
import matplotlib
import matplotlib.pyplot as plt

def on_click(event:matplotlib.backend_bases.MouseEvent):
    plt.close(event.canvas.figure)      # 关闭接收事件Figure

fig = plt.figure('fig')                 # 添加Figure
ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax0.plot(range(10), color='red')
ax = fig.add_axes([0.1, 0.85, 0.1, 0.05])
btn = matplotlib.widgets.Button(ax, "Click Me", )
cid = btn.on_clicked(on_click)          # 连接点击事件
# btn.disconnect(cid)                     # 断开点击事件
plt.show()
```

![button](btn.png)

---
# 3D绘图

Matplotlib已经内置3D绘图模块[mplot3d API](https://matplotlib.org/api/toolkits/mplot3d.html)，在程序中引入即可使用。绘图时，主要使用[Axes3D](https://matplotlib.org/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D)的函数进行绘制3D图形绘制。一个简单实例如下：

```python
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d

fig = plt.figure('fig')                     # 添加Figure
ax = fig.add_subplot(111, projection='3d')  # 添加3d图表
a = b = np.linspace(0, 3*np.pi, 1000)
x, y = np.meshgrid(a, b)                    # 生成x,y坐标数据
z = 10 * np.sin(np.sqrt(x**2 + y**2))       # 生成z数据
ax.plot_wireframe(x, y, z, color='red')     # 绘制
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

![3d](3d.png)

3D绘图也可以绘制散点图、条形图等，这里就不一一举例了。
