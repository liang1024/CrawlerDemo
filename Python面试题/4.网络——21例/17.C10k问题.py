#coding=utf-8
'''
所谓c10k问题，指的是服务器同时支持成千上万个客户端的问题，
也就是concurrent 10 000 connection（这也是c10k这个名字的由来）。
参考: http://www.kegel.com/c10k.html

解决方案：
采用IO多路复用，如select,poll,epoll等
一条线程或进程处理多个客户端发送的请求
使用如nginx等，并发数5w


'''
