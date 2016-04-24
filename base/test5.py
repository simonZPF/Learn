# -*-coding:utf8 -*-

# Black technology -- collection !!

# namedtuple # 用元组表示点坐标不合适 用class小题大做
# from collections import namedtuple
# Point =namedtuple('Point',['x','y'])
# p=Point(1,2)
# print p.x,p.y
# print isinstance(p,tuple)

#deque 高效实现插入和删除操作的双向列表，适合用于队列和栈
# from collections import deque
# q=deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print q
# q.popleft()

#defaultdict key不存在时 返回一个默认值
# from collections import defaultdict
# dd=defaultdict(lambda :"N/A")
# dd["key1"]="aa"
# print dd["key1"],dd["key2"]

#OrderedDict
from collections import OrderedDict
# #d= dict([("a",1),('b',2),('c',3)])
# d=dict(a=1,b=2,c=3)
# print d
# od =OrderedDict([("a",1),('b',2),('c',3)])
# #od=OrderedDict(a=1,b=2,c=3)#这种还是无序...
# # od.popitem(last=False)
# print od
# class FIFODict(OrderedDict):
#     def __init__(self,capacity):
#         super(FIFODict,self).__init__()
#         self.capacity=capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self)-containsKey >= self.capacity:
#             last=self.popitem(last=False)
#             print 'remove: ',last
#         if containsKey:
#             del self[key]
#             print 'set: ',(key,value)
#         else:
#             print'add: ',(key,value)
#         OrderedDict.__setitem__(self,key,value)
# b=FIFODict(3)
# b['a']=1
# b['b']=2
# b['c']=3
# print b
# print
# b['d']=4
# print b
# print
# b['c']=5
# print b
# for key,value in b.iteritems():
#     print str(key)+u" : "+str(value)

# counter
# from collections import Counter
# c=Counter()
# for ch in "Proogrserpserlag asldg noqwe ":
#     c[ch]+=1
# print c

# base64----------
# import base64 #4字节编译为3节 =号补位
# a=base64.b64encode("ban2++")
# print base64.b64encode("ban2")
# print base64.b64encode("ban23")
# print a
# b=base64.b64decode(a)
# print b
# print base64.b64encode("i\xb7\x1d\xfb\xef\xff") #abcd++//#在Url中不能出现+/
# print base64.urlsafe_b64encode("i\xb7\x1d\xfb\xef\xff") #abcd--__

#struct------
# import struct
# print [struct.pack('>I',10240099)]
# print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')#I：4字节无符号整数和H：2字节无符号整数。
# with open('test.bmp','rb') as f:
#     a=f.read(30)
#     s=struct.unpack("<ccIIIIIIHH",a)
#     if s[0] == 'B' and s[1] == 'M':
#         print 'BMP size is %s * %s' %(s[6],s[7])
#         print 'BMP color is %s' % s[9]
#     else:
#         print 'This is not a bmp image'

#hashlib-----------
# import hashlib
#
# md1=hashlib.md5()
# md2=hashlib.md5()
# md1.update("how to use md5 in python hashlib?")
# md2.update("How to use md5 in python hashlib?")
# print md1.hexdigest()
# print md2.hexdigest()

# itertools-------------
import itertools
#itertools.count(1)#无限循环
#itertools.cycle('ABC')#无限循环
#ns=itertools.repeat("a",10)
# for a,i,x in zip(ns,itertools.count(1),itertools.cycle('ABC')):
#     print a,i,x
# natuals=itertools.count(1)
# def foo(x):
#     return True if x<=10 else False
# ns=itertools.takewhile(lambda x:x<=10,natuals)
#ns=itertools.takewhile(foo,natuals)
# for n in ns:
#     print n

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# for c in itertools.chain('abc','xyz'):
#     print c

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
# for key,group in itertools.groupby("AaaCCsSDdFEGS",lambda u:u.upper()):
#     print key,len(list(group))
# from collections import Counter#对比方法
# c=Counter()
# for ch in "AAACCCSSSDDFEGS":
#     c[ch]+=1
# for key,value in c.iteritems():
#     print key,value
# for x in itertools.imap(lambda x,y:x*y,[10,20,30],itertools.count(1)):
#     print x
# x=itertools.imap(lambda x,y:x*y,[10,20,30],itertools.count(1))
# print x.next()#imap()返回一个迭代对象，而map()返回list
# r=map(lambda x,y,z: x*y*z, [1,2,3],[2,3,4],[1,2,3])
# print r

#生成验证码------------
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg');