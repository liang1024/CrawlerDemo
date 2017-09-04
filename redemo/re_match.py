# coding=utf-8
'''
re模块中match()的使用
match 方法用于查找字符串的头部（也可以指定起始位置），它是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果。它的一般使用形式如下：
match(string[, pos[, endpos]])
其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。因此，当你不指定 pos 和 endpos 时，match 方法默认匹配字符串的头部。
当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。

例子1：
例子2：
'''
import re

# 例子1：
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print m

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print m

# 匹配成功
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print m

print m.group(0)   # 可省略 0
print m.start()
print m.end(0)
print m.span(0)


'''
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。
'''
# 例子2
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写

m = pattern.match('Hello World Wide Web')

print m     # 匹配成功，返回一个 Match 对象

print m.group(0)  # 返回匹配成功的整个子串
print m.span(0)   # 返回匹配成功的整个子串的索引
print m.group(1)  # 返回第一个分组匹配成功的子串
print m.span(1)   # 返回第一个分组匹配成功的子串的索引
print m.group(2)  # 返回第二个分组匹配成功的子串
print m.span(2)   # 返回第二个分组匹配成功的子串
print m.groups()  # 等价于 (m.group(1), m.group(2), ...)

# m.group(3)   # 不存在第三个分组，会报错