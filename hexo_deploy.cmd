
@echo off
echo This need admini and are you sure : Continue generate and delopy ?
echo Press Ctrl + c to exit.
pause

echo Hexo : generate and deploy in gitee...
hexo clean && ^
hexo generate && ^
hexo deploy && ^
echo Hexo : deploy complete! && ^
hexo clean & pause

