# coding=utf-8
'''
参考：
https://stackoverflow.com/questions/674304/pythons-use-of-new-and-init

__new__是一个静态方法,而__init__是一个实例方法.
__new__方法会返回一个创建的实例,而__init__什么都不返回.
只有在__new__返回一个cls的实例时后面的__init__才能被调用.
当创建一个新实例时调用__new__,初始化一个实例时用__init__.
'''

class Test(object):
    def __init__(self):
        print '我是__init__方法'
    def __new__(cls, *args, **kwargs):
        print '我是__new__方法,我可以返回一个对象'
        return object.__new__(cls, *args, **kwargs)

Test()