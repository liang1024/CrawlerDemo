# coding=utf-8
'''



'''

import urllib2
import re


class Spider:
    """
        内涵段子爬虫类
    """
    def loadPage(self, page):
        """
            @brief 定义一个url请求网页的方法
            @param page 需要请求的第几页
            @returns 返回的页面html
        """

        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
        #User-Agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'

        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)
        html = response.read()
        gbk_html = html.decode('gbk').encode('utf-8')
        # print gbk_html

        # 找到所有的段子内容<div class = "f18 mb20"></div> <div class="f18 mb20"> </div>
        # re.S 如果没有re.S 则是只匹配一行有没有符合规则的字符串，如果没有则下一行重新匹配
        # 如果加上re.S 则是将所有的字符串将一个整体进行匹配

        item_list = pattern.findall(gbk_html)

        return item_list

    def printOnePage(self, item_list, page):
        """
            @brief 处理得到的段子列表
            @param item_list 得到的段子列表
            @param page 处理第几页
        """
        print len(item_list)
        print "******* 第 %d 页 爬取完毕...*******" % page
        for item in item_list:
            print "================"
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            print item



if __name__ == '__main__':
    """
    
        ======================
            内涵段子小爬虫
        ======================
    """
    # print '请按下回车开始'
    # raw_input()

    #定义一个Spider对象
    mySpider = Spider()

    mySpider.printOnePage(mySpider.loadPage(1),1)