
@echo off
echo Are you sure : Continue generate and delopy ?????
echo Press Ctrl + c to exit.
pause

echo Hexo : generate and deploy in oschina...
copy /y _config_oschina.yml _config.yml
hexo clean && ^
hexo generate && ^
hexo deploy && ^
echo Hexo : generate and deploy in github... && ^
copy /y _config_github.yml _config.yml && ^
hexo clean && ^
hexo generate && ^
hexo deploy && ^
echo Hexo : deploy complete! && ^
copy /y _config_all.yml _config.yml && ^
hexo clean & pause

