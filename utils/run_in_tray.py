import pystray
from PIL import Image

def on_quit_clicked(icon, item):
    icon.stop()

# 定义点击托盘图标时执行的操作
def on_tray_clicked(icon, item):
    pass    

def runInTray():
    # 创建托盘图标
    image = Image.open("icon.png")  # 替换成你自己的图标文件路径
    menu = (pystray.MenuItem('None', on_tray_clicked), \
            pystray.MenuItem('Quit', on_quit_clicked)    )
    programme_pystray = pystray.Icon('name', image, 'auto_login', menu)

    # 运行托盘应用
    programme_pystray.run()