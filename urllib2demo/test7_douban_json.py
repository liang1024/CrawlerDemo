# -*-coding:utf-8-*-
"""
通过请求豆瓣电影页面进行抓包，获取豆瓣返回的json串

"""
import urllib
import urllib2

# demo1
def demo1():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

    headers = {"User-Agent": "Mozilla...."}

    # 变动的是这两个参数，从start开始往后显示limit个
    formdata = {
        'start': '0',
        'limit': '10'
    }
    data = urllib.urlencode(formdata)

    request = urllib2.Request(url, data=data, headers=headers)
    response = urllib2.urlopen(request)

    print response.read()


# demo2
def demo2():
    url = "https://movie.douban.com/j/chart/top_list?"
    headers = {"User-Agent": "Mozilla...."}

    # 处理所有参数
    formdata = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '10'
    }
    data = urllib.urlencode(formdata)

    request = urllib2.Request(url, data=data, headers=headers)
    response = urllib2.urlopen(request)

    print response.read()

if __name__ == '__main__':
    # demo1()
    demo2()