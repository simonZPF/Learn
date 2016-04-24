# -*-coding:utf8-*-
import functools
# d={'a':1,'b':2,'c':3}
# for key in d:
#     print key
# for key in d.itervalues():
#     print key
# for key,value in d.iteritems():
#     print key
# for i in enumerate(['a','b','c']):
#     print i
# print [m+n for m in "ab" for n in "xyz"]
# l=[x*x for x in range(10)]
# print l
# k=(x*x for x in range(10))
# print k.next()
# def fib(max):
#     n,a,b=0,0,1
#     while (n<max):
#         yield b
#         a,b=b,a+b
#         n=n+1
# a=fib(6)
# print a.next()
# def add(x,y,f):
#     return f(x)+f(y)
# print add(-1,10,abs)
#print map(str,[1,2,3,4,5])

# def fn(x,y):
#     return 10*x+y
# print reduce(fn,[1,0,3,4,5])

# def f(x):
#     return x%3==0
# print filter(f,[1,5,6,7,3,18,3,4])

# def f(x,y):
#     return -1 if x>y else 1
# print sorted([5,6,3,8,1],f)

# def lazy_sum(*args):
#     def mysum():
#         n=0
#         for i in args:
#             n+=i
#         return n
#     return mysum
# f=lazy_sum(1,2,3,4,5,6)
# print f()

# def count():
#     fs=[]
#     for i in range(1,4):
#         def g():
#             return i*i
#         fs.append(g)
#     return fs
#
# for i in count():
#     print i()

# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         fs.append(f(i))
#     return fs
# f1=count()
# for i in f1:
#     print i()

# f=lambda x:x*x
# print f(-2)

# def log(text):
#     if not callable(text):
#         def derocter(func):
#             @functools.wraps(func)
#             def wrapper(*args,**kw):
#                 print '%s call %s():' % (text,func.__name__)
#                 return func(*args, **kw)
#             return wrapper
#         return derocter
#     else:
#         @functools.wraps(text)
#         def wrapper(*args,**kw):
#             print 'call %s():' % (text.__name__)
#             return text(*args, **kw)
#         return wrapper
#
# @log("lala")
# def now():
#     print "2013-5-12"
#
# now()

# print int("35618",base=16)
# int16=functools.partial(int,base=16)
# print int16("1354a")
