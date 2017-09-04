#coding=utf-8
'''
1.为请求添加请求头信息
'''
import urllib2

url = "http://www.itcast.cn"

#IE 9.0 的 User-Agent
header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib2.Request(url, headers = header)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
# requestdemo.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
# requestdemo.get_header(header_name="Connection")

response = urllib2.urlopen(request)

print response.code     #可以查看响应状态码
html = response.read()

print html

#使用轮询随机添加
def d2():
    import urllib2
    import random

    url = "http://www.itcast.cn"

    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS... "
    ]

    user_agent = random.choice(ua_list)

    request = urllib2.Request(url)

    # 也可以通过调用Request.add_header() 添加/修改一个特定的header
    request.add_header("User-Agent", user_agent)

    # 第一个字母大写，后面的全部小写
    request.get_header("User-agent")

    response = urllib2.urlopen(req)

    html = response.read()
    print html