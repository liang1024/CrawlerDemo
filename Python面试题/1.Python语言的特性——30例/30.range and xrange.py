#coding=utf-8
'''
30.range and xrange
都在循环时使用，xrange内存性能更好。

for i in range(0, 20): for i in xrange(0, 20): 
What is the difference between range and xrange functions in Python 2.X? 
range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
xrange is a sequence object that evaluates lazily.

简述：
range在python2中如果创建range(1, 100000)，将直接开辟100000个内存去存储，浪费内存
而xrange则只会返回以后迭代器对象，需要的时候再去创建相应的值，比range()更省内存

参考：
https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x

'''
