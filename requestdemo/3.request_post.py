# coding=utf-8
"""
使用request完成POST请求

最基本的GET请求可以直接用post方法
# response = requests.post("http://www.baidu.com/", data = data)

d1():使用request进行POST提交到有道翻译 进行翻译
d2():使用request进行POST提交到百度翻译 进行翻译

"""

# 基本POST请求（data参数）


import requests


def d1():
    formdata = {
        "type": "AUTO",
        "i": "i love python",
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_ENTER",
        "typoResult": "true"
    }

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    response = requests.post(url, data=formdata, headers=headers)

    # print response.text

    # 如果是json文件可以直接显示
    print response.json()


def d2():
    formData = {
        "from": "en",
        "query": "I love Python",
        "simple_means_flag": "	3",
        "to": "zh",
        "transtype": "	translang",
    }
    url = "http://fanyi.baidu.com/v2transapi"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    response = requests.post(url, data=formData, headers=headers)

    # print response.text

    # 如果是json文件可以直接显示
    print response.json()


if __name__ == '__main__':
    d1() #有道翻译
    print "=+"*50
    d2() #百度翻译