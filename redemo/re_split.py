# coding=utf-8
'''
re模块中split的使用
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
split(string[, maxsplit])
其中，maxsplit 用于指定最大分割次数，不指定将全部分割。
'''
import re
p = re.compile(r'[\s\,\;]+')
print p.split('a,b;; c   d')