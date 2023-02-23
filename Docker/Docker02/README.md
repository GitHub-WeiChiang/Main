Docker02 Docker 常用命令
=====
* ### 容器参数
    * ### Dockerfile 中的 ENTRYPOINT: 和 CMD 一样，都是在指定容器启动时的程序和参数。
    ```
    ENTRYPOINT ["python3", "pyramid.py"]
    ```
    * ### Dockerfile 中的 CMD: 指定的是容器的默认命令，其命令可以被覆盖。
    ```
    CMD ["5"]
    ```
    * ### 如果没有输入额外命令的话，容器最后会默认运行 "python3 pyramid.py 5"。
    ```
    # 命令创建 image 文件
    $ docker build . --tag pyramid

    # 运行 image
    $ docker run pyramid

    # 运行 image 並指定容器参数
    $ docker run pyramid 10
    ```
* ### 容器端口映射 Container Ports
    * ### 一个容器需要暴露端口才能运行，那么需要将本地端口映射到容器的端口后，才能从本地访问到程序，以下的命令则会把 my-app 容器中的端口 3000 映射到本地端口 5000。
    ```
    $ docker run -p 5000:3000 my-app
    ```
    * ### Dockerfile 中的 RUN: 安装此程序需要的依赖。
    ```
    RUN ["pip3", "install", "-r", "requirements.txt"]
    ```
    * ### Dockerfile 中的 EXPOSE: 表示将指定端口打开。
    ```
    EXPOSE 5001
    ```
    * ### 運行
    ```
    # 命令创建 image 文件
    $ docker build . --tag web-app-backend

    # 运行 image，指定容器中的 5001 端口对应到本地的 5001 端口
    $ docker run -p 5001:5001 web-app-backend


    # 命令创建 image 文件
    $ docker build . --tag web-app-frontend

    # 运行 image，指定容器中的 3001 端口对应到本地的 3001 端口
    $ docker run -p 3001:3001 web-app-frontend
    ```
* ### Docker 数据管理 (Manage Data in Docker)
    * ### Docker container 并不能永远储存数据，一旦容器被停止，那么其中的文件也无法被访问了。
    * ### Docker 提供了两种解决方案，一种是 Bind mount，另一种是 volume。
* ### 挂载 Bind Mount
    * ### 使用 Bind Mount 可以将本地的一个文件夹与 Docker 容器中的另一个文件夹同步，就是说对本地指定的文件夹上做的任何操作都会同步到容器中的文件夹反之亦然。
    * ### 创建镜像并运行容器
    ```
    docker build . -t volume

    docker run -p 3001:3001 -v /Users/albert/GitLab/main/Docker/Docker02/volume/volume_data:/app/volume_data volume
    ```
    * ### 如果要让本地文件夹与容器中的文件夹同步，则需要在运行时使用 -v <local_folder_path>:<container_folder_path> 参数，定义好同步文件夹的绝对路径和容器文件夹的路径。
* ### 数据卷 Docker Volume
    * ### 和 Bind Mount 不同的是，Docker Volume 不需要在本地提前建好文件夹，只需要指定 volume 的名字，Docker 则会自动创造出一个文件夹，用来储存 volume 对应的数据。
    * ### 使用 volume create 创建 volume，使用 inspect 查看 volume 的具体信息。
    ```
    $ docker volume create book-data

    $ docker volume inspect book-data
    [
        {
            "CreatedAt": "2020-12-18T20:33:53Z",
            "Driver": "local",
            "Labels": {},
            "Mountpoint": "/var/lib/docker/volumes/book-data/_data",
            "Name": "book-data",
            "Options": {},
            "Scope": "local"
        }
    ]
    ```
    * ### 让 Docker 容器和 volume 同步，只需要使用 -v <volume_name>:<container_folder_path> 定义好 volume 名字和容器文件夹的位置。
    ```
    docker run -p 3000:3000 -v book-data:/app/volume_data volume
    ```
    * ### 要改变 volume 中的文件内容，则需要开启 ubuntu 容器并与之相同的 volume 同步後修改之。
    ```
    $ docker run -v book-data:/book-data -it ubuntu

    root:/# ls

    root:/# cd book-data

    root:/book-data# ls

    root:/book-data# cat book.json

    root:/book-data# echo {\"title\": \"hi\"}
    ```
* ### Docker 命令总结
    ```
    # Images
    $ docker build --tag my-app:1.0 .
    $ docker images # listing images
    $ docker save -o <path_for_generated_tar_file> <image_name> # Save the image as a tar file
    $ docker load -i <path_to_tar_file> # Load the image into Docker
    $ docker rmi my-app:1.0 # Remove a docker image
    $ docker rmi --force my-app:1.0 
    $ docker rmi $(docker images -a -q) # Remove all images that are not associated with existing containers
    $ docker rmi $(docker images -a -q) -f # same as above, but forces the images associated with running containers to be also be removed

    # Containers
    $ docker run my-app:1.0
    $ docker ps # view a list of running containers
    $ docker ps -a # includes stopped containers
    $ docker run -p 8000:3000 my-app:1.0 # Exposes port 3000 in a running container, and maps to port 8000 on the host machine
    $ docker rm $(docker ps -a -q)  # removes all containers
    $ docker rm $(docker ps -a -q) -f  # same as above, but forces running containers to also be removed

    # Volumes
    $ docker run -d --name my-app -v volume-name:/usr/src/app my-app:1.0
    $ docker run -p 3000:3000 -v <load_absolute_path>:<docker_absolute_path> volume-app-frontend
    $ docker volume ls 
    $ docker volume prune # Removes unused volumes
    ```
<br />
