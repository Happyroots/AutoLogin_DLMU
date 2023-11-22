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
    file_state,username,password,domain = read_message()
    width, height = 1400,800 #网页宽高
    browser = await pyp.launch(headless=False,
                                args=[
                                # f'–disable-gpu', # GPU硬件加速
                                # f'–disable-dev-shm-usage', # 创建临时文件共享内存
                                # f'–disable-setuid-sandbox', # uid沙盒
                                # f'–no-first-run', # 没有设置首页。在启动的时候，就会打开一个空白页面。
                                # f'–no-sandbox', # 沙盒模式
                                # f'–no-zygote',
                                # f'–single-process' # 单进程运行
                                f'--window-size={width},{height}'],
                                userdataDir = "C:\\Users\\Dr.Y\\Desktop",
                            )
    page = await browser.newPage()
    await antiAntiCrawler(page)
    await page.setViewport({'width': width, 'height':height})
    # async def intercept_request(req):
    #     if req.resourceType in ['image', 'stylesheet', 'font']:
    #         await req.abort()
    #     else:
    #         await req.continue_()
    # await page.setRequestInterception(True)
    # page.on('request', lambda req: asyncio.ensure_future(intercept_request(req)))
    await page.goto(loginUrl, {'timeout': 60000})
    await page.waitForNavigation()# 等待新的网页装入完毕，并不保险，有可能一下跳好几个文件
    time.sleep(10) #等待网页加载

    # 若手动登录，则一下若干行可以去掉
    element = await page.querySelector("#login-normal > div:nth-child(2) > form > div.login-normal-item.ant-row.ng-star-inserted > nz-input-group > input")
    await element.type(str(username))
    element = await page.querySelector("#login-normal > div:nth-child(2) > form > div.login-normal-item.passwordInput.ant-row > nz-input-group > input")
    await element.type(str(password))
    element = await page.querySelector("#login-normal > div:nth-child(2) > form > div.login-normal-button.ant-row > div > button > span")#找到登录按钮，"#"代表id属性
    time.sleep(random.randint(1, 10)) #输入别太快    

    await element.click()#点击登录按钮; 异步协程，立即返回，不等待; 若操作下个页面则会出错
    await page.waitForNavigation(), #加载下一个网页
    # 若手动登录，上面若干行可以去掉
    time.sleep(random.randint(1, 10)) #等待登录完成
    print("已登录")
    await browser.close()

def autologin_pyppeteer():
    #是永久的吗？
    print("logining")
    read_message()
    # url = "https://id.dlmu.edu.cn/login?service=http%3A%2F%2F202.118.88.9%2Feportal%2Findex.jsp%3Fwlanuserip%3De9f6276ead07a8898d26e726ce8bc542%26wlanacname%3Dc20f646d18ec8420743bb59779d3aa5d%26ssid%3D%26nasip%3D321b8c06ed4b01461a74c22a11633718%26snmpagentip%3D%26mac%3Df829acacc6e60116edc2607f84e1b916%26t%3Dwireless-v2%26url%3D137959cd1821ef106bb9c54cf5e2fcecb2b61ecf1f18ce09a8820eaa59596fab9f8aef8adda54e5d%26apmac%3D%26nasid%3Dc20f646d18ec8420743bb59779d3aa5d%26vid%3D6121f950533a4bd1%26port%3D1f897c6a120b51aa%26nasportid%3Dc6abed3ee205e3f81369f2aee75d9658793233c2c2ba139ad6600e266c032f8d7f91717f7fc80086"
    url = "https://id.dlmu.edu.cn/login?service=http:%2F%2F202.118.88.9%2Feportal%2Findex.jsp%3Fwlanuserip%3De9f6276ead07a8898d26e726ce8bc542%26wlanacname%3Dc20f646d18ec8420743bb59779d3aa5d%26ssid%3D%26nasip%3D321b8c06ed4b01461a74c22a11633718%26snmpagentip%3D%26mac%3Df829acacc6e60116edc2607f84e1b916%26t%3Dwireless-v2%26url%3Dba89be7f1fb5bf76c7c21d5e78a4bb46db7404fdfae1ba7ecb96f7d8f9ef275bc2ea29441f0f9b828e33c91b499b916b2877795b9a17c8b4d5b8df94bcddf2fa%26apmac%3D%26nasid%3Dc20f646d18ec8420743bb59779d3aa5d%26vid%3D6121f950533a4bd1%26port%3D1f897c6a120b51aa%26nasportid%3Dc6abed3ee205e3f81369f2aee75d9658793233c2c2ba139ad6600e266c032f8d7f91717f7fc80086"
    asyncio.get_event_loop().run_until_complete(getOjSourceCode(url)) # 协程启动！
