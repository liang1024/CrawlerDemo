#coding=utf-8
import urllib
word = {"wd" : "传智播客"}

# 通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
print urllib.urlencode(word)

# 结果
# wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2