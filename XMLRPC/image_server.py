from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


def python_logo() -> xmlrpc.client.Binary | None:
    with open("./server/avatar_yu_dan.jpg", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())


if __name__ == '__main__':
    server = SimpleXMLRPCServer(("localhost", 8000))

    print("Listening on port 8000...")

    server.register_function(python_logo, 'python_logo')

    server.serve_forever()
