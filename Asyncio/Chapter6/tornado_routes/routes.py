from abc import ABC

import tornado.routing


# HomePage 是一个继承自 tornado.web.RequestHandler 的类
class HomePage(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Home")


class Users(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Users")


class AppPage(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write(f"Request path is: {self.request.path}")


if __name__ == '__main__':
    # 创建Web服务器应用
    app = tornado.web.Application([
        # 将 HomePage 映射到 / 路径上
        ("/", HomePage),
        # 将 Users 映射到 /users 路径上
        ("/user", Users),
        (r"/app.*", AppPage)
    ])
    # 侦听端口 8888
    app.listen(8888)
    # 启动
    tornado.ioloop.IOLoop.current().start()
