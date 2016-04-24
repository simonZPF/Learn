# -*-coding:utf8-*-
#import os #需要的时候在查
#print os.name
#print os.uname()#window不支持...
#print os.environ #获取系统环境变量
#print os.getenv("PATH").split(";")

# JSON
# import json
# a=dict(name="bob",age=18,sex="f")
# print json.dumps(a)
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print json.loads(json_str)
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob', 20, 88)
# def Student2Dict(std):
#     return {"name":std.name,
#             "age":std.age,
#             "score":std.score}
# #print json.dumps(s,default=Student2Dict)
# print json.dumps(s,default=lambda obj:obj.__dict__)

#多进程
# 少量进程
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print "Run child process %s (%s)..." %(name,os.getpid())
#
# if __name__=='__main__':#必须有这个
#     print 'Parent process %s.' % os.getpid()
#     p=Process(target=run_proc,args=('test',))
#     print "Process will start."
#     p.start()
#     p.join()
#     print 'Process end.'
#   大量进程from multiprocessing import Pool
# import os,time,random
#
# def long_time_task(name):
#     print "Run task %s (%s)..." % (name,os.getpid())
#     start = time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print "Task %s runs %0.2f seconds." % (name, (end-start))
#
# if __name__=="__main__":
#     print "Parent process %s." % os.getpid()
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print "Waiting for all subprocesses done..."
#     start = time.time()
#     p.close()
#     p.join()
#     end = time.time()
#     print "ALL sublprocesses done in %0.2f " % (end-start)
#   进程之间的通信
# from multiprocessing import Process ,Queue
# import os ,time ,random
#
# def write(q):
#     for value in ['A','B','C']:
#         print "Puts %s to queue" % value
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     while True:
#         value = q.get(True)
#         print "Get %s from queue" % value
#
# if __name__=="__main__":
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

#多线程
# import time,threading
#
# def loop():
#     print "thraed %s is running..." % threading.current_thread().name
#     n = 0
#     while n<5:
#         n=n+1
#         print "thread %s >>> %s" % (threading.current_thread().name,n)
#         time.sleep(1)
#     print 'thread %s ended.' % threading.current_thread().name
#
# print 'thread %s is running...' % threading.current_thread().name
# start =time.time()
# t= threading.Thread(target=loop,name="LoopThread")
# t.start()
# print "lala\n"
# time.sleep(1)
# t.join()
# end =time.time()
# print "thread %s ended." % threading.current_thread().name
# print "time %0.2f seconds " % (end-start)

# import time,threading
#
# balance=0
# lock=threading.Lock()
# def change_it(n):
#     global balance
#     balance+=n
#     balance-=n
# def run_thread(n):
#     for i in range(10000):
#         lock.acquire() #线程锁
#         try:
#             change_it(n)
#         finally:
#             lock.release() #解锁
#
# t1= threading.Thread(target=run_thread,args=(5,))
# t2= threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

# ThreadLocal
# import threading
#
# local_school=threading.local()
# def process_student():
#     print "hello, %s(in %s)" % (local_school.student,threading.current_thread().name)
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()