# coding=utf-8
'''
使用request库对cookie,sission，Https进行处理
方法:
d1(): 存储cookie
d2():人人网列子：存储session   (仅供参考)
d3():12306忽略证书验证

'''

import requests


def d1():
    '''
    存储cookie
    :return: 
    '''
    response = requests.get("http://www.baidu.com/")

    # 7. 返回CookieJar对象:
    cookiejar = response.cookies

    # 8. 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

    print cookiejar

    print cookiedict


def d2():
    '''
    人人网：存储session
    :return: 
    '''
    # 1. 创建session对象，可以保存Cookie值
    ssion = requests.session()

    # 2. 处理 headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 3. 需要登录的用户名和密码
    data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}

    # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
    ssion.post("http://www.renren.com/PLogin.do", data=data)

    # 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    response = ssion.get("http://www.renren.com/410043129/profile")

    # 6. 打印响应内容
    print response.text


def d3():
    '''
    response = requests.get("https://www.12306.cn/mormhweb/")
    # requests.exceptions.SSLError
    
    添加参数verify=False  即可忽略证书验证
    :return: 
    '''
    response = requests.get("https://www.12306.cn/mormhweb/", verify=False)
    print response.text


if __name__ == '__main__':
    d1()  # 存储cookie
    # d2() #人人网存储session(仅供参考)
    # d3()  # https忽略证书验证
