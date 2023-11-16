import winreg
import os
import subprocess

# 注册表项信息
reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
key_name = "autoLogin_DLMU"
current_path = os.path.dirname(os.path.abspath(__file__))
executable_path_exe = os.path.join(current_path, 'dist', 'main', 'main.exe')
executable_path = r"C:/Users/Dr.Y/anaconda3/envs/crawler/python.exe c:/Users/Dr.Y/Desktop/AutoLogin_DLMU/main.py"
executable_path = executable_path_exe

def check_registry_key():
    is_exist = False
    
    try:
        # 打开注册表项
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
        
        # 检查注册表项中是否存在指定的键
        value, _ = winreg.QueryValueEx(key, key_name)
        if value == executable_path:
            is_exist = True
            print("Registry key exist.")
        elif (value != executable_path):
            print("Registry key does not match.")
            delete_registry_key()
            is_exist = False
        else:
            is_exist = False
            print("Registry key does not exist.")

        # 关闭注册表项
        winreg.CloseKey(key)

    except FileNotFoundError:
        is_exist = False
        print("Registry key does not exist.")
    return is_exist

def create_registry_key():
    # 创建或打开注册表项
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

    # 在注册表项中设置键值
    winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, executable_path)

    # 关闭注册表项
    winreg.CloseKey(key)
    print("Registry key created.")

def delete_registry_key():
    try:
        # 打开注册表项
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS)

        # 删除指定的键
        winreg.DeleteValue(key, key_name)

        # 关闭注册表项
        winreg.CloseKey(key)
        print("Registry key deleted.")

    except FileNotFoundError:
        print("Registry key does not exist.")

def start_when_startup():
    if(check_registry_key() == False):
        create_registry_key()

def close_when_startup():
    if(check_registry_key() == True):
        delete_registry_key()

def edit_regedit():
    global autorun_value_flag,autorun_value

    key_browser = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet")
    browser_value, type1 = winreg.QueryValueEx(key_browser, r'EnableActiveProbing')

    try:
        key_autorun = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
        autorun_value, type2 = winreg.QueryValueEx(key_autorun, key_name)
        if autorun_value != 0:
            autorun_value_flag = 0
        #print(autorun_value)
    except FileNotFoundError:
        autorun_value_flag = 1
    except NameError:
        autorun_value_flag = 1
    list=[browser_value, autorun_value_flag]

    current_path = os.path.dirname(os.path.abspath(__file__))
    # exe_path = os.path.join(current_path, "..", "main.exe")
    exe_path = os.path.join(current_path, "..", "dist", "main", "main.exe")

    registry_content = f"""
    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
    "autoLogin_DLMU"="{exe_path}" 
    """ 
    # registry_content = f"""
    # Windows Registry Editor Version 5.00

    # [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet]
    # "EnableActiveProbing"=dword:1

    # [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
    # "i-NUSIT1.0"=-
    # """
    with open("registration.reg", "w") as reg_file:
        reg_file.write(registry_content)

    if autorun_value_flag != 0:
        print('【开机自启动-注册表已写入】')
        print(' ')
        subprocess.Popen(['regedit', '/s', current_path + '\\..\\registration.reg'], shell=True)
        os.system('regedit /s ' + current_path + '\\..\\registration.reg')
    else:
        pass
    return browser_value,autorun_value_flag

def recover_regedit():
    # registry_content = f"""
    # Windows Registry Editor Version 5.00

    # [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
    # "autoLogin_DLMU"="-" 
    # """
    registry_content = fr"""
    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet]
    "EnableActiveProbing"=dword:1

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
    "i-NUSIT1.0"=-"""

    with open("registration.reg", "w") as reg_file:
        reg_file.write(registry_content)

    print('【开机自启动-注册表已写入】')
    print(' ')
    subprocess.Popen(['regedit', '/s', current_path + '\\..\\registration.reg'], shell=True)


if __name__ == "__main__":
    recover_regedit()