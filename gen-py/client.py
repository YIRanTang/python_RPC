# coding: utf-8

from HelloWorld import HelloWorldService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 8800)  # 创建一个传输层对象（TTransport），设置调用的服务地址为本地，端口为 9090,TSocket传输方式
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)  # 创建通信协议对象（TProtocol），设置传输协议为 TBinaryProtocol
    client = HelloWorldService.Client(protocol)  # 创建一个Thrift客户端对象
    transport.open()

    rec_msg = client.SayBayBay()
    print("SayBayBay方法返回的信息为：", rec_msg)
    rec_msg = client.SayHello()
    print('SayHello方法返回的信息为：', rec_msg)

except Thrift.TException as ex:
    print(ex.message)
finally:
    transport.close()