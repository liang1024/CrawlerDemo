# coding=utf-8
'''
cookielib 库
该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。
MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。
LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。
其实大多数情况下，我们只用CookieJar()，如果需要和本地文件交互，就用 MozillaCookjar() 或 LWPCookieJar()

获取Cookie，并保存到CookieJar()对象中:

'''
import urllib2
import cookielib

# 构建一个CookieJar对象实例来保存cookie
cookiejar = cookielib.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler=urllib2.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urllib2.build_opener(handler)

# 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

## 可以按标准格式将保存的Cookie打印出来
cookieStr = ""
for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

## 舍去最后一位的分号
print cookieStr[:-1]

# 访问百度的cookie
# BAIDUID=2A108097B1287DB74FC03B94FEADCD3E:FG=1;BIDUPSID=2A108097B1287DB74FC03B94FEADCD3E;H_PS_PSSID=1430_21085_18559_17001_20927;PSTM=1503568203;BDSVRTM=0;BD_HOME=0