# coding=utf-8
import requests
import cookielib
import re
import os
import time
from lxml import etree
from bs4 import BeautifulSoup as bs

# 将python默认编码改成utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class mm131():
    '''
    爬取mm131
    http://www.mm131.com/xinggan/
http://www.mm131.com/xinggan/list_6_2.html
http://www.mm131.com/xinggan/list_6_3.html
http://www.mm131.com/xinggan/list_6_11.html
    '''
    def __init__(self):
        # self.baseUrl="http://www.mm131.com/xinggan/"
        # self.baseUrl="http://www.mm131.com/qingchun/"
        # self.baseUrl="http://www.mm131.com/xiaohua/"
        # self.baseUrl="http://www.mm131.com/chemo/"
        # self.baseUrl="http://www.mm131.com/qipao/"
        self.baseUrl="http://www.mm131.com/mingxing/"
        self.startPage=2
        self.endPage=11
        # self.basedir="mm131-性感美女"
        # self.basedir="mm131清纯美女"
        # self.basedir="mm131大学校花"
        # self.basedir="mm131车模"
        self.basedir="mm131明星写真"
        self.basedirs="mm131"
        os.mkdir(self.basedir.decode("utf-8"))

        self.headers = {
            "Host": "img1.mm131.com",
            "Referer": self.baseUrl,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    def startController(self):
        '''
        控制方法
        :return: 
        '''
        print "正在爬取第1页图片"
        # self.basedirs=self.basedir + "\\" + "第1页"
        # print self.basedirs
        # os.mkdir(self.basedirs.decode("utf-8"))
        html=self.loadPage(self.baseUrl)
        self.loadData(1,  self.baseUrl ,html)

        # self.saveData(1, html)
        for i in range(self.startPage,self.endPage+1):
            # url="http://www.mm131.com/xinggan/list_6_"+str(i)+".html"
            # url="http://www.mm131.com/qingchun/list_1_"+str(i)+".html"
            # url="http://www.mm131.com/xiaohua/list_2_"+str(i)+".html"
            # url="http://www.mm131.com/chemo/list_3_"+str(i)+".html"
            # url="http://www.mm131.com/qipao/list_4_"+str(i)+".html"
            url="http://www.mm131.com/mingxing/list_5_"+str(i)+".html"
            print "正在爬取第" + str(i) + "图片"
            html=self.loadPage(url)
            self.loadData(i,url,html)

            # self.saveData(i,html)

    def loadPage(self,url):
        '''
        获取网页源代码
        :return: 
        '''

        # request = urllib2.Request(url, headers=headers)
        # response = urllib2.urlopen(request)
        # print response.read().decode("gb2312")
        result=requests.get(url,headers=self.headers,timeout=15)
        print url
        result.encoding="gb2312"
        # print result.text
        return result.text

    def loadData(self,i,url,html):
        '''
        提取详细标签
        :return: 
        '''
        soup=bs(html, "html.parser")
        list=soup.find_all('a')
        # print soup.find_all('a')
        # print "============================"
        if len(soup.find_all('a'))>0:
            self.baseUrl = url
            self.basedirs = self.basedir + "\\" + "第" + str(i) + "页"
            os.mkdir(self.basedirs.decode("utf-8"))

            self.saveExtractImage(list)
        else:
            print "第"+str(i)+"页没有数据"

    def saveExtractImage(self,list):
        '''
        保存网页图片
        :param list: 
        :return: 
        '''
        i = 0
        for item in list:
            # print "========"
            # print item
            pattern =re.compile(r'alt=".+" height="160"')
            Match=pattern.search(str(item))
            if Match:
                i += 1
                resultName=Match.group().replace("\" height=\"160\"","").replace("alt=\"","")
                resultImg=re.compile(r'src="http://.+\.jpg').search(str(item)).group().replace("src=\"","")
                # print self.headers
                result_img = requests.get(resultImg, headers=self.headers,timeout=15)
                if result_img.status_code==200:
                    with open(self.basedirs+"\\"+str(i)+str(resultName)+".jpg".decode("utf-8"), 'wb') as f:
                        print "=====正在下载第" + str(i) + "张:" + resultName
                        f.write(result_img.content)


    def savePageCode(self,page,html):
        '''
        保存数据
        :return: 
        '''
        print "正在保存第"+str(page)+"页"
        # 保存网页方法1：
        # try:
        #     r=open(self.basedir+"\\"+str(page)+".html","w")
        #     r.write(html)
        # except Exception as e:
        #     print e
        # 保存网页方法2：
        with open(self.basedir+"\\"+str(page)+".html","w") as a:
            a.write(html)
            a.close()



if __name__ == '__main__':
    # os.mkdir("mm131_img")
    mm=mm131()
    mm.startController()
    # headers = {
    #     "Host": "img1.mm131.com",
    #     "Referer": "http://www.mm131.com/xinggan//",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    # img=requests.get("http://img1.mm131.com/pic/3125/0.jpg",headers=headers)
    # print img
    # with open('2.jpg', 'wb') as f:
    #     f.write(img.content)