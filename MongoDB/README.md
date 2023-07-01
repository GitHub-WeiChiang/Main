MongoDB
=====
* ### Docker MongoDB
    ```
    # 查看可用版本
    $ docker search mongo

    # 取最新版的 MongoDB 镜像
    $ docker pull mongo:latest

    # 查看本地镜像
    $ docker images

    # 运行容器
    $ docker run -itd --name mongo -p 27017:27017 mongo --auth

    # 查看容器运行信息
    $ docker ps

    # 添加用户和设置密码
    # 在運行 mongo 的 Docker 容器中執行 "mongo admin" 指令，作用是連接到 MongoDB 的 admin 資料庫。
    $ docker exec -it mongo mongo admin
    # 在連接到 admin 資料庫後，使用 MongoDB 的 Shell 建立一個新的使用者，
    # 使用者名稱與密碼為 "admin"，並賦予兩個角色:
    # userAdminAnyDatabase: 表示具有管理任何資料庫的使用者權限。
    # readWriteAnyDatabase: 表示具有對任何資料庫進行讀寫的權限。
    > db.createUser({user: 'admin', pwd: 'admin', roles: [{role: 'userAdminAnyDatabase', db: 'admin'}, "readWriteAnyDatabase"]});

    # 连接
    > db.auth('admin', 'admin')
    ```
    * ### ```-p 27017:27017```: 映射容器服务的 27017 端口到宿主机的 27017 端口。
    * ### ```--auth```: 需要密码才能访问容器服务。
* ### Compass
    ```
    brew install --cask mongodb-compass
    ```
* ### Python
    ```
    pip install pymongo
    ```
<br />
