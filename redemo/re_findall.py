# coding=utf-8
'''
re模块中的findall 方法
上面的 match 和 search 方法都是一次匹配，只要找到了一个匹配的结果就返回。然而，在大多数时候，我们需要搜索整个字符串，获得所有匹配的结果。
findall 方法的使用形式如下：
findall(string[, pos[, endpos]])
其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。
findall 以列表形式返回全部能匹配的子串，如果没有匹配，则返回一个空列表。
例子1：
例子2：
'''
import re

# 例子1：
pattern = re.compile(r'\d+')   # 查找数字

result1 = pattern.findall('hello 123456 789')
result2 = pattern.findall('one1two2three3four4', 0, 10)

print result1
print result2

# 例子2：
#re模块提供一个方法叫compile模块，提供我们输入一个匹配的规则
#然后返回一个pattern实例，我们根据这个规则去匹配字符串
pattern = re.compile(r'\d+\.\d*')

#通过partten.findall()方法就能够全部匹配到我们得到的字符串
result = pattern.findall("123.141593, 'bigcat', 232312, 3.15")

#findall 以 列表形式 返回全部能匹配的子串给result
for item in result:
    print item