# -*-coding:utf-8-*-
"""
处理HTTPS请求 SSL证书验证
现在随处可见 https 开头的网站，urllib2可以为 HTTPS 请求验证SSL证书，就像web浏览器一样，如果网站的SSL证书是经过CA认证的，则能够正常访问，如：https://www.baidu.com/等...
如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/的时候，会警告用户证书不受信任。（据说 12306 网站证书是自己做的，没有通过CA认证）

d1() ：会报SSL异常，程序崩溃
d2():忽略SSL异常,正常运行

"""
import urllib
import urllib2

def d1():

    url = "https://www.12306.cn/mormhweb/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request)

    print response.read()

def d2():
    # 1. 导入Python SSL处理模块
    import ssl

    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()

    url = "https://www.12306.cn/mormhweb/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    request = urllib2.Request(url, headers=headers)

    # 3. 在urlopen()方法里 指明添加 context 参数
    response = urllib2.urlopen(request, context=context)

    print response.read()

if __name__ == '__main__':
#     会报异常：
# urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)>
#     d1()

#  我们需要单独处理SSL证书，让程序忽略SSL证书验证错误，即可正常访问。
    d2()



'''
关于CA

CA(Certificate Authority)是数字证书认证中心的简称，是指发放、管理、废除数字证书的受信任的第三方机构，如北京数字认证股份有限公司、上海市数字证书认证中心有限公司等...
CA的作用是检查证书持有者身份的合法性，并签发证书，以防证书被伪造或篡改，以及对证书和密钥进行管理。
现实生活中可以用身份证来证明身份， 那么在网络世界里，数字证书就是身份证。和现实生活不同的是，并不是每个上网的用户都有数字证书的，往往只有当一个人需要证明自己的身份的时候才需要用到数字证书。
普通用户一般是不需要，因为网站并不关心是谁访问了网站，现在的网站只关心流量。但是反过来，网站就需要证明自己的身份了。
比如说现在钓鱼网站很多的，比如你想访问的是www.baidu.com，但其实你访问的是www.daibu.com”，所以在提交自己的隐私信息之前需要验证一下网站的身份，要求网站出示数字证书。
一般正常的网站都会主动出示自己的数字证书，来确保客户端和网站服务器之间的通信数据是加密安全的。

'''