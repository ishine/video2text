# video2text
视频->音频->剥离出人声->去噪、声音正则化、去静默等->语音识别


# 添加子模块
+ [git中submodule子模块的添加、使用和删除](https://blog.csdn.net/guotianqing/article/details/82391665)
git submodule add git@github.com:X-CCS/spleeter.git ./spleeter
git submodule add git@github.com:redtreeai/subtitle-maker.git ./subtitle-maker
git commit -m "add subtitle-maker submodule"
git submodule add git@github.com:X-CCS/aukit.git ./aukit
git commit -m "add aukit submodule"

# 远程服务器开
ssh chenchangshu@192.168.9.202
123456
conda activate spleeter

cp -r ./pretrained_models/ ../video2text/spleeter/
1、放个视频跟音频过去
2、测试视频剥离，弄出音频
