#coding=utf-8
'''
4.类变量和实例变量
参考：
http://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block

'''

# 例子1：
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"

print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa

# 例子2：
class Person:
    name=[]
p1=Person()
p2=Person()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print Person.name  # [1]

'''
类变量就是供类使用的变量,实例变量就是供实例使用的.
这其实和函数传参一样,
不可变类型变量在实例对象中被改变后，会重新创建
可变类型则是共享
'''