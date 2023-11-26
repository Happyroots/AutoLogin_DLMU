import requests
import subprocess
# 由于代理的原因，测试联网不太好用
def get_status_ping():
    test_url = 'www.bing.com'
    r = subprocess.run(
                        'ping ' + test_url + ' -n 1',
                        # 'ping https://cn.bing.com/search?pglt=515&q=cnki&cvid=d33960dfab8143d59caf4e9607bad3f7&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGEEyBggCEEUYQTIGCAMQRRhBMgYIBBBFGDwyBggFEEUYPNIBCDEwNjJqMGoxqAIAsAIA&FORM=ANNTA1&PC=CNNDDB -n 1',
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin= subprocess.PIPE,
                       shell=True)
    print("登录页面状态码:", r.returncode)
    return r.returncode

def get_status_requests(login_html = "http://www.cnki.net"): #不好用
    login_html = "https://sunlogin.oray.com"
    # login_html = "https://cn.bing.com/search?pglt=515&q=cnki&cvid=d33960dfab8143d59caf4e9607bad3f7&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGEEyBggCEEUYQTIGCAMQRRhBMgYIBBBFGDwyBggFEEUYPNIBCDEwNjJqMGoxqAIAsAIA&FORM=ANNTA1&PC=CNNDDB"
    try:
        page_status = requests.get(login_html, timeout=1)
        response = page_status.status_code
    except requests.exceptions.Timeout:
        response = -1  # 设置超时时的状态码
    except requests.exceptions.RequestException:
        response = -2  # 设置其他错误时的状态码
    print("登录页面状态码:", response)
    return response

def is_Connected():
    connect = False
    response = get_status_ping()
    if(response == 1):
        connect = False
    elif(response == 0):
        connect = True
    # response = get_status_requests()
    # if(response == 200):
    #         connect = True
    # elif(response == -1 or response == -2):
    #     connect = False
        
    return connect