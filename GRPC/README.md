GRPC
=====
* ### gRPC 是一个高性能、通用的开 源RPC 框架，基于 HTTP/2 协议标准而设计，基于 ProtoBuf 序列化协议开发。
* ### 一个 gRPC 服务的大体结构图如下: gRPC 的服务跨语言的但需要遵循相同的协议 (proto)。
* ### 相比于 REST 服务，gPRC 的优势是使用了二进制编码，比 JSON / HTTP 更快，且有清晰的接口规范以及支持流式传输，但实现相比 REST 服务要复杂。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/GRPC/gRPC.png)
* ### 搭建 gRPC 服务步骤
    * ### 安装 Python 需要的库
        ```
        pip install grpcio
        pip install grpcio-tools
        pip install protobuf
        ```
    * ### 定义 gRPC 的接口
        * ### 创建 gRPC 服务的第一步是在 .proto 文件中定义好接口，proto 是一个协议文件，客户端和服务器的通信接口正是通过 proto 文件协定的，可以根据不同语言生成对应语言的代码文件。
        * ### 这个协议文件主要就是定义好服务 (service) 接口，以及请求参数和相应结果的数据结构。
        * ### 具体的 proto 语法 -> [click me](https://www.jianshu.com/p/da7ed5914088)
        * ### 二维数组、字典等 Python 中常用的数据类型 proto 语法表达 -> [click me](https://blog.csdn.net/xiaoxiaojie521/article/details/106938519)
        ```
        syntax = "proto3";
        
        option cc_generic_services = true;
        
        // 定义服务接口
        service GrpcService {
            // 一个服务中可以定义多个接口，也就是多个函数功能
            rpc hello (HelloRequest) returns (HelloResponse) {}
        }
        
        // 请求的参数
        message HelloRequest {
            // 数字1, 2是参数的位置顺序，并不是对参数赋值
            string data = 1;
            // 支持自定义的数据格式，非常灵活
            Skill skill = 2;
        };
        
        // 返回的对象
        message HelloResponse {
            string result = 1;
            // 支持 map 数据格式，类似 dict
            map<string, int32> map_result = 2;
        };
        
        message Skill {
            string name = 1;
        };
        ```
    * ### 使用 protoc 和相应的插件编译生成对应语言的代码
        ```
        python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=. ./hello.proto
        ```
        * ### -I: 指定 proto 所在目录。
        * ### -m: 指定通过 protoc 生成 py 文件。
        * ### --python_out: 指定生成 py 文件的输出路径。
        * ### hello.proto: 输入的 proto 文件。
        * ### 若遇到 symbol not found in flat namespace '_CFRelease' 問題:
            * ### 使用 Python 3.9.16
            * ### pip uninstall grpcio
            * ### conda install grpcio
            * ### conda install grpcio-tools
        * ### 若遇到編碼格式相關問題
            ```
            iconv -f utf-8 -t GB2312 ./hello.proto > ./hello2.proto
            ```
        * ### 如果順利，將會得到 hello_pb2.py 和 hello_pb2_grpc.py 这两个文件。
    * ### 编写 grpc 的服务端代码:
        * ### 需实现 hello 方法来满足 proto 文件中 GrpcService 的接口需求。
        * ### hello 方法的传入参数，是在 proto 文件中定义的 HelloRequest。
        * ### context 是保留字段。
        * ### 返回参数则是在 proto 中定义的 HelloResponse，服务启动的代码是标准的，可以根据需求修改提供服务的 ip 地址以及端口号。
    * ### 编写 gRPC 客户端的代码:
        * ### 定义访问 ip 和端口号。
        * ### 定义 HelloRequest 数据结构，远程调用 hello 即可。
        * ### 客户端和服务端一定要 import 相同 proto 文件编译生成的 hello_pb2_grpc 和 hello_pb2 模块，即使服务端和客户端使用的语言不一样。
    * ### 调用测试。
<br />
