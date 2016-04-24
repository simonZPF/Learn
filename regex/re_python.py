# encoding:utf-8

import re

# pattern = re.compile(r'hello')
#
# match = pattern.match("hello world! hello")
# match.group()
#
# m=re.match(r"hello","hello world!")#匹配开始
# print m.group()

# m=re.search(r"dog","cat dog dog")#匹配任意位置它查找到一个匹配项之后停止继续查找
# print m.group()
#
# print m.start()#match和search返回一个match对象 可以调用start和end方法

# print m.end()

# m=re.findall(r"dog","dog catdog")#所有匹配对象
# print m

#contactInfo = 'Doe, John: 555-1212'
#print re.search(r'\w+, \w+: \S+', contactInfo).group()

# match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
# print match.group(0)#第0个组被预留来存放所有匹配对象
# print match.group(1)
# print match.group(2)
# print match.group(3)
# match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
# print match.group('last')
# print match.group('first')
# print match.group('phone')

# print re_python.findall(r'(\w+), (\w+): (\S+)', contactInfo)