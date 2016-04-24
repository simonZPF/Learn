# -*-coding:utf8-*-
#协程
# import time
# def consumer():
#     r=''
#     while True:
#         n = yield r
#         print '[CONSUMER] Consuming %s...' % n
#         time.sleep(1)
#         r='200 ok'
# def produce(c):
#     c.next()
#     n=0
#     while n<5:
#         n=n+1
#         print '[PRODUCER] Producing %s...' % n
#         r=c.send(n)
#         print '[PRODUCER] Consumer return: %s' % r
#     c.close()
# if __name__ == '__main__':
#     c=consumer()
#     produce(c)

# class Parent(object):
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# class Child3(Child1,Child2):
#     pass
# class Child4(Child2,Child1):
#     pass
# print Parent.x, Child1.x, Child2.x, Child3.x, Child4.x
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x, Child3.x, Child4.x
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x, Child3.x, Child4.x
# Child2.x= 4
# print Parent.x, Child1.x, Child2.x, Child3.x, Child4.x

#----yield----
# def h():
#     print 'Wen Chuan'
#     yield 5
#     print 'Fighting!'
#     yield 3
# c = h()
# c.next()
# c.next()

# def h():
#     print 'Wen Chuan'
#     m=yield 5
#     print m
#     print 'Fighting!'
#     yield 3
# c = h()
# #c.close()
# b = c.next()
# print "b=%s" % b
# b = c.send("heheda")
# print "b=%s" % b

# def choose_class(name):
#     if name == 'foo':
#         class Foo(object):
#             def __init__(self):
#                 self.x=1
#         return Foo
#     # 返回的是类，不是类的实例
#     else:
#         Bar=type("Bar",(object,),{"x":2})
#         return Bar
#
# MyClass = choose_class('foo')
# print MyClass().x

# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#
#     '''返回一个类对象，将属性都转为大写形式'''
#     print future_class_name
#     print future_class_parents
#     print future_class_attr
#     #  选择所有不以'__'开头的属性
#     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
#     # 将它们转为大写形式
#     uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#     # 通过'type'来做类对象的创建
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
# class Foo(object):
#     __metaclass__ = upper_attr
# # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
#     bar = 'bip'
# print hasattr(Foo, 'bar')
# print hasattr(Foo, 'BAR')
# f = Foo()
# print f.BAR

# pythonic and non-pythonnic
# strList = ["Python", "is", "good"]
# res =  ' '.join(strList)
#
# res = ''
# for s in strList:
#     res += s + ' '
# dic = {'name':'Tim', 'age':23}
# dic['workage'] = dic.get('workage',0) + 1
#
# if 'workage' in dic:
#     dic['workage'] += 1
# else:
#     dic['workage'] = 1
# a=3
# b = a > 5 and  "aa" or  "hh"
# print b
# array = [1, 2, 3, 4, 5]
# for i, e in enumerate(array,0):
#     print i, e
#
# for i in xrange(len(array)):
#     print i, array[i]

# get file type
# import struct
# # 支持文件类型
# # 用16进制字符串的目的是可以知道文件头是多少字节
# # 各种文件头的长度不一样，少则2字符，长则8字符
# """
# JPEG (jpg) FFD8FF
# PNG (png) 89504E47
# GIF (gif) 47494638
# TIFF (tif) 49492A00
# Windows Bitmap (bmp) 424D
# CAD (dwg) 41433130
# Adobe Photoshop (psd) 38425053
# Rich Text Format (rtf) 7B5C727466
# XML (xml) 3C3F786D6C
# HTML (html) 68746D6C3E
# Email [thorough only] (eml) 44656C69766572792D646174653A
# Outlook Express (dbx) CFAD12FEC5FD746F
# Outlook (pst) 2142444E
# MS Word/Excel (xls.or.doc) D0CF11E0
# MS Access (mdb) 5374616E64617264204A
# """
# def typeList():
#   return {
#     "FFD8FF": "JPEG",
#     "89504E47": "PNG"}
#
# # 字节码转16进制字符串
# def bytes2hex(bytes):
#   num = len(bytes)
#   hexstr = u""
#   for i in range(num):
#     t = u"%x" % bytes[i]
#     if len(t) % 2:
#       hexstr += u"0"
#     hexstr += t
#   return hexstr.upper()
#
# # 获取文件类型
# def filetype(filename):
#   binfile = open(filename, 'rb') # 必需二制字读取
#   tl = typeList()
#   ftype = 'unknown'
#   for hcode in tl.keys():
#     numOfBytes = len(hcode) / 2 # 需要读多少字节
#     binfile.seek(0) # 每次读取都要回到文件头，不然会一直往后读取
#     hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes)) # 一个 "B"表示一个字节
#     f_hcode = bytes2hex(hbytes)
#     if f_hcode == hcode:
#       ftype = tl[hcode]
#       break
#   binfile.close()
#   return ftype
#
# if __name__ == '__main__':

# print divmod(9,2)
# print divmod(10,3)

# 反编码
f='\u53eb\u6211'

print f.decode('unicode-escape')