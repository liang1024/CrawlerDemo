#coding=utf-8
'''
4.urllib和urllib2的区别

这个面试官确实问过,当时答的urllib2可以Post而urllib不可以.

1.urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。
这是为何urllib常和urllib2一起使用的原因。

2.urllib2可以接受一个Request类的实例来设置URL请求的headers，
urllib仅可以接受URL。这意味着，你不可以伪装你的User Agent字符串等。
'''