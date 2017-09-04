#coding=utf-8
'''
基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
使用相关的 Handler处理器 来创建特定功能的处理器对象；
然后通过 urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
使用自定义的opener对象，调用open()方法发送请求。
如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener() 将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

'''
import urllib2

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = urllib2.HTTPHandler()

# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_handler = urllib2.HTTPSHandler()

# 参数debuglevel=1，会将 Debug Log 打开
#  在执行的时候，会把收包和发包的报头在屏幕上自动打印出来
# http_handler = urllib2.HTTPSHandler(debuglevel=1)

# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib2.build_opener(http_handler)

# 构建 Request请求
request = urllib2.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)

# 获取服务器响应内容
print response.read()