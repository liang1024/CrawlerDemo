#coding=utf-8
'''
3.矩形覆盖

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
第2*n个矩形的覆盖方法等于第2*(n-1)加上第2*(n-2)的方法。
'''

# 第2*n个矩形的覆盖方法等于第2*(n-1)加上第2*(n-2)的方法。

f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)
print type(f)