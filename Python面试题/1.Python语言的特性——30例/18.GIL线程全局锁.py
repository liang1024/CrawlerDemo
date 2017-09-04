# coding=utf-8
'''
18 GIL线程全局锁
参考：
http://www.oschina.net/translate/pythons-hardest-problem

线程全局锁(Global Interpreter Lock),
即Python为了保证线程安全而采取的独立线程运行的限制,
说白了就是一个核只能在同一时间运行一个线程.
解决办法就是多进程和下面的协程(协程也只是单CPU,但是能减小切换代价提升性能).

'''