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
    python manage.py startapp APP_NAME
    ```
* ### include 语法相当于多级路由，它把接收到的 url 地址去除与此项匹配的部分，将剩下的字符串传递给下一级路由 urlconf 进行判断。
* ### path() 方法: 接收 4 个参数，前 2 个是必须的 (route & view)，後 2 个是可选的 (kwargs & name)。
    * ### route: 匹配 URL 的准则，执行的是短路机制，且不会匹配 GET 和 POST 等参数或域名。
    * ### view: 处理当前 url 请求的视图函数，当 Django 匹配到某个路由条目时，自动将封装的 HttpRequest 对象作为第一个参数，被 "捕获" 的参数以关键字参数的形式，传递给该条目指定的视图。
    * ### kwargs: 任意数量的关键字参数可以作为一个字典传递给目标视图。
    * ### name: 对 URL 进行命名，能够在 Django 的任意处 (尤其是模板内) 显式地引用 (相当于给URL取了个全局变量名)。
* ### 数据库配置
    ```
    LANGUAGE_CODE = 'zh-hant'

    TIME_ZONE = 'Asia/Taipei'

    INSTALLED_APPS = [
        ...,
        'APP_NAME',
    ]

    python manage.py makemigrations

    python manage.py migrate
    ```
* ### Django 自动生成的 INSTALLED_APPS
    * ### django.contrib.admin: admin 管理后台站点。
    * ### django.contrib.auth: 身份认证系统。
    * ### django.contrib.contenttypes: 内容类型框架。
    * ### django.contrib.sessions: 会话框架。
    * ### django.contrib.messages: 消息框架。
    * ### django.contrib.staticfiles: 静态文件管理框架。
* ### 启用模型
    ```
    python manage.py makemigrations APP_NAME

    python manage.py sqlmigrate APP_NAME XXXX

    python manage.py migrate
    ```
    * ### makemigrations: Django 会检测对模型文件的修改，也就是告诉 Django 对模型有改动，并且想把这些改动保存为一个 "迁移 (migration)"。
    * ### migrations 是 Django 保存模型修改记录的文件，这些文件保存在磁盘上。
    * ### sqlmigrate 命令可以展示 SQL 语句。
    * ### migrate 命令将对数据库执行真正的迁移动作。
    * ### migrate 命令对所有还未实施的迁移记录进行操作，本质上就是将你对模型的修改体现到数据库中具体的表中。
    * ### Django 通过一张叫做 django_migrations 的表，记录并跟踪已经实施的 migrate 动作，通过对比获得哪些迁移尚未提交。
* ### 改模型时的操作
    * ### 在 models.py 中修改模型。
    * ### 运行 python manage.py makemigrations 为改动创建迁移记录文件。
    * ### 运行 python manage.py migrate 将操作同步到数据库。
* ### 模型自带的 API
    ```
    python manage.py shell

    from polls.models import Question, Choice

    Question.objects.all()

    from django.utils import timezone

    q = Question(question_text="What's new?", pub_date=timezone.now())

    q.save()

    q.id

    q.question_text

    q.pub_date

    q.question_text = "What's up?"

    q.save()

    Question.objects.all()

    exit()
    ```
    ```
    from polls.models import Question, Choice

    Question.objects.all()

    Question.objects.filter(id=1)

    Question.objects.filter(question_text__startswith='What')

    from django.utils import timezone

    current_year = timezone.now().year

    Question.objects.get(pub_date__year=current_year)

    Question.objects.get(id=2)

    Question.objects.get(pk=1)

    q = Question.objects.get(pk=1)

    q.was_published_recently()

    # 显示所有与 q 对象有关系的 choice 集合。
    q.choice_set.all()

    # 创建 3 个 choices。
    q.choice_set.create(choice_text='Not much', votes=0)

    q.choice_set.create(choice_text='The sky', votes=0)

    c = q.choice_set.create(choice_text='Just hacking again', votes=0)

    # Choice 对象可通过 API 访问和其关联的 Question 对象。
    c.question

    q.choice_set.all()

    q.choice_set.count()

    # API 会自动进行连表操作，通过双下划线分割关系对象。
    # 连表操作可以无限多级，一层一层的连接。
    # 查询所有的 Choices，它所对应的 Question 的发布日期是今年。
    Choice.objects.filter(question__pub_date__year=current_year)

    c = q.choice_set.filter(choice_text__startswith='Just hacking')

    c.delete()

    exit()
    ```
* ### 创建管理员用户 (root / root)
    ```
    python manage.py createsuperuser
    ```
* ### 注册投票应用 (polls/admin.py)
    ```
    polls/admin.py

    from django.contrib import admin
    from .models import Question

    admin.site.register(Question)
    ```
<br />
