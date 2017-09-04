# coding=utf-8
'''
d1():访问网站获得cookie，并把获得的cookie保存在cookie文件中
d2():从文件中获取cookies，做为请求的一部分去访问
'''
import cookielib
import urllib2

def d1():
    # 保存cookie的本地磁盘文件名
    filename = 'cookie.txt'

    # 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
    cookiejar = cookielib.MozillaCookieJar(filename)

    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    handler = urllib2.HTTPCookieProcessor(cookiejar)

    # 通过 build_opener() 来构建opener
    opener = urllib2.build_opener(handler)

    # 创建一个请求，原理同urllib2的urlopen
    response = opener.open("http://www.baidu.com")

    # 保存cookie到本地文件
    cookiejar.save()
    print "保存完成"

def d2():
    # 创建MozillaCookieJar(有load实现)实例对象
    cookiejar = cookielib.MozillaCookieJar()

    # 从文件中读取cookie内容到变量
    cookiejar.load('cookie.txt')

    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    handler = urllib2.HTTPCookieProcessor(cookiejar)

    # 通过 build_opener() 来构建opener
    opener = urllib2.build_opener(handler)

    response = opener.open("http://www.baidu.com")

    print response.read()

if __name__ == '__main__':
    d1()
    # d2()