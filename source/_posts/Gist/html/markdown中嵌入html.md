---
title: markdown中嵌入html
categories:
  - Gist
mathjax: false
date: 2018-01-21 23:18:46
tags:
 - html
---

> File : html_in_md.html
> Type : html
> Brief : 在markdown中使用html

<!-- more -->

---

在MarkDown中可以使用Html5和JavaScript。

<canvas id = "cnsDraw" class = "drawArea" width = "600" height = "500"
  style = "border : 1px solid #ddd;"
></canvas>

<script charset="utf-8">
  var c = document.getElementById("cnsDraw");
  var ctx = c.getContext("2d");
  var curPoint = {
    x : 0,
    y : 0
  }
  var lastPoint = curPoint;
  var leftPressed = false;

  initCanvas();

  function initCanvas() {
    ctx.moveTo(0, 0);
    ctx.lineTo(100, 100);
    ctx.lineTo(200, 100);
    ctx.arc(100, 100, 99, 0, 2*Math.PI);
    ctx.font = "30px";
    ctx.fillText("Hello", 100, 110);
    ctx.stroke();
  }

  function getCanvasPoint(c, x, y) {
    var cbox = c.getBoundingClientRect();
    return {
      x : (x - cbox.left) * (c.width / cbox.width),
      y : (y - cbox.top) * (c.height / cbox.height)
    };
  }

  c.onmousedown = function(e){
    curPoint = getCanvasPoint(c, e.pageX, e.pageY);
    lastPoint = curPoint;
    leftPressed = true;
  }

  c.onmousemove = function(e){
    if (leftPressed)
    {
      curPoint = getCanvasPoint(c, e.pageX, e.pageY);
      ctx.moveTo(curPoint.x, curPoint.y);
      ctx.lineTo(lastPoint.x, lastPoint.y);
      lastPoint = curPoint;
      ctx.stroke();
    }
  }

  c.onmouseup = function(e){
    if (leftPressed)
    {
      curPoint = getCanvasPoint(c, e.pageX, e.pageY);
      ctx.moveTo(curPoint.x, curPoint.y);
      ctx.lineTo(lastPoint.x, lastPoint.y);
      lastPoint = curPoint;
      ctx.stroke();
    }
    leftPressed = false;
  }
</script>


```html
<canvas id = "cnsDraw" class = "drawArea" width = "600" height = "500"
  style = "border : 1px solid #ddd;"
></canvas>

<script charset="utf-8">
  var c = document.getElementById("cnsDraw");
  var ctx = c.getContext("2d");
  var curPoint = {
    x : 0,
    y : 0
  }
  var lastPoint = curPoint;
  var leftPressed = false;

  initCanvas();

  function initCanvas() {
    ctx.moveTo(0, 0);
    ctx.lineTo(100, 100);
    ctx.lineTo(200, 100);
    ctx.arc(100, 100, 99, 0, 2*Math.PI);
    ctx.font = "30px";
    ctx.fillText("Hello", 100, 110);
    ctx.stroke();
  }

  function getCanvasPoint(c, x, y) {
    var cbox = c.getBoundingClientRect();
    return {
      x : (x - cbox.left) * (c.width / cbox.width),
      y : (y - cbox.top) * (c.height / cbox.height)
    };
  }

  c.onmousedown = function(e){
    curPoint = getCanvasPoint(c, e.pageX, e.pageY);
    lastPoint = curPoint;
    leftPressed = true;
  }

  c.onmousemove = function(e){
    if (leftPressed)
    {
      curPoint = getCanvasPoint(c, e.pageX, e.pageY);
      ctx.moveTo(curPoint.x, curPoint.y);
      ctx.lineTo(lastPoint.x, lastPoint.y);
      lastPoint = curPoint;
      ctx.stroke();
    }
  }

  c.onmouseup = function(e){
    if (leftPressed)
    {
      curPoint = getCanvasPoint(c, e.pageX, e.pageY);
      ctx.moveTo(curPoint.x, curPoint.y);
      ctx.lineTo(lastPoint.x, lastPoint.y);
      lastPoint = curPoint;
      ctx.stroke();
    }
    leftPressed = false;
  }
</script>

```
