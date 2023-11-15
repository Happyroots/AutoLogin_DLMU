# AutoLogin_DLMU
自动登录大连海事校园网（电脑网线端）
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/Downtime111/i-NUSIT-AutoLogin.svg)](https://github.com/Downtime111/i-NUSIT-AutoLogin)  [![Github All Releases](https://img.shields.io/github/downloads/Downtime111/i-NUSIT-AutoLogin/total.svg)](http://github.com/Downtime111/i-NUSIT-AutoLogin/releases)  [![GitHub release](https://img.shields.io/github/release/Downtime111/i-NUSIT-AutoLogin.svg)](http://github.com/Downtime111/i-NUSIT-AutoLogin/releases)  [![GitHub issues](https://img.shields.io/github/issues/Downtime111/i-NUSIT-AutoLogin.svg)](https://github.com/Downtime111/i-NUSIT-AutoLogin/issues)

# 背景
出差或放假等场景需要远程连接使用学校的电脑，但是校园网月初会自动断开，导致无法远程，所以萌生了自动连接校园网的需求。

# Todo
* 开机自启
    * 手动操作：
        1. Win + R 快捷键打开运行窗口；
        2. 输入 shell:Startup，点击“确定”即可；可见，自启动文件保存在以下路径：C:\用户\[你的用户名]\AppData\Roaming\Microsoft\Windows\「开始」菜单\程序\启动
        3. 放入原脚本的快捷方式,切记一定是原脚本的快捷方式，不是原脚本
        4. 参考文章：http://t.csdnimg.cn/B2BKP ，经过验证，第一种方式是可行的
    * 注册表方法，程序一闪而过，原因未知。可能是系统保护，懒得查了，另外修改系统设置可能会出问题，就这么凑活用吧。下个脚本再研究
* ~~自动检测网络状态~~
* ~~把网址、用户名、密码放到文件中,自己输入文件路径？~~
* ~~每天8点检查连接状态~~
* ~~托盘运行~~
* 装饰器
* 实现休眠后登陆时自动联网

# issue
1. 校园网登录的网址不知道是什么。为了防爬，先请求网络才可以获得有效网址，一般的网址请求网络，百度，B站都免疫。解决方法：需要登录时，在浏览器上临时粘贴

# Advance
1. ~~抓包，实现request库自动爬取~~

# 注意事项
1. 使用之前需要魔法下载chromium.exe
