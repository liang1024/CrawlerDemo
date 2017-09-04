# coding=utf-8
'''
3 @staticmethod和@classmethod
参考：
http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:
'''

def foo(x):
    print "executing foo(%s)"%(x)

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()
a.foo("1")
a.class_foo("1")
a.static_foo("1")
A.static_foo("1")  #静态方法可以通过类名直接调用，不需要实例对象

'''
这里先理解下函数参数里面的self和cls.这个self和cls是对类或者实例的绑定,
对于一般的函数来说我们可以这么调用foo(x),这个函数就是最常用的,
它的工作跟任何东西(类,实例)无关.对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,
就是foo(self, x),为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给函数,
调用的时候是这样的a.foo(x)(其实是foo(a, x)).类方法一样,只不过它传递的是类而不是实例,A.class_foo(x).
注意这里的self和cls可以替换别的参数,但是python的约定是这俩,还是不要改的好.
'''