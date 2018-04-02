---
title: Vim加几行代码实现qmake工程的构建
categories:
  - 杂记
mathjax: false
tags:
  - vim
date: 2017-09-28 20:43:11
---

在vimrc加几行代码，实现qmake工程的构建，直接用vim简单实现qt-IDE。

<!-- more -->

使用简单，打开pro文件，call QtBuild()即可。有几点说明：
 - linux下需要安装qmake和make
 - windows下需要安装Qt
  - 若使用Qt-msvc版，需要将VS的vcvars32.bat所在路径添加到PATH环境变量中；
  - 若使用Qt-mingw版，则需要将代码中的nmake改成make，同时去掉vcvars32.bat；

```vim
function! QtBuild()
    let l:ext = expand("%:e")                             " 扩展名
    let l:filename = '"./' . expand('%:t') . '"'          " 文件名，不带路径，带扩展名
    let l:name = '"./' . expand('%:t:r') . '"'            " 文件名，不带路径，不带扩展名
    let l:exec_str = "!"
    if exists(":AsyncRun") == 2                           " 如果有asyncrun异步插件，则使用之
        let l:exec_str = ":AsyncRun "
    endif

    if "pro" ==? l:ext
        if IsLinux()
            let l:exec_str .= "qmake " . " -r -o ./DebugV/Makefile " . l:filename
            let l:exec_str .= " && cd ./DebugV"
            let l:exec_str .= " && make"
        else if IsWin()
            let l:exec_str .= " mkdir DebugV"
            let l:exec_str .= " & cd DebugV"
            " Attetion: here shouls be <qmake ../file.pro>
            let l:exec_str .= " && qmake " . " -r ." . l:filename
            let l:exec_str .= " && vcvars32.bat"
            let l:exec_str .= " && nmake -f Makefile.Debug"
            let l:exec_str .= " && cd ./debug"
        endif
        let l:exec_str .= " && " . l:name
    else
        return
    endif

    " execute shell code
    execute l:exec_str
endfunction

```
