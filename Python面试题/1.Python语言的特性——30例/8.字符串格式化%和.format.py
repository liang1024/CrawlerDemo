# coding=utf-8
'''
8 字符串格式化:%和.format

参考：http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

'''
name = "123"
print "hi there %s" % name

name = (1, 2, 3)
# print "hi there %s" % name  # 它将会抛出一个TypeError异常
# 为了保证它总是正确的,你必须这样做:
print "hi there %s" % (name,)  # 提供一个单元素的数组而不是一个参数

# .format在许多方面看起来更便利.
print "hi there {0}" .format(name)