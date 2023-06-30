import xmlrpc.client

if __name__ == '__main__':
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    with open("./client/avatar_yu_dan.jpg", "wb") as handle:
        handle.write(proxy.python_logo().data)
