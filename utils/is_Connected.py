# import requests
import subprocess

def get_status_ping():
    r = subprocess.run('ping www.cnki.net -n 1',
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin= subprocess.PIPE,
                       shell=True)
    # print(r.returncode)
    return r.returncode

# def get_status(): #不好用
#     login_html = "http://www.cnki.net"
#     try:
#         page_status = requests.get(login_html, timeout=1)
#         response = page_status.status_code
#     except requests.exceptions.Timeout:
#         response = -1  # 设置超时时的状态码
#     except requests.exceptions.RequestException:
#         response = -2  # 设置其他错误时的状态码
#     print("登录页面状态码:", response)
#     return response

def is_Connected():
    connect = False
    # get_status()
    response = get_status_ping()
    if(response == 1):
        connect = False
    elif(response == 0):
        connect = True
    # print( is_Connected())

    return connect