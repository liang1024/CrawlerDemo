#coding=utf-8
'''
1.打印百度网页源代码的字符串
'''

# 导入urllib2 库
# urllib2 在 python3.x 中被改为urllib.request
import urllib2

def def1():

    # url 作为Request()方法的参数，构造并返回一个Request对象
    # request = urllib2.Request("http://www.baidu.com")
    # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    # response = urllib2.urlopen(request)

    # 以上两句也可以用下面一句替代
    # 向指定的url发送请求，并返回服务器响应的类文件对象
    response = urllib2.urlopen("http://www.baidu.com")

    # 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
    html = response.read()

    # 打印字符串
    print html

if __name__ == '__main__':
    def1()
