# -*-coding:utf-8-*-
'''
使用post方法对有道进行在线翻译 

通过抓取有道词典的在线翻译   http://fanyi.youdao.com/
抓取有道词典的请求头信息，来进行POST提交，进行在线翻译

有道的请求头
POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
Host: fanyi.youdao.com
Proxy-Connection: keep-alive
Content-Length: 209
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://fanyi.youdao.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://fanyi.youdao.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: _ntes_nnid=1137c1e9883cff16999be4aab1e1d797,1498894433080; OUTFOX_SEARCH_USER_ID_NCOO=1914719784.6467974; OUTFOX_SEARCH_USER_ID=1284781035@122.226.185.113; JSESSIONID=aaay4thmnwBSb5l81rp4v; ___rl__test__cookies=1503494985244

i=I+love++Python&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1503494985247&sign=ceadbb605aceeb14ec60bc6e717686ec&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=true

=====================================
WebForms：

i	I love  Python
from	AUTO
to	AUTO
smartresult	dict
client	fanyideskweb
salt	1503494985247
sign	ceadbb605aceeb14ec60bc6e717686ec
doctype	json
version	2.1
keyfrom	fanyi.web
action	FY_BY_REALTIME
typoResult	true



'''

import urllib
import urllib2

# POST请求的目标URL
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers={"User-Agent": "Mozilla...."}

# 要翻译的信息：
# txt="i love python"
txt="性"

# 里面使用的是用Fidder 抓取的WebForms信息
formdata = {
    "type":"AUTO",
    "i":txt,
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)
print response.read()

'''
发送POST请求时，需要特别注意headers的一些属性：
Content-Length: 144： 是指发送的表单数据长度为144，也就是字符个数是144个。
X-Requested-With: XMLHttpRequest ：表示Ajax异步请求。
Content-Type: application/x-www-form-urlencoded ： 表示浏览器提交 Web 表单时使用，表单数据会按照 name1=value1&name2=value2 键值对形式进行编码。
'''