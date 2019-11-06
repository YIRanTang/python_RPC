# coding: utf-8

from HelloWorld import HelloWorldService
from HelloWorld.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class HelloServiceHandler:
    def SayBayBay(self):
        ret = "服务端执行SayBayBay"
        print(ret)
        return "BayBay~~~~~~~~~"  # 返回int，与thrift文件中定义的返回i32数据类型一致

    def SayHello(self):
        ret = "服务端执行SayHello"
        print(ret)
        return "Hello~~~~~~~~~~~~~"  # 返回string，与thrift文件中一致


handler = HelloServiceHandler()
processor = HelloWorldService.Processor(handler)  # 定义一个TProcess处理类，创建TProcess对象
transport = TSocket.TServerSocket("localhost", 9090)  # 设置网络读写
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("启动服务")
server.serve()