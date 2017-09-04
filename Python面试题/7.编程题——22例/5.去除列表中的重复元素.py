#coding=utf-8
'''
5.去除列表中的重复元素

'''

# 方法1 set集合
l1 = ['b','c','d','b','c','a','a']
print list(set(l1))

# 方法2：用字典
l2 = ['b','c','d','b','c','a','a']
r2 = {}.fromkeys(l1).keys()
print r2

# 用字典并保持顺序
l3 = ['b','c','d','b','c','a','a']
r3 = list(set(l1))
r3.sort(key=l1.index)
print r3

# 3.列表推导式
l4 = ['b','c','d','b','c','a','a']
r4 = []
[r4.append(i) for i in l1 if not i in l2]