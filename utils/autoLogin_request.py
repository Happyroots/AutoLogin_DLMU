import requests
import urllib.parse
import base64
from operatation_message import read_message, save_message

def autologin_requests():
    #缺点：使用代理没法连接
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '6269',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'SESSION=c9840b46-46f2-4ecd-8d8c-f9ab27210c85',
        'Host': 'id.dlmu.edu.cn',
        'Origin': 'https://id.dlmu.edu.cn',
        'Referer': 'https://id.dlmu.edu.cn/login?service=http:%2F%2F202.118.88.9%2Feportal%2Findex.jsp%3Fwlanuserip%3De9f6276ead07a8898d26e726ce8bc542%26wlanacname%3Dc20f646d18ec8420743bb59779d3aa5d%26ssid%3D%26nasip%3D321b8c06ed4b01461a74c22a11633718%26snmpagentip%3D%26mac%3Df829acacc6e60116edc2607f84e1b916%26t%3Dwireless-v2%26url%3Dba89be7f1fb5bf76c7c21d5e78a4bb46db7404fdfae1ba7ecb96f7d8f9ef275bc2ea29441f0f9b828e33c91b499b916b2877795b9a17c8b4d5b8df94bcddf2fa%26apmac%3D%26nasid%3Dc20f646d18ec8420743bb59779d3aa5d%26vid%3D6121f950533a4bd1%26port%3D1f897c6a120b51aa%26nasportid%3Dc6abed3ee205e3f81369f2aee75d9658793233c2c2ba139ad6600e266c032f8d7f91717f7fc80086',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    file_state,username,password,domain = read_message()
    # 对字符串进行 URL 编码
    encoded_password = urllib.parse.quote(password)
    # 对字符串进行 Base64 编码
    base64_encoded_data = base64.b64encode(password.encode()).decode()

    # 将编码后的值拼接成负载数据
    data = {
        'username': username,
        'type':'UsernamePassword',
        '_eventId': 'submit',
        'geolocation': '',
        'execution': 'f18a4cbc-6c21-4431-8648-db8d1e73429f_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',
        'captcha_code': '',
        'croypto': 'q51enXbv74k=',
        'password': encoded_password,
    }

    url = 'https://id.dlmu.edu.cn/login'  # 修改为你的目标URL

    response = requests.post(url, headers=headers, data=data, timeout=10)
    print(response.text)  # 输出响应内容

if __name__ == "__main__":
    autologin_requests()