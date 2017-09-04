# coding=utf-8
'''

参考：
百度百科
https://baike.baidu.com/item/MVCC/6298019?fr=aladdin
MVCC浅析
http://blog.csdn.net/chosen0ne/article/details/18093187
MVCC的原理与copyonwrite类似，全称是Multi-Version Concurrent Control，
即多版本并发控制。在MVCC协议下，每个读操作会看到一个一致性的snapshot，
并且可以实现非阻塞的读。


'''