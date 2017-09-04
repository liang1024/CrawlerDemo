# -*-coding:utf-8-*-
'''
爬取百度贴吧
输入一个百度贴吧的地址，比如：
百度贴吧LOL吧第一页：http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0
第二页： http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50
第三页： http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=100
kw=lol   lol吧     
pn=*     数量，一页50个

以下方法：
writeFile :保存下载的页面
loadPage :请求下载页面
tiebaSpider ：调度器，负责调度下载和保存
main   : 主方法，python解析器最先执行的方法
'''
import urllib
import urllib2


def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print "正在存储" + filename
    # with open(filename, 'w') as f:
    with open(filename.decode('utf-8'), 'w') as f:
        f.write(html)
    print "-" * 20


def loadPage(url, filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename: 文件名
    '''
    print "正在下载" + filename

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    return response.read()


def tiebaSpider(url, beginPage, endPage):
    """
        作用：负责处理url，分配每个url去发送请求
        url：需要处理的第一个url
        beginPage: 爬虫执行的起始页面
        endPage: 爬虫执行的截止页面
    """

    for page in range(beginPage, endPage + 1):

        pn = (page - 1) * 50  #每页的数量

        filename = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        #print fullurl

        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)


if __name__ == "__main__":
    # 需要爬取的贴吧
    kw ="美女"

    # 输入起始页beginPage和终止页endPage，str转成int类型
    beginPage =1  #从1开始
    endPage = 5

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw" : kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage)
