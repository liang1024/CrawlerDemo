# coding=utf-8
'''
22.Python函数式编程
参考：
https://coolshell.cn/articles/10822.html

包括以下方法：
filter()
map()
reduce()
'''


'''
filter
filter 函数的功能相当于过滤器。
调用一个布尔函数bool_func来迭代遍历每个seq中的元素；
返回一个使bool_seq返回值为true的元素的序列。
'''
def filter_demo():
    a = [1, 2, 3, 4, 5, 6, 7]
    b=filter(lambda x:x>5,a)
    print b
'''
map:
map函数是对一个序列的每个项依次执行函数，
下面是对一个序列每个项都乘以2：
'''
def map_demo():
    a=map(lambda x:x*2,[1,2,3])
    list(a)

'''
reduce
reduce函数是对一个序列的每个项迭代调用函数，下面是求3的阶乘：
'''
def reduce_demo():
    a=reduce(lambda x,y:x*y,range(1,4))
    print a

if __name__ == '__main__':
    filter_demo()
    map_demo()
    reduce_demo()