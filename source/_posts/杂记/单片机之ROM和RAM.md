---
title: 单片机之ROM和RAM
categories:
  - 杂记
tags: 单片机
date: 2017-06-16 21:27:13
---


---
# RAM和ROM基本介绍
ROM和RAM都是半导体存储器。
ROM是Read Only Memory的缩写，在系统停止供电时，仍然可以保持数据；
RAM是Random Access Memory，通常掉电之后就丢失数据，典型的RAM就是计算机内存。

本文对ROM和RAM的分类进行一些说明。
将断电后能保存断据的，均归于ROM类；断电后不能保存数据的，均归于RAM类。


<!-- more -->


---
# RAM主要分类
 - 静态SRAM(Static RAM)
SRAM速度非常快，读写快，但是也非常昂贵，好多单片机中有SRAM，CPU的一级缓冲，二级缓冲也是SRAM。

 - 动态RAM(Dynamic RAM)
DRAM保留数据的时间很短，需要不断刷新，速度也比SRAM慢，不过它还是比任何的ROM都要快，但从价格上来说DRAM相比SRAM要便宜很多。

 - FIFO
全称是先进先出存储器。只允许两端，一个写，一个读，但不能对FIFO内部的存储器进行寻址（双口RAM可以对存储单元寻址）。


---
# ROM主要分类
 - 可编程ROM(PROM)
是一次性的，只允许定入一次，无法再修改，这种是早期的产品，现在已经不可能使用了。

 - 可擦除ROM(EPROM)
是通过紫外光的照射擦出原先的程序，是一种通用的存储器。

 - EEPROM
可直接用电信号擦除，也可用电信号写入。而且是以Byte为最小修改单位，不必将资料全部洗掉才能写入。

 - Flash
FLASH存储器又称闪存，它结合了ROM和RAM的长处，不仅具备电子可擦除可编程(EEPROM)的性能，还不会断电丢失数据，同时可以快速读取数据，U盘和MP3里用的就是这种存储器。
属于EEPROM的改进，在嵌入式中，也是EEPROM替代品。

 - NOR Flash
NOR Flash的读取和我们常见的SDRAM的读取是一样，用户可以直接运行装载在NOR FLASH里面的代码，这样可以减少SRAM的容量从而节约了成本。
但是写入速度低，擦除速度慢。

 - NAND Flash
NAND Flash没有采取内存的随机读取技术，它的读取是以一次读取一块的形式来进行的，通常是一次读取512个字节。写入擦除速度快，适用于大量数据存储。
用户不能直接运行NAND Flash上的代码，因此好多使用NAND Flash的开发板除了使用NAND Flash以外，还用一块小的NOR Flash来运行启动代码。 
