# coding=utf-8
'''
re模块中search的使用

search 方法用于查找字符串的任何位置，它也是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果，它的一般使用形式如下：
search(string[, pos[, endpos]])
其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。
当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
例子1：
例子2：
'''
import re

# 例子1:
pattern = re.compile('\d+')
m = pattern.search('one12twothree34four')  # 这里如果使用 match 方法则不匹配

print m
print m.group()

m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
print m

print m.group()

print m.span()


# 例子2:
# 将正则表达式编译成 Pattern 对象
pattern = re.compile(r'\d+')
# 使用 search() 查找匹配的子串，不存在匹配的子串时将返回 None
# 这里使用 match() 无法成功匹配
m = pattern.search('hello 123456 789')
if m:
    # 使用 Match 获得分组信息
    print 'matching string:',m.group()
    # 起始位置和结束位置
    print 'position:',m.span()