from win32com.client import Dispatch
import os

def create_desktop_shortcut(target_file, shortcut_name, icon=None):
    start_menu_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    desktop_path = start_menu_path
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(os.path.join(desktop_path, f'{shortcut_name}.lnk'))
    shortcut.Targetpath = target_file
    shortcut.WorkingDirectory = os.path.dirname(target_file)
    if icon:
        
        shortcut.IconLocation = icon
    shortcut.save()
