# video2text
视频->音频->剥离出人声->去噪、声音正则化、去静默等->语音识别


# 添加子模块
+ [git中submodule子模块的添加、使用和删除](https://blog.csdn.net/guotianqing/article/details/82391665)
git submodule add git@github.com:X-CCS/spleeter.git ./spleeter
git submodule add git@github.com:redtreeai/subtitle-maker.git ./subtitle-maker
git commit -m "add subtitle-maker submodule"
git submodule add git@github.com:X-CCS/aukit.git ./aukit
git commit -m "add aukit submodule"