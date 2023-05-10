import thriftpy2

from thriftpy2.rpc import make_server


class Dispatcher(object):
    """ 根据通信配置文件定义的方法，重写实现方法 """

    @staticmethod
    def ping():
        """
        Ping 一下
        :return:
        """

        return "pong"

    @staticmethod
    def login(username, password):
        """
        登录
        :param username: 用户名
        :param password: 密码
        :return:
        """

        print('获取客户端传过来的参数，用户名: ', username, "，密码: ", password)

        return '登录成功！'


if __name__ == '__main__':
    # 读取通信配置文件
    pingpong_thrift = thriftpy2.load("foo.thrift", module_name="pingpong_thrift")

    # 创建服务，指定本地 ip 地址及监听端口号
    server = make_server(pingpong_thrift.PingPong, Dispatcher(), '127.0.0.1', 6000)

    # 开启服务并监听
    server.serve()
