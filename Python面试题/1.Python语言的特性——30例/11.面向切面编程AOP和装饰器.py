# coding=utf-8
'''
11.面向切面编程AOP和装饰器

面向切面编程AOP：
在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。

装饰器的作用就是为已经存在的对象添加额外的功能。

这个AOP一听起来有点懵,有同学面阿里的时候就被问懵了...

装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、
性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，
有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

这个问题比较大,推荐: http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python
中文: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/3/README.html
'''
