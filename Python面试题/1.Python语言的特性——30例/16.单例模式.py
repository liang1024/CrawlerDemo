# coding=utf-8
'''
单列模式
下面列出四种实现模式
1.使用__new__方法
2.共享属性
3.装饰器版本
4.import方法
'''

# 1.使用__new__方法:
class Slingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig=super(Slingleton,cls)
            cls._instance=orig.__new__(cls,*args,**kw)
        return cls._instance
class MyClass(Slingleton):
    a=1

# 2.共享属性
# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
class Borg(object):
    _state={}
    def __new__(cls, *args, **kwargs):
        ob=super(Borg,cls).__new__(cls,*args,**kwargs)
        ob.__dict__=cls._state
        return ob
class MyClass2(Borg):
    a=1

# 3.装饰器版本
def Singleton3(cls,*args,**kw):
    instances={}
    def getinstance():
        if cls not in instances:
            instances[cls]=cls(*args,**kw)
        return instances[cls]
    return getinstance

@Singleton3
class MyClass:
    a=1

# 4 import方法
# 作为python的模块是天然的单例模式
#单独定义一个 mysingleton.py 文件，然后在使用的时候进行导入
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

# to use   使用
# from mysingleton import my_singleton
# my_singleton.foo()
