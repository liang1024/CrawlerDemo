# coding=utf-8
'''
23 Python里的拷贝

copy：浅拷贝。只拷贝父对象，不会拷贝对象的内部的子对象
deepcopy：深拷贝。拷贝对象及其子对象

'''
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print 'a = ', a
print id(a)
print 'b = ', b
print id(b)
print 'c = ', c
print id(c)
print 'd = ', d
print id(d)
