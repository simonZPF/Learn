#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ import division
' a test module '

__author__ = 'Simon Z'
# import sys
# def foo():
#     args=sys.argv
#     if len(args)==1:
#         print "hello world"
#     elif len(args)==2:
#         print "hello "+args[1]
#
# if __name__=="__main__":
#     foo()

# print "10/3 = ",10/3
# print "10//3 = ",10//3
# print "10.0/3 = ",10.0/3

#  __slots__限制添加属性
# class student(object):
#     __slots__=("name","age")#限制可添加的属性 对子类无影响
#     pass
# class highSchoolStudent(student):
#     pass
# s=student()
# s3=highSchoolStudent()
#s2=student()
# def set_age(self,age):
#     self.age=age

#  给类动态添加方法
# from types import MethodType
# #s.set_age=MethodType(set_age,s,student)# 只对s有用
# student.set_age=MethodType(set_age,None,student)# 对所以有用
# s2.set_age(25)
# s3.score=100
# print s3.score

# @property 使用
# class Student(object):
#
#     @property #= score.getter
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s=Student()
# s.score=160
# print s.score

# 定制类
#   定制print class
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return "This student named '%s'" % self.name # print s 与 s 有区别
#     __repr__ = __str__ #__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
#
# s=Student("hello")
# print s
#   定制迭代对象
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>100:
#             raise StopIteration
#         return self.a
# for i in Fib():
#     print i
# 定制getitem对象
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n,int):
#             a,b=0,1
#             for i in range(n):
#                 a,b=b,a+b
#             return a
#         elif isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             a,b=0,1
#             l=[]
#             for i in range(stop):
#                 if i>=start:
#                     l.append(a)
#                 a,b=b,a+b
#             return l
#
# print Fib()[:7]
# __getattr__
# class Student(object):
#
#     def __getattr__(self, attr):
#         if attr=='age':
#             #return lambda: 25 # can return function
#             return 26
#         return "no"
#         #raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
#
# s=Student()
# print s.aa
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
# s=Chain()
# print Chain().users.pp.sss

# __call__对实例进行调用
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
# s=Student("aaa")
# print s()

