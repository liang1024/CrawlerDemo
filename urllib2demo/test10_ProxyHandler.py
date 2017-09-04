# coding=utf-8
'''
urllib2中通过ProxyHandler来设置使用代理服务器
使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。
很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。
所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

常用的代理：
西刺免费代理IP  http://www.xicidaili.com/
快代理免费代理  http://www.kuaidaili.com/free/inha/
Proxy360代理   http://www.proxy360.cn/default.aspx
全网代理IP    http://www.goubanjia.com/free/index.shtml

高匿：只能看到代理ip,不能看到被代理电脑的物理ip
透明:可以看到被代理电脑ip

'''
import urllib2

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
# 参数为 {"http/https":"ip地址:端口"}
httpproxy_handler = urllib2.ProxyHandler({"http": "180.168.179.193:8080"})
nullproxy_handler = urllib2.ProxyHandler({})

proxySwitch = True  # 定义一个代理开关

# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request("http://www.baidu.com/")

# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理
response = opener.open(request)



    # 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
    # urllib2.install_opener(opener)
    # response = urlopen(requestdemo)
print response.read()



def d2():
    import urllib2
    import random

    proxy_list = [
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"}
    ]

    # 随机选择一个代理
    proxy = random.choice(proxy_list)
    # 使用选择的代理构建代理处理器对象
    httpproxy_handler = urllib2.ProxyHandler(proxy)

    opener = urllib2.build_opener(httpproxy_handler)

    request = urllib2.Request("http://www.baidu.com/")
    response = opener.open(request)
    print response.read()
