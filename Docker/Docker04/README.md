Docker04 什么是 Docker Registry 和 DockerHub ?
=====
* ### Docker Registry
    * ### Docker Registry 是存储 Docker image 的仓库。
    * ### 运行 Docker pull 與 Docker push 时，实际上就是和 Docker Registry 通信。
    * ### Docker pull 负责从 Docker registry 将存好的 image 下载到本地。
    * ### Docker push 是将自己创建的 image 上传到 Docker registry 中。
    * ### Docker registry 本质上就是存放 image 的仓库。
    * ### 在本地开启 Docker Registry
        ```
        $ docker run -d -p 5000:5000 --name registry registry:2
        ```
    * ### 將镜像 ubuntu 放到本地的 Docker registry 中
        ```
        $ docker pull ubuntu
        $ docker tag ubuntu localhost:5000/my-ubuntu
        $ docker push localhost:5000/my-ubuntu
        ```
    * ### 将本地的镜像删除
        ```
        $ docker image remove ubuntu
        $ docker image remove localhost:5000/my-ubuntu
        ```
    * ### 将镜像从 registry中 下载下来并运行
        ```
        $ docker pull localhost:5000/my-ubuntu
        $ docker run -it localhost:5000/my-ubuntu
        ```
    * ### 停止或停止并删除 registry
        ```
        $ docker container stop 

        $ docker container stop registry && docker container rm -v registry
        ```
* ### Docker Hub
    * ### Docker Hub 是一个由 Docker 公司运行和管理的基于云的储存库。
    * ### 它是一个在线存储库，Docker 镜像可以由其他用户发布和使用。
    * ### 在 Docker Hub 创建一个自己的仓库
        * ### 点击在欢迎界面中点击 Create a Repository
        * ### 将仓库命名为 <your-username>/my-private-repo
        * ### 设定 visibility 为 Private
        * ### 然后点击 Create 创建 repository
    * ### 将本地的镜像扔到 Docker Hub
        * ### 为项目创建 Dockerfile
        * ### 创建镜像
            ```
            docker build -t <your_username>/my-private-repo
            ```
        * ### 测试镜像
            ```
            docker run <your_username>/my-private-repo
            ```
        * ### 登入 Docker Desktop
        * ### 上传镜像到 DockerHub
            ```
            docker push <your_username>/my-private-repo
            ```
        * ### 登入 Docker Hub，你就会看到 Tags 下有 latest 的标签。
    * ### 下载镜像
        * ### 删除本地的镜像。
        * ### 运行 ```docker pull <your_user_name>/my-private-repo```
* ### docker tag: 标记本地镜像，将其归入某一仓库。
* ### docker tag 用于给镜像打标签
    ```
    docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
    ```
    * ### 比如有一个 centos 镜像
    ```
    [root@localhost ~]$ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    centos              latest              1e1148e4cc2c        2 weeks ago         202MB
    ```
    * ### 对 centos 进行开发，开发了第一个版本，就可以对这个版本打标签，打完标签后会生成新的镜像
    ```
    [root@localhost ~]$ docker tag centos centos:v1
    [root@localhost ~]$ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    centos              latest              1e1148e4cc2c        2 weeks ago         202MB
    centos              v1                  1e1148e4cc2c        2 weeks ago         202MB
    ```
    * ### 继续对 centos 进行开发，开发了第二个版本，继续打标签
    ```
    [root@localhost ~]$ docker tag centos centos:v2
    [root@localhost ~]$ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    centos              latest              1e1148e4cc2c        2 weeks ago         202MB
    centos              v1                  1e1148e4cc2c        2 weeks ago         202MB
    centos              v2                  1e1148e4cc2c        2 weeks ago         202MB
    ```
    * ### 以此类推，每开发一个版本打一个标签，如果以后想回滚版本，就可以使用指定标签的镜像来创建容器
    ```
    [root@localhost ~]$ docker run -itd centos:v1
    ```
<br />
