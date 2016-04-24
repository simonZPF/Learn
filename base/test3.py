# -*-coding:utf8-*-
# class hello(object):
#     def h(self):
#         print "hello"
# h=hello()
# print type(h)# h实例 是class 类型
# print type(hello) #hello 是type类型
# def fn(self,name="world"):
#     print ("my name is %s" % name)
# Hello = type('Hello', (object,), dict(hello=fn))#class的名称,继承的父类集合,class的方法名称与函数绑定
# h=Hello()
# h.hello()

# class ListMetaclass(type):
#     def __new__(cls,name,base,attr):
#         attr["add"]=lambda self,value:self.append(value)
#         return type.__new__(cls,name,base,attr)
# class mylist(list):
#     __metaclass__ = ListMetaclass
# l=mylist()
# l.add(1)
# print l

# class Field(object):
#     def __init__(self,name,column_type):
#         self.name=name
#         self.column_type=column_type
#     def __str__(self):
#         return "<%s:%s>" % (self.__class__.__name__,self.name)
#
# class StringField(Field):
#     def __init__(self,name):
#         super(StringField,self).__init__(name,'varchar(100)')
#
# class IntegerField(Field):
#     def __init__(self,name):
#         super(IntegerField,self).__init__(name,'bigint')
#
# class ModelMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         if name=="Model":
#             return type.__new__(cls,name,bases,attrs)
#         mappings =dict()
#         for k,v in attrs.iteritems():
#             if isinstance(v,Field):
#                 print('Found mapping: %s==>%s' % (k,v))
#                 mappings[k] = v
#         for k in mappings.iterkeys():
#             attrs.pop(k)
#         attrs["__table__"] =name
#         attrs["__mappings__"]=mappings
#         return type.__new__(cls,name,bases,attrs)
#
#
# class Model(dict):
#     __metaclass__ = ModelMetaclass
#
#     def __init__(self,**kw):
#         super(Model,self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key]=value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k,v in self.__mappings__.iteritems():
#             fields.append(v.name)
#             params.append("?")
#             args.append(getattr(self,k,None))
#         sql = "insert into %s (%s) values (%s)" % (self.__table__
#                                                    ,",".join(fields),",".join(params))
#         print("SQL: %s" % sql)
#         print("ARGS: %s" % str(args))
#
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()
# print u.id

# logging Error
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except StandardError, e:
#         logging.exception(e)
# print 'start'
# main()
# print 'END'

#raise error
# class FooError(StandardError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo(0)

#debug
#   assert #启动Python解释器时可以用-O参数来关闭assert：
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     print foo(0)
#
# main()
#   logging
# import logging
# logging.basicConfig(level=logging.INFO)# 有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# s="2"
# n = int(s)
# logging.info(">>>==%d",n)
# print 10/n
#   pdb # low级别的断点调试....
# import pdb
# s=0
# pdb.set_trace()
# print 10/s

# 测试 ???
# class Dict(dict):
#
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# import unittest
# class TestDict(unittest.TestCase):
#     def setUp(self):    #在每次测试之前调用
#         print 'setUp...'
#
#     def tearDown(self):
#         print 'tearDown...'
#
#     def test_init(self):
#         d= Dict(a=1,b='test')
#         self.assertEqual(d.a,1)
#         self.assertEquals(d.b,'test')
#         self.assertTrue(isinstance(d,dict))
#
#     def test_key(self):# 函数必须以test开头
#         d=Dict()
#         d["key"]='value'
#         self.assertEquals(d.key,'value')
#
#     def test_attr(self):
#         d=Dict()
#         d.key='value'
#         self.assertTrue('key' in d)
#         self.assertEquals(d['key'],'value')
#
#     def test_keyerror(self):
#         d=Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d=Dict()
#         with self.assertRaises(AttributeError):
#             value= d.empty
#
# unittest.main()

# 文档测试 ?
# def multiply(a,b):
#     """
#     >>> multiply(2,3)
#     6
#     >>> multiply('baka~',3)
#     'baka~baka~baka~'
#     """
#     return a*b
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)