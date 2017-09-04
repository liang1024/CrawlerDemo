# coding=utf-8
'''
7.Python中单下划线和双下划线

参考：http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python
或者: http://www.zhihu.com/question/19754941

'''


# 例子
class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"


class my2(MyClass):
    pass

m2 = my2()
print m2._semiprivate
mc = MyClass()

# print mc.__superprivate       #会报错，报出以下异常
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: myClass instance has no attribute '__superprivate'

print mc._semiprivate

print mc.__dict__  # 查看实例对象的属性

'''
__foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突.
_foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.
__foo:这个有真正的意义:解析器用_classname__foo来代替这个名字,以区别和其他类相同的命名.

'''
