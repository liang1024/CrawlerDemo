#coding=utf-8
'''
2.变态台阶问题

一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

fib = lambda n: n if n < 2 else 2 * fib(n - 1)