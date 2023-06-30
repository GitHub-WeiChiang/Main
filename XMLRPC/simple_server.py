import datetime
import xmlrpc.client

from xmlrpc.server import SimpleXMLRPCServer


def today() -> xmlrpc.client.DateTime | None:
    now = datetime.datetime.today()
    return xmlrpc.client.DateTime(now)


if __name__ == '__main__':
    server = SimpleXMLRPCServer(("localhost", 8000))

    print("Listening on port 8000...")

    server.register_function(today, "today")
    server.serve_forever()
