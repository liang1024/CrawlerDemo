#coding=utf-8
'''
RPC（Remote Procedure Call Protocol）——远程过程调用协议，
它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。
RPC协议假定某些传输协议的存在，如TCP或UDP，
为通信程序之间携带信息数据。在OSI网络通信模型中，
RPC跨越了传输层和应用层。RPC使得开发包括网络分布式多程序在内的应用程序更加容易。
总结:服务提供的两大流派.传统意义以方法调用为导向通称RPC。
为了企业SOA,若干厂商联合推出webservice,制定了wsdl接口定义,传输soap.
当互联网时代,臃肿SOA被简化为http+xml/json.但是简化出现各种混乱。
以资源为导向,任何操作无非是对资源的增删改查，于是统一的REST出现了.

进化的顺序: RPC -> SOAP -> RESTful
'''