# coding=utf-8
'''
proxies:代理
如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求：

也可以通过本地环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理：

export HTTP_PROXY="http://12.34.56.79:9527"
export HTTPS_PROXY="https://12.34.56.79:9527"

方法说明：
    d1() ：使用proxies进行代理
    d2() ：使用request进行私密代理
    d3() ：使用request对web客户端验证进行处理

'''
import requests


def d1():
    '''
    根据协议类型，选择不同的代理
    :return: 
    '''
    proxies = {
        "http": "http://180.168.179.193:8080",
        "https": "http://12.34.56.79:9527",
    }

    response = requests.get("http://www.baidu.com", proxies=proxies)
    print response.text


def d2():
    '''
    私密代理验证（特定格式） 
    :return: 
    '''
    # 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
    proxy = {"http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816"}

    response = requests.get("http://www.baidu.com", proxies=proxy)

    print response.text


def d3():
    '''
    Web客户端验证（auth
        参数）
    '''
    auth = ('test', '123456')

    response = requests.get('http://192.168.199.107', auth=auth)

    print response.text


if __name__ == '__main__':
    d1()  # 使用proxies进行代理
    d2()  # 使用request进行私密代理
    d3()  # 使用request对web客户端验证进行处理
