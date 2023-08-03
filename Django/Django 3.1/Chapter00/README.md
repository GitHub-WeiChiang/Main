Chapter00 - 第一个 Django 应用
=====
* ### 新建项目
    ```
    conda env list

    conda create --name VENV_NAME python=3.10

    source activate VENV_NAME

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
* ### 为什么不把模板文件直接放在 polls/templates 目录下，而是费劲的再建个子目录 polls 呢?
    * ### 设想这么个情况，有另外一个 app，它也有一个名叫 index.html 的文件，当 Django 在搜索模板时，有可能就找到它，然后退出搜索，这就命中了错误的目标。
    * ### 解决这个问题的最好办法就是在 templates 目录下再建立一个与 app 同名的子目录，将自己所属的模板都放到里面，从而达到独立命名空间的作用，不会再出现引用错误。
    1. ### 應用中可能有很多个 app，其中甚至有不少 app 並非從零撰寫只是導入使用。
    2. ### app 的排序是不可預期的，Django 只会按照既定的规则顺序查找每个 app。3. ### Django 查找模版时，会去每个 app 的 templates 目录下查找，这是核心机制 ! 就是每个 ! 而不是只查找該 app 的 html 文件目录。
    4. ### 如果有多个 app 同时有 index.html 模板，那么 Django 找到的第一个 index 就会被调用，比如 app_a 排在 app_b 前面，那么 app_a 没问题了，但 app_b 会使用 app_a 中的 index.html 文件。
    5. ### 为了解决这个问题，在每个 app 的 templates 目录下再创建一级目录，就相当于增加了模版命名空间限制。
* ### render() 函数
    * ### 第一个位置参数是请求对象 (就是 view 函数的第一个参数)。
    * ### 第二个位置参数是模板文件。
    * ### 第三参数是可选的，一个字典，包含需要传递给模板的数据。
    * ### 最后 render() 函数返回一个经过字典数据渲染过的模板封装而成的 HttpResponse 对象。
* ### 返回 404 错误
    * ### get_object_or_404(): 替代 models.objects.get()。
    * ### get_list_or_404(): 替代 models.objects.filter()。
* ### HttpResponseRedirect: 重定向的 URL。
    * ### reverse() 函数: 避免在视图函数中硬编码 URL，首先需要一个在 URLconf 中指定的 name，然后是传递的数据。
* ### vote{{ choice.votes|pluralize }}: Django 模板语言中用来智能选择正确单词形式的过滤器，它根据对象的 votes 属性的值来决定是使用单数还是复数形式。
* ### DetailView 需要从 url 捕获到的称为 "pk" 的主键值。
* ### context_object_name 属性: 用於客製化指定上下文变量。
* ### FBV vs. CBV
    * ### 类视图相比函数视图具有类的特性，可封装可继承，利于代码重用。
    * ### 通用视图是类视图的一种。
    * ### 通用视图的代码虽然少了，但学习成本高了。
    * ### 在享受便利的同时，要记住更多通用视图的用法和规则，有得有失。
    * ### 其实可以自己编写新的通用视图，定義客製化规则與规矩，不必使用 Django 提供的，但这相当于造轮子。
    * ### 不要沉迷于类视图的强大。
* ### 编写测试程序
    ```
    python manage.py shell

    import datetime

    from django.utils import timezone

    from polls.models import Question

    future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))

    future_question.was_published_recently()

    exit()
    ```
* ### 创建一个测试来暴露这个 bug
    * ### 测试代码放在应用的 tests.py 文件中，测试系统将自动地从任何名字以 test 开头的文件中查找测试程序。
    * ### 每个 app 在创建的时候，都会自动创建一个 tests.py 文件。
* ### 运行测试程序
    ```
    python manage.py test polls
    ```
    * ### python manage.py test polls 命令会查找投票应用中所有的测试程序。
    * ### 发现一个 django.test.TestCase 的子类。
    * ### 为测试创建一个专用的数据库。
    * ### 查找名字以 test 开头的测试方法。
    * ### 在 test_was_published_recently_with_future_question 方法中，创建一个 Question 实例，该实例的 pub_data 字段的值是 30 天后的未来日期。
    * ### 然后利用 assertIs() 方法，它发现 was_published_recently() 返回了 True，而不是我们希望的 False。
* ### 使用静态文件
    * ### Django 的 STATICFILES_FINDERS 设置项中包含一个查找器列表，它们知道如何从各种源中找到静态文件。
    * ### 其中一个默认的查找器是 AppDirectoriesFinder，它在每个 INSTALLED_APPS 下查找 static 子目录。
    * ### {% static %} 模板标签会生成静态文件的绝对 URL 路径。
<br />
