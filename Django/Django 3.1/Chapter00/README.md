Chapter00 - 第一个 Django 应用
=====
* ### 新建项目
    ```
    conda env list

    conda create --name VENV_NAME python=3.10

    source activate django

    pip install django

    django-admin startproject PROJECT_NAME

    cd PROJECT_NAME
    ```
* ### 各文件和目录解释
    * ### 外层的 mysite/: 与 Django 无关，只是项目的容器，可以任意重命名。
    * ### manage.py: 一个命令行工具，管理 Django 的交互脚本。
    * ### 内层的 mysite/: 真正的项目文件包裹目录，其名為引用内部文件的 Python 包名 (例: mysite.urls)。
    * ### mysite/__init__.py: 一个定义包的空文件。
    * ### mysite/settings.py: 项目的配置文件。
    * ### mysite/urls.py: 路由文件，所有的任务皆从此處开始分配，相当于 Django 驱动站点的目录。
    * ### mysite/wsgi.py: 一个基于 WSGI 的 web 服务器进入点，提供底层的网络通信功能。
    * ### mysite/asgi.py: 一个基于 ASGI 的 web 服务器进入点，提供异步的网络通信功能。
* ### 启动开发服务器
    ```
    python manage.py runserver
    ```
* ### 创建投票应用
    * ### app 应用与 project 项目的区别
        * ### app 用於实现某个具体功能。
        * ### project 是配置文件和多个 app 的集合。
        * ### project 可以包含多个 app。
        * ### app 可以属于多个 project。
    ```
    python manage.py startapp polls
    ```
* ### include 语法相当于多级路由，它把接收到的 url 地址去除与此项匹配的部分，将剩下的字符串传递给下一级路由 urlconf 进行判断。
* ### path() 方法: 接收 4 个参数，前 2 个是必须的 (route & view)，後 2 个是可选的 (kwargs & name)。
    * ### route: 匹配 URL 的准则，执行的是短路机制，且不会匹配 GET 和 POST 等参数或域名。
    * ### view: 处理当前 url 请求的视图函数，当 Django 匹配到某个路由条目时，自动将封装的 HttpRequest 对象作为第一个参数，被 "捕获" 的参数以关键字参数的形式，传递给该条目指定的视图。
    * ### kwargs: 任意数量的关键字参数可以作为一个字典传递给目标视图。
    * ### name: 对 URL 进行命名，能够在 Django 的任意处 (尤其是模板内) 显式地引用 (相当于给URL取了个全局变量名)。
<br />
