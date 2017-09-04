# coding=utf-8
'''
有些Web服务器（包括HTTP/FTP等）访问时，需要进行用户身份验证，爬虫直接访问会报HTTP 401 错误，表示访问身份未经授权：

urllib2.HTTPError: HTTP Error 401: Unauthorized

如果我们有客户端的用户名和密码，我们可以通过下面的方法去访问爬取：
'''


import urllib
import urllib2

# 用户名
user = "test"
# 密码
passwd = "123456"
# Web服务器 IP
webserver = "http://192.168.199.107"

# 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 Web服务器、用户名、密码
passwdmgr.add_password(None, webserver, user, passwd)

# 3. 构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

# 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler
opener = urllib2.build_opener(httpauth_handler)

# 5. 可以选择通过install_opener()方法定义opener为全局opener
urllib2.install_opener(opener)

# 6. 构建 Request对象
request = urllib2.Request("http://192.168.199.107")

# 7. 定义opener为全局opener后，可直接使用urlopen()发送请求
response = urllib2.urlopen(request)

# 8. 打印响应内容
print response.read()