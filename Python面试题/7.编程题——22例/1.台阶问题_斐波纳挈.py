#coding=utf-8
'''
1.台阶问题_斐波纳挈

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

三种实现方式：

'''

# 方法1：
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

# 方法2：
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@memo
def fib2(i):
    if i < 2:
        return 1
    return fib2(i-1) + fib2(i-2)

# 方法3：
def fib3(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
        print b
    return b
fib3(10)