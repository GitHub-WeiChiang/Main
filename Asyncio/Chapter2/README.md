Chapter2 Docker 工具
=====
* ### 下載 Python 鏡像
    ```
    # -ti 代表該環境擁有可交互的終端
    docker run -ti python:3.8-alpine
    ```
* ### 显示所有的容器 (包括未运行的)
    ```
    docker ps -a
    ```
* ### 徹底刪除容器
    ```
    docker rm container_id
    ```
* ### 創建一個退出後自動清理的容器
    ```
    docker run -ti --rm python:3.8-alpine
    ```
* ### 如果是服務器程序，需要長時間運行，且不需要交互的終端
    ```
    docker run -d --rm httpd:alpine

    # 端口映射
    # 訪問 http://127.0.0.1/ 結果顯示 "It works!"
    docker run -d --rm -p 80:80 httpd:alpine
    ```
* ### 停止容器
    ```
    docker stop container_id
    ```
* ### aio_http_server.py 示例
    * ### Dockerfile 範例
        ```
        # 指定鏡像基於環境
        FROM python:3.8-alpine
        # 將 aio_http_server.py 複製到鏡像中的 /opt 目錄
        COPY aio_http_server.py /opt/
        # 指定默認的運行命令
        CMD python3 /opt/aio_http_server.py
        ```
    * ### Docker 操作
        ```
        # 構建鏡像
        docker build . -t http_server

        # 運行
        docker run --rm -d -p 8888:8888 http_server

        # 停止容器
        docker stop container_id
        ```
    * ### docker-compose  範例
        ```
        version: "3"

        services:
        web:
            build: .
            ports:
            - "8888:8888"
        ```
    * ### Docker 操作
        ```
        # 自動構建
        docker-compose up -d
        ```
* ### Docker Compose 相關指令
    ```
    # 停止
    docker-compose stop

    # 停止並清除
    docker-compose down

    # 日誌
    docker-compose logs

    # 服務狀態
    docker-compose ps

    # 實時輸出信息 (將服務運行進程切換到終端前台)
    docker-compose up

    # 將處與終端前台的服務切換到後台
    Ctrl + Z
    ```
<br />
