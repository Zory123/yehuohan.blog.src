
@echo off
echo This need admini and are you sure : Continue generate and delopy ?
echo Press Ctrl + c to exit.
pause

echo Hexo : generate and deploy in gitee...
copy /y _config_gitee.yml _config.yml
hexo clean && ^
hexo generate && ^
hexo deploy && ^
echo Hexo : generate and deploy in github... && ^
copy /y _config_github.yml _config.yml && ^
hexo clean && ^
hexo generate && ^
hexo deploy && ^
echo Hexo : deploy complete! && ^
hexo clean & pause

