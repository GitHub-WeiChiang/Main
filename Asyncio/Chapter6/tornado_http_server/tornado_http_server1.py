import tornado.web

if __name__ == '__main__':
    # 创建Web服务器应用
    app = tornado.web.Application()
    # 侦听端口 8888
    app.listen(8888)
    # 启动
    tornado.ioloop.IOLoop.current().start()
