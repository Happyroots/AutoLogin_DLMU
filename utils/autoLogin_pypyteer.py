import asyncio
import  pyppeteer as pyp
import random
import time
from utils.operatation_message import read_message, save_message


async def antiAntiCrawler(page):
    await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; \
                            Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/78.0.3904.70 Safari/537.36')
    await page.evaluateOnNewDocument(
        '() => { Object.defineProperties(navigator, \
        { webdriver:{ get () => false}})}')
    
async def getOjSourceCode(loginUrl):
    #缺点：第一次使用需要代理下载google chromiumu
    file_state,username,password,domain = await read_message()
    width, height = 1400,800 #网页宽高
    browser = await pyp.launch(headless=False,
                            userdataDir = "C:\\Users\\Dr.Y\\Desktop",
                            args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await antiAntiCrawler(page)
    await page.setViewport({'width': width, 'height':height})

    await page.goto(loginUrl)
    await page.waitForNavigation()# 等待新的网页装入完毕，并不保险，有可能一下跳好几个文件
    time.sleep(10)
    # 若手动登录，则一下若干行可以去掉
    element = await page.querySelector("#login-normal > div:nth-child(2) > form > div.login-normal-item.ant-row.ng-star-inserted > nz-input-group > input")
    await element.type(str(username))
    element = await page.querySelector("#login-normal > div:nth-child(2) > form > div.login-normal-item.passwordInput.ant-row > nz-input-group > input")
    await element.type(str(password))
    element = await page.querySelector("#login-normal > div:nth-child(2) > form > div.login-normal-button.ant-row > div > button > span")#找到登录按钮，"#"代表id属性
    time.sleep(random.randint(1,10))
    await element.click()#点击登录按钮; 异步协程，立即返回，不等待; 若操作下个页面则会出错
    # 若手动登录，上面若干行可以去掉
    await page.waitForNavigation()# 等待新的网页装入完毕，并不保险，有可能一下跳好几个文件
    time.sleep(random.randint(1,10))

    print("已登录")
    await browser.close()

def autologin_pyppeteer():
    #是永久的吗？
    print("logining")
    read_message()
    url = "https://id.dlmu.edu.cn/login?service=http:%2F%2F202.118.88.9%2Feportal%2Findex.jsp%3Fwlanuserip%3De9f6276ead07a8898d26e726ce8bc542%26wlanacname%3Dc20f646d18ec8420743bb59779d3aa5d%26ssid%3D%26nasip%3D321b8c06ed4b01461a74c22a11633718%26snmpagentip%3D%26mac%3Df829acacc6e60116edc2607f84e1b916%26t%3Dwireless-v2%26url%3Dba89be7f1fb5bf76c7c21d5e78a4bb46db7404fdfae1ba7ecb96f7d8f9ef275bc2ea29441f0f9b828e33c91b499b916b2877795b9a17c8b4d5b8df94bcddf2fa%26apmac%3D%26nasid%3Dc20f646d18ec8420743bb59779d3aa5d%26vid%3D6121f950533a4bd1%26port%3D1f897c6a120b51aa%26nasportid%3Dc6abed3ee205e3f81369f2aee75d9658793233c2c2ba139ad6600e266c032f8d7f91717f7fc80086"
    asyncio.get_event_loop().run_until_complete(getOjSourceCode(url)) # 协程启动！
