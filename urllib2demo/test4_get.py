#coding=utf-8
'''
GET方法
直接拼接在url后，如百度这个

https://www.baidu.com/s?wd=Python爬虫
可以进行百度搜索Python爬虫
会被转换为：
https://www.baidu.com/s?wd=python%E7%88%AC%E8%99%AB

'''
import urllib      #负责url编码处理
import urllib2

url = "http://www.baidu.com/s"
word = {"wd":"Python爬虫"}
word = urllib.urlencode(word) #转换成url编码格式（字符串）
newurl = url + "?" + word    # url首个分隔符就是 ?

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(newurl, headers=headers)

response = urllib2.urlopen(request)

print response.read()