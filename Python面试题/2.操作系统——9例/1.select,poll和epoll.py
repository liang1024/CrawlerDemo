#coding=utf-8
'''
1.select,poll和epoll
参考：
http://www.cnblogs.com/Anker/p/3265058.html

select，poll，epoll都是IO多路复用的机制。I/O多路复用就通过一种机制，可以监视多个描述符，
一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程序进行相应的读写操作。
但select，poll，epoll本质上都是同步I/O，
因为他们都需要在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的，

基本上select有3个缺点:
连接数受限(1024)
查找配对速度慢(循环列表进行匹配)
数据由内核拷贝到用户态

poll改善了第一个缺点
epoll改了三个缺点.(链接数无限制，采用callback进行监听，比轮询好)

关于epoll的: 
参考：
http://www.cnblogs.com/my_life/articles/3968782.html

'''