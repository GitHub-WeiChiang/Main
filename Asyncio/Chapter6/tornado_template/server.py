from abc import ABC

import tornado.web


class IndexHandler(tornado.web.RequestHandler, ABC):
    async def get(self):
        await self.render("index.html")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", IndexHandler),
    ])

    application.listen(8888)

    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt as e:
        print("User stopped the server")
