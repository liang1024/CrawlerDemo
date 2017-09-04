#coding=utf-8
'''
28 Python2和3的区别
参考：
https://chenqx.github.io/2014/11/10/Key-differences-between-Python-2-7-x-and-Python-3-x/

1.__future__模块
Python 3.x 介绍的 
一些Python 2 不兼容的关键字和特性可以通过在 Python 2 的内置 __future__ 模块导入。
如果你计划让你的代码支持 Python 3.x，建议你使用 __future__ 模块导入。

2.print函数
Python 2 的 print 声明已经被 print() 函数取代了，这意味着我们必须包装我们想打印在小括号中的对象。

3.整除
如果你正在移植代码，这个变化是特别危险的。或者你在 Python 2 上执行 Python 3 的代码。因为这个整除的变化表现在它会被忽视（即它不会抛出语法异常）。
Python 2
3 / 2 = 1
Python 3
3 / 2 = 1.5

4.Unicode
Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型。
现在， 在 Python 3，我们最终有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。

5.xrange模块
python2中很流行xrange模块
python3中range被xrange被替换，xrange被移除了
Python 3 倾向于比 Python 2 运行的慢一点。

另外返回可迭代对象，而不是列表

python2
print type(range(3))
< type ‘list’>
python3:
print(type(range(3)))
< class ‘range’>

在 Python 3 中一些经常使用到的不再返回列表的函数和方法：
zip()
map()
filter()
dictionary’s .keys() method
dictionary’s .values() method
dictionary’s .items() method


6.range对象的__contains__方法
Python 3 中 range 有一个新的 __contains__ 方法，
__contains__ 方法可以加速 “查找” 在 Python 3.x 中显著的整数和布尔类型。

7.Raising exceptions
python2中语句不会报错，
raise IOError, "file error"

python3中只能使用()包裹
raise IOError("file error")

8.Handling exceptions    python3使用as
python2:
try:
except NameError, err:
    print err, '--> our error message'
Python 3
try:
except NameError as err:
    print(err, '--> our error message')

9.next()函数 and .next()方法
next()    .next()
python2两种都可以用
python3只能使用next()，第二种会报错

9.input()和raw_input()
python2中只能使用raw_input()读取中文,input()不可以
python3中可以直接使用input()进行读取，


10.For循环变量和全局命名空间泄漏
好消息：在 Python 3.x 中 for 循环变量不会再导致命名空间泄漏。
　　在 Python 3.x 中做了一个改变，在 What’s New In Python 3.0 中有如下描述：
　　“列表推导不再支持 [... for var in item1, item2, ...] 这样的语法。
使用 [... for var in (item1, item2, ...)] 代替。也需要提醒的是列表推导有不同的语义：
 他们关闭了在 list() 构造器中的生成器表达式的语法糖, 
 并且特别是循环控制变量不再泄漏进周围的作用范围域.”
'''

# for循环中的变量泄露到了周围的变量
i = 1
print 'before: i =', i
print 'comprehension: ', [i for i in range(5)]
print 'after: i =', i

# python2不会再出现这种情况

'''
11.比较不可排序类型
在 Python 3 中的另外一个变化就是当对不可排序类型做比较的时候，会抛出一个类型错误。
python2中则不会
'''
print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)
