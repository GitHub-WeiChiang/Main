import time
import grpc
import hello_pb2_grpc
import hello_pb2

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TestService(hello_pb2_grpc.GrpcServiceServicer):
    """
    继承 GrpcServiceServicer 实现 hello 方法
    """

    def __init__(self):
        pass

    def hello(self, request, context):
        """
        具体实现 hello 的方法，并按照 pb 的返回对象构造 HelloResponse 返回
        :param request:
        :param context:
        :return:
        """

        result = request.data + request.skill.name + " this is gprc test service"
        list_result = {"12": 1232}
        return hello_pb2.HelloResponse(result=str(result), map_result=list_result)


def run():
    """
    模拟服务启动
    :return:
    """

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    hello_pb2_grpc.add_GrpcServiceServicer_to_server(TestService(),server)
    
    server.add_insecure_port('[::]:50052')
    
    server.start()
    
    print("start service...")
    
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()
