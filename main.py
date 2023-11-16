from utils.autoLogin_pypyteer import autologin_pyppeteer
from utils.is_Connected import is_Connected
from utils.calculate_delay_time import calculate_delay_time
from utils.run_in_tray import runInTray
import schedule
import time
import threading
import os
from utils import flag
from utils.create_desktop_shortcut import create_desktop_shortcut
import sys

def check_and_login():
    if(is_Connected() == False):
        autologin_pyppeteer()

def schedule_task(_hour=8, _minute=8, _second=0, _microsecond=0):
    delay = calculate_delay_time(_hour, _minute, _second, _microsecond)
    schedule.every(delay).seconds.do(check_and_login)

def main():
    check_and_login()
    while (True):
        schedule_task(8, 8)
        schedule.run_pending()
        time.sleep(1)
        if (flag.exit_flag):
            print("exit")
            break

if __name__=='__main__':
    current_path = executable_path_exe = ""
    if getattr(sys, 'frozen', False):
        current_path = os.path.dirname(sys.executable)
        executable_path_exe = os.path.join(current_path, 'AutoLogin_DLMU.exe')
  
    path_icon = os.path.join(current_path, "autologin.ico")  
    create_desktop_shortcut(executable_path_exe,'AutoLogin_DLMU', )

    thread = threading.Thread(target=runInTray)
    thread.daemon = True
    thread.start()
  
    main()

    
