# coding=utf-8
'''
19.协程Coroutine
简单点说协程是进程和线程的升级版,进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间,而协程就是用户自己控制切换的时机,不再需要陷入系统的内核态.
Python里最常见的yield就是协程的思想!
'''
import time

# 协程的实现
def A():
    while True:
        print("----A---")
        yield
        # 下面做要做的操作
        # time.sleep(0.5)

def B(c):
    while True:
        print("----B---")
        c.next()
        # 下面做要做的操作
        # time.sleep(0.5)

if __name__=='__main__':
    a = A()
    B(a)