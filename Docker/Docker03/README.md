Docker03 什么是 Docker Compose ?
=====
* ### Docker 为了解决更好管理多个容器的问题，就推出了 Docker Compose 这个项目，使多个容器可以更方便地定义和运行。
* ### Docker Compose 很好使用，只需要将所有容器的设置放到一个单独的 docker-compose.yml 文件中。
* ### docker-compose.yml
    ```
    version: "3.9"

    services:

    backend:
        build: ./backend
        ports: 
        - "5000:5000"
        volumes:
        - ./backend:/app

    frontend:
        build: ./frontend
        ports:  
        - "3000:3000"
    ```
    * ### version "3.9": 代表我们使用的是 Docker Compose 的 3.9 版本。
    * ### services: 这个区域指定了我们会创建的容器，在这个例子中有两个服务，backend 和 frontend。
    * ### backend: 这是后端程序的名字。
    * ### build: 指定了 Dockerfile 的路径，./backend 代表在 docker-compose.yml 所在目录下的 backend 文件夹中。
    * ### ports: 指定本机端口和容器端口的映射关系。
    * ### volumes: 制定挂载的参数，相当于 -v 之后的内容。
* ### 构建镜像 (image) 與启动容器
    ```
    $ docker-compose build

    $ docker-compose up
    ```
* ### 启动特定的服务
    ```
    $ docker-compose up <service1> <service2>

    $ docker-compose up backend
    ```
* ### 关闭容器
    ```
    docker-compose stop
    ```
* ### 查看当前容器的状态
    ```
    docker-compose ps
    ```
* ### Redis 啟動、關閉與重啟
    ```
    brew services start redis

    brew services stop redis

    brew services restart redis
    ```
* ### Docker-compose 常用命令整理
    ```
    $ docker-compose build # Builds the images, does not start the containers.

    $ docker-compose up # Builds the images if the images do not exist and starts the containers.

    $ docker-compose stop # Stops your containers, but it won't remove them.
    
    $ docker-compose down # Stops your containers, and also removes the stopped containers as well as any networks that were created.
    ```
<br />
