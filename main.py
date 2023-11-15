from utils.autoLogin_pypyteer import autologin_pyppeteer
from utils.is_Connected import is_Connected
from utils.calculate_delay_time import calculate_delay_time
from utils.run_in_tray import runInTray
from utils.start_when_startup import edit_regedit
import schedule
import time
# from start_when_startup import start_when_startup, close_when_startup
import threading
import sys

def check_and_login():
    if(is_Connected() == False):
        autologin_pyppeteer()

def schedule_task():
    delay = calculate_delay_time()
    schedule.every(delay).seconds.do(check_and_login)

# 创建异步事件循环
def main():
    # 异步加载pypeteer相关代码
    while (True):
        schedule_task()
        schedule.run_pending()
        time.sleep(1)

import os
import shutil

def start_when_startup():
    # 获取本程序文件的文件位置
    current_path = os.path.dirname(os.path.abspath(__file__))

    # 解析盘符
    drive_letter, _ = os.path.splitdrive(current_path)

    # 创建.bat文件
    bat_file_path = os.path.join(current_path, 'startup_script_autologin_dlmu.bat')
    with open(bat_file_path, 'w') as f:
        f.write(f'{drive_letter}\n')
        f.write(f'cd {current_path}\n')
        f.write(f'conda activate crawler\n')
        f.write('python main.py')  # 将xxx.py替换为你所要自启动的Python程序的文件名

    # 移动.bat文件到启动目录
    startup_folder = os.path.join('C:', 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'StartUp') 
    shutil.move(bat_file_path, os.path.join(startup_folder, 'startup_script_autologin_dlmu.bat'))

if __name__=='__main__':
    # # 创建并启动循环线程，守护线程会随着程序退出而退出
    # edit_regedit()
    thread = threading.Thread(target=main)
    thread.daemon = True
    thread.start()
    runInTray()

    
