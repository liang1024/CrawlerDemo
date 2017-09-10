#coding=utf-8
import requests
from bs4 import BeautifulSoup as bs
import re
import pymysql.cursors
import threading
def getHtml():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    html=requests.get("http://www.xicidaili.com/",headers=headers).text

    Country=""
    ipAddress=""
    port=""
    serverAddress=""
    isAnonymous=""
    httpType=""
    survivalTime=""
    verificationTime=""
    isDetele=""

    # print html
    # print re.findall("<div class=\"main\">.+",html)
    ipitem=re.split(" </tr>", html)

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='971019',
                                 db='proxy',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            for i in range(1,len(ipitem)-1):
                print "*"*100
                print ipitem[i]
                detailItem=re.split("<td>",ipitem[i])
                Country="中国"
                isDetele="0"
                for i in range(1,len(detailItem)):
                    # print len(detailItem)
                    # print i
                    detail=detailItem[i].replace(" ", "").replace("</td>", "")
                    if "<tdclass=\"country\">" in detail:
                        # print detail+"================"
                        print re.split("<tdclass=\"country\">",detail)[0]
                        serverAddress=re.split("<tdclass=\"country\">",detail)[0]
                        print "*" * 10
                        print re.split("<tdclass=\"country\">",detail)[1]
                        isAnonymous=re.split("<tdclass=\"country\">",detail)[1]
                    else:
                        print detail
                        if i ==1:
                            ipAddress=detail
                        elif i==2:
                            port=detail
                        elif i==4:
                            httpType=detail
                        elif i==5:
                            survivalTime=detail
                        elif i==6:
                            verificationTime=detail
                    print "*" * 10

                    # Create a new record
                sql = "INSERT INTO `xici` (`Country`, `ipAddress`, `port`, `serverAddress`, `isAnonymous`," \
                          " `httpType`, `survivalTime`, `verificationTime`, `isDetele`)" \
                          " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(Country,ipAddress,port,serverAddress,isAnonymous,
                httpType,survivalTime,verificationTime,isDetele))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
    finally:
        connection.close()

def coonectMysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='971019',
                                 db='proxy',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `xici`"
            cursor.execute(sql)
            # result = cursor.fetchone()
            result = cursor.fetchall()
            print result
            print type(result)
    finally:
        connection.close()

class MyThread(threading.Thread):
    def run(self):
        print "*" * 50
        print "这是第" + str(i) + "个"


def getIpState(item,i):
    print "第"+str(i)+"任务开启"

    if str(item["httpType"]).strip("\n") == "HTTPS":
        print "我是Https"
        proxies = {
            "https": str(item["ipAddress"].strip("\n")) + ":" + str(item["port"].strip("\n")),
        }
        url = "https://www.baidu.com/"
    elif str(item["httpType"]).strip("\n") == "HTTP":
        print "我是Http"
        proxies = {
            "http": str(item["ipAddress"].strip("\n")) + ":" + str(item["port"].strip("\n")),
        }
        url = "http://www.baidu.com/"
    else:
        print "我不是http也不是https"

    try:
        response = requests.get(url=url, proxies=proxies)
        print response.status_code
        print "验证成功，代理有效"
    except Exception as e:
        print "验证成功，代理无效"


def verificationIp():
    result=[]
    url=""
    proxies={}
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='971019',
                                 db='proxy',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `xici`"
            cursor.execute(sql);            # result = cursor.fetchone()
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    print "代理总数："+str(len(result))
    for i in range(len(result)):
        print i
        th=threading.Thread(target=getIpState(result[i],i))
        th.setDaemon(True)
        th.start()

    print "检测完成====="
    # proxies = {
    #     "http": "http://180.168.179.193:8080",
    #     "https": "http://12.34.56.79:9527",
    # }
    #
    # response = requests.get("http://www.baidu.com", proxies=proxies)
    # print response.text


if __name__ == '__main__':
    # getHtml()
    # coonectMysql()
    verificationIp()
    # response = requests.get("https://www.baidu.com")
    # proxies = {
    #     "https": "http://39.88.13.3:53281",
    #     # "http": "http://221.215.234.229:8118",
    # }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # request = requests.get("https://www.baidu.com", headers=headers,proxies=proxies)
    # print request.url
    # print request.text
