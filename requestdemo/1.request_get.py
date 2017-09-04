# coding=utf-8
'''
Requests 继承了urllib2的所有特性。Requests支持HTTP连接保持和连接池，
支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，
支持国际化的 URL 和 POST 数据自动编码。

开源地址：https://github.com/kennethreitz/requests
中文文档 API： http://docs.python-requests.org/zh_CN/latest/index.html
安装：
 pip install requests
 
最基本的GET请求：
'''
import requests

response = requests.get("http://www.baidu.com/")
# 也可以这么写
# response = requests.request("get", "http://www.baidu.com/")

print response.text