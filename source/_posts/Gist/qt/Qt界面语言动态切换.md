---
title: Qt界面语言动态切换
categories:
  - Gist
mathjax: false
tags:
  - qt
date: 2017-09-29 21:18:18
---

> File : [lang.h 主要程序](lang.h) *(直接右键另存为下载)*
> File : [main.cpp](main.cpp) *(直接右键另存为下载)*
> File : [lang.pro](lang.pro) *(直接右键另存为下载)*
> File : [en.qm](en.qm) *(直接右键另存为下载)*
> File : [zh.qm](zh.qm) *(直接右键另存为下载)*
> Type : qt
> Brief : Qt界面语言动态切换，以一个Button为例，文件有点多。

<!-- more -->

---

 - 要点：要做动动态切换语言，从load(qm) -> install translator -> set text，一步都不能少。

```cpp
// lang.h
#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
#include <QTranslator>
class LangUi : public QObject
{
    Q_OBJECT
public:
    void setupUi(QMainWindow* pa)
    {
        this->setParent(pa);
        this->btn = new QPushButton(pa);
        this->setTranslator();
    }

    void setTranslator()
    {
        this->btn->setText(tr("Toggle"));
    }
    QPushButton* btn;
};

class Lang : public QMainWindow
{
    Q_OBJECT
public:
    Lang(QWidget *parent = 0): QMainWindow(parent), ui(new LangUi()), trans(new QTranslator())
    {
        ui->setupUi(this);
        lang = 0;
        connect(this->ui->btn, &QPushButton::clicked, 
                [this]{
                    if (0 == lang)
                    {
                        lang = 1;
                        trans->load("zh.qm");
                    }
                    else if(1 == lang)
                    {
                        lang = 0;
                        trans->load("en.qm");
                    }
                    qApp->installTranslator(trans);
                    this->ui->setTranslator();
                });
    }
    ~Lang(){}
private:
    LangUi* ui;
    QTranslator* trans;
    int lang;
};



```
