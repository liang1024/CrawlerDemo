#coding=utf-8
'''
3.死锁

原因:
竞争资源
程序推进顺序不当

必要条件:
互斥条件
请求和保持条件
不剥夺条件
环路等待条件

处理死锁基本方法:
预防死锁(摒弃除1以外的条件)
避免死锁(银行家算法)
检测死锁(资源分配图)
解除死锁
剥夺资源
撤销进程

'''