# coding=utf-8
'''
21.lambda函数

参考：
https://www.zhihu.com/question/20125256

通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，
也就是指匿名函数。
'''

# 例子：
# 求0到10的平方

print map(lambda x: x * x, [y for y in range(11)])


# 上面的写法好过下面的写法
def sq(x):
    return x * x

map(sq, [y for y in range(11)])
