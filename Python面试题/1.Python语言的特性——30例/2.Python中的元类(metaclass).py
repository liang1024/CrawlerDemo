# coding=utf-8
'''
2.Python中的元类(metaclass)

参考:https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python


在理解元类之前，您需要掌握Python中的类。而Python对于从Smalltalk语言借来的课程有着非常独特的认识。
在大多数语言中，类只是描述如何生成对象的代码段。在Python中也是如此：
Python中的一个对象。这包括int，string，函数和类。他们都是对象。所有这些都是从一个类创建的：

元类是创建类的“东西”。
你定义类来创建对象，对吧？
但是我们了解到Python类是对象。
那么，元类就是创建这些对象。他们是班级的课程，你可以这样画：
MyClass = MetaClass()
MyObject = MyClass()
你看过，type可以让你做这样的事情：
MyClass = type('MyClass', (), {})
这是因为该函数type实际上是一个元类。type是Python用于创建幕后的所有类的元类。
你可以通过检查__class__属性来看看。

type 是Python使用的内置元类，但是当然可以创建自己的元类。
您可以__metaclass__在编写课程时添加属性：
class Foo(object):
  __metaclass__ = something...
  [...]
如果这样做，Python将使用元类创建该类Foo。
Python将__metaclass__在类定义中寻找。如果找到它，它将使用它来创建对象类Foo。如果没有，它将  type用于创建类。


事实上，元类最主要的作用：
拦截类创建
修改类
返回修改的类

元类的主要用例是创建一个API。一个典型的例子就是Django ORM。


元级是更多的魔法，99％的用户不用担心。如果你想知道你是否需要他们，你不会（实际需要的人知道他们需要他们，而不需要解释为什么）。
Python大师蒂姆·彼得斯

'''
