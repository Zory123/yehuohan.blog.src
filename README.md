
---
# yehuohan.blog.src

 - [yehuohan.github.io](https://yehuohan.github.io)

---
# Hexo Style
 - tags：一般全小写，做为二级分类
 - categories：目前只有“笔记，杂记，随笔，Gist”

---
# MarkDown Style

 - code：代码标识\`\`\`前后均空一行，或只在后面空一行
 - 图片：优先使用MarkDown自身语法`![]()`（hexo asset_img 语法只用于需要在标题预览图片的地方）
 - 引用：数学公式使用MathJax的语法，MarkDown使用以下语法：

```
\\\ 标记处：
<span id = "图1-1"></span>

\\\ 引用处：
[图1-1](#图1-1)
```

---
# Plugin & Config

 - [3-hexo排序](http://yelog.org/2017/02/24/hexo-top-sort/)：修改node_modules/hexo-generator-index/lib/generator.js
 - [3-hexo数学公式](http://yelog.org/2017/07/05/3-hexo-mathjax/)：修改node_modules\marked\lib\marked.js
 - [hexo-auto-category](https://github.com/xu-song/hexo-auto-category)：按目录生成分类
