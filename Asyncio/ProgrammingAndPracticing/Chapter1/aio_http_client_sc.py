import asyncio


async def main():
    # open_connection 函数有两个返回值，reader 和 writer，
    # 其中 reader 用于读取服务器的数据，writer 用于向服务器发送数据
    reader, writer = await asyncio.open_connection("yunp.top", "80")

    # HTTP 协议的第一行，指定请求资源及 HTTP 版本
    writer.write(b'GET / HTTP/1.1\r\n')

    # HTTP 协议头， Host 指定请求的主机，注意在冒号后面必须有一个空格
    writer.write(b"Host: yunp.top\r\n")

    # HTTP 协议头， Connection 指定连接服务器的方式
    writer.write(b"Connection: close\r\n")

    # 发送协议头结尾标识
    writer.write(b'\r\n')

    # write 函数会尝试立即向 socket 连接发送数据，
    # 但是也有可能失败，最常见的原因是当前 IO 资源被占用，失
    # 败时数据以队列形式暂存于缓冲区直到可以被再次发送，
    # 为确保数据已经完全发送成功之后再做后续操作，
    # 通常使用 drain 函数来等待数据发送完毕，
    # 如果在调用该函数前数据已经发送完毕，则该函数立即返回结果
    await writer.drain()

    result = await reader.read()

    print(result.decode("utf-8"))


if __name__ == '__main__':
    asyncio.run(main())
