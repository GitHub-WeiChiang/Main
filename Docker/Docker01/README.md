Docker01 Docker 是什么 ?
=====
* ### 虚拟机 (Virtual Machine): 虚拟机是移植环境的一种解决方案。虚拟机本质上也是一个软件，在这个软件中，我们可以运行另一种操作系统。
    * ### 占用资源多
    * ### 运行步骤冗余
    * ### 运行速度慢
* ### Linux 容器 (Container)
    * ### 占有资源少
    * ### 资源利用率高
    * ### 运行速度快
* ### Docker 是什么 ?
    * ### 属于 Linux 容器的一种封装，提供简单易用的容器使用接口。
    * ### 将软件代码和其依赖，全打包在一个文件中，运行单个文件，就会生成虚拟容器。
    * ### 在这个虚拟容器中，不管本地的操作系统是如何的不同，此容器都能照常运行。
    * ### 简而言之，Docker 的接口非常简单，可以帮助用户更好地创建和使用容器，让相同的代码在不同的环境上正常运行。
* ### Docker 的用途
    * ### 提供一次性的环境
    * ### 提供弹性的云服务
    * ### 组建微服务构架
* ### image 文件
    * ### Docker 把应用程序及其依赖，打包在 image 文件里面，只有通过这个文件，才能生成 Docker 容器。
    * ### image 文件可以看作是容器的设计蓝图，Docker 根据 image 文件生成容器的实例。
    * ### 同一个 image 文件，可以生成多个同时运行的容器实例。
    * ### 一个 image 文件往往通过继承另一个 image 文件，加上一些个性化设置而生成。
    * ### 为了节省时间，我们应该尽量使用别人制作好的 image 文件。
    * ### image 文件制作完成后，可以上传到网上的仓库，Docker 的官方仓库 Docker Hub 是最重要也最常用的 image 仓库。
    ```
    # 列出本机所有的 image 文件
    $ docker image ls

    # 删除特定的 image
    $ docker image rm [imageName]
    ```
* ### 官方镜像 Hello World
    ```
    # 将 image 从仓库抓取到本地
    $ docker image pull hello-world

    # 列出本机所有的 image 文件
    $ docker image ls

    # 运行这个 image
    $ docker container run hello-world
    ```
    * ### docker container run 命令具有自动抓取 image 文件的功能，如果发现本地没有指定的 image 文件，就会从云端仓库自动抓取，因此，上述的 docker image pull 命令并不是必需的步骤。
* ### 有些容器不会自动终止，比如一些容器提供的是服务: 像是 Ubuntu 的 image，就可以在命令行体验 Ubuntu 系统。
    ```
    $ docker container run -it ubuntu bash
    ```
* ### 对于那些不会自动终止的容器，我们可以使用 docker container kill 命令终止。
    ```
    # 使用 docker container ls 找到要终止容器的 id
    $ docker container ls 

    # 使用 kill 命令终止容器
    $ docker container kill [containerId]
    ```
* ### 文本文件 .dockerignore 用於排除不要被打包进入 image 文件的路径。
* ### Dockerfile 是一个文本文件，用来配置 image 的具体内容。
    ```
    # 将 image 文件继承与官方的 3.7 版本的 Python。
    FROM python:3.7

    # 将当前目录下的所有文件 (除了 .dockerignore 排除的路径)，
    # 都拷贝进 image 文件的 /app 目录。
    COPY . /app

    # 指定接下来的工作路径为 /app。
    WORKDIR /app

    # 在 /app 目录下，运行 python 文件。
    CMD python3 Hello.py
    ```
* ### 使用 docker image build 命令创建 image 文件
    ```
    $ docker image build -t python-app .
    or
    $ docker image build -t python-app:0.0.1 .

    # -t 参数用来指定 image 文件的名字，后面还可以用冒号指定标签
    # . 表示 Dockerfile 文件使用的路径
    ```
* ### 使用 docker container run 运行 image
    ```
    $ docker container run python3-app
    ```
<br />
