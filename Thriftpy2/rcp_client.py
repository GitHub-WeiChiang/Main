import thriftpy2

from thriftpy2.rpc import make_client

if __name__ == '__main__':
    # 读取通信配置文件
    pingpong_thrift = thriftpy2.load("foo.thrift", module_name="pingpong_thrift")

    # 创建客户端
    client = make_client(pingpong_thrift.PingPong, '127.0.0.1', 6000)

    # 调用通信文件中定义好的方法（实际调用服务端的方法）
    print(client.ping())
    print(client.login('root', 'pwd'))
