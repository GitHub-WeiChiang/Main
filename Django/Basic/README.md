Basic
=====
* ### Initial Configuration Sample Code
* ### VS Code Extensions
* ### Django 的 CBV 与 FBV
* ### Python 中多继承与 Mixin Coding Style (代碼風格)
* ### Chapter01 網站開發環境建置
* ### Chapter02 Django 網站快速入門
* ### Chapter03 讓網站上線
* ### Chapter04 深入瞭解 Django 的 MVC 架構
* ### Chapter05 網址的對應與委派
* ### Chapter06 Template 深入探討
<br />

Initial Configuration Sample Code
=====
```
conda env list

conda env remove --name VENV_NAME
```
```
# "VENV_NAME" here is "django"

conda create --name VENV_NAME python=3.10

conda activate VENV_NAME

pip install django

django-admin startproject PROJECT_NAME

cd PROJECT_NAME

python manage.py startapp APP_NAME
```
```
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    ...,
    'APP_NAME',
]

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'
```
```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```
```
# If necessary, you can add the following code to admin.py.

from APP_NAME.models import MODELS_NAME

admin.site.register(MODELS_NAME)
```
```
pip list --format=freeze > requirements.txt
```
```
mkdir static
mkdir templates
```
```
TEMPLATES = [
    {
        ...,
        'DIRS': [BASE_DIR / 'templates'],
        ...,
    },
]

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```
```
python manage.py runserver
```
```
conda deactivate
```
<br />

VS Code Extensions
=====
* ### Code Runner
* ### Django
* ### Django Template
* ### HTML CSS Support
* ### Python
<br />

Django 的 CBV 与 FBV
=====
* ### FBV (Function Base Views): 在视图里使用函数处理请求。
* ### CBV (Class Base Views): 在视图里使用类处理请求。
* ### Python 是一个面向对象的编程语言，如果只用函数来开发，很多面向对象的优点就错失了 (继承、封装、多态)。
* ### Django 在后来加入了 CBV，可以让我们用类写 View，这样做的优点如下:
    * ### 提高了代码的复用性，可以使用面向对象的技术，比如 Mixin (多继承)。
    * ### 可以用不同的函数针对不同的 HTTP 方法处理，而不是通过很多 if 判断，提高代码可读性。
* ### 处理 GET 方法的 view: FBV
    ```
    from django.http import HttpResponse

    def my_view(request):
        if request.method == 'GET':
                return HttpResponse('OK')
    ```
* ### 处理 GET 方法的 view: CBV
    ```
    from django.http import HttpResponse
    from django.views import View

    class MyView(View):
        def get(self, request):
                return HttpResponse('OK')
    ```
* ### Django 的 url 是将一个请求分配给可调用的函数的，而不是一个 class。
* ### 针对上述问题，CBV 提供了一个 ```as_view()``` 静态方法 (也就是类方法)，调用这个方法，会创建一个类的实例，然后通过实例调用 dispatch() 方法。
    ```
    from django.conf.urls import url
    from myapp.views import MyView

    urlpatterns = [
        url(r'^index/$', MyView.as_view()),
    ]
    ```
* ### dispatch() 方法会根据 request 的 method 的不同调用相应的方法来处理 request (get()、post()、...)。
* ### 之後就和 FBV 差不多了，要接收 request，得到一个 response 返回，如果方法没有定义，会抛出 HttpResponseNotAllowed 异常。
* ### 类的属性可以通过两种方法设置，第一种是常见的 Python 的方法，可以被子类覆盖。
    ```
    from django.http import HttpResponse
    from django.views import View

    class GreetingView(View):
        name = "yuan"
        def get(self, request):
            return HttpResponse(self.name)

    # You can override that in a subclass

    class MorningGreetingView(GreetingView):
        name= "alex"
    ```
* ### 第二种方法則是在 url 中指定类的属性
    ```
    urlpatterns = [
        url(r'^index/$', GreetingView.as_view(name="egon")),
    ]
    ```
<br />

Python 中多继承与 Mixin Coding Style (代碼風格)
=====
* ### Python 支持一种简单类型的多重继承，它允许创建 Mixins。
* ### Mixins 是一种类，用于将额外的属性和方法 "混合 (mix in)" 到一个类中，也就是允许以组合风格创建类。
* ### Mixins 是一个非常棒的概念，但错误地使用它们会导致一些错误。
```
class Mixin1(object):
    def test(self):
        print "Mixin1"

class Mixin2(object):
    def test(self):
        print "Mixin2"

class MyClass(BaseClass, Mixin1, Mixin2):
    pass
```
* ### 在 Python 中，类层次结构是从右到左定义的，因此在这种情况下 Mixin2 类是基类，由 Mixin1 扩展，最后由 BaseClass 扩展。
* ### 示例代碼在 mixin 中重写了方法或属性，这可能会导致意想不到的结果，因为方法的解析优先级是从左到右。
```
>>> obj = MyClass()
>>> obj.test()
Mixin1
```
* ### 使用 mixin 的正确方法是相反的顺序
```
class MyClass(Mixin2, Mixin1, BaseClass):
    pass
```
```
>>> obj = MyClass()
>>> obj.test()
Mixin2
```
* ### 这种类型起初看起来有悖常理 (Counter Intuitive)，因为大多数人会从左到右读取自上而下的类层次结构，但是如果以程序运行的思维考虑这个正在定义的类，则可以正确读取类层次结构 (MyClass => Mixin2 => Mixin1 => BaseClass)。
* ### 如果以这种方式定义类，将不会有很多冲突，也不会遇到太多错误。
* ### 认识 Mixin Coding Style (代碼風格)
    * ### 类的单继承，是再熟悉不过的，写起来也毫不费力。
    * ### 而多继承呢，见得很多，写得很少，在很多的项目代码里，还会见到一种很奇怪的类，它們有一个命名上的共同点，就是在类名的结尾，都喜欢用 Mixin。
    * ### 继承是一个 "is-a" 关系。比如轿车类继承交通工具类，因为轿车是一个 "is-a" 交通工具。
    * ### 一个物品不可能是多种不同的东西，因此就不应该存在多重继承，不过有没有这种情况，一个类的确是需要继承多个类呢 ?
    * ### 答案是有，还是拿交通工具来举例子，民航飞机是一种交通工具，对于土豪们来说直升机也是一种交通工具。
    * ### 对于这两种交通工具，它们都有一个功能是飞行，但是轿车没有。
    * ### 所以，不可能将飞行功能写在交通工具这个父类中，但是如果民航飞机和直升机都各自写自己的飞行方法，又违背了代码尽可能重用的原则 (如果以后飞行工具越来越多，那会出现许多重复代码)。
    * ### 怎么办，那就只好让这两种飞机同时继承交通工具以及飞行器两个父类，这样就出现了多重继承，这时又违背了继承必须是 "is-a" 关系。
    * ### 这时候 Mixin 就闪亮登场了，飞行只是飞机做为交通工具的一种 (增强) 属性，可以为这个飞行的功能单独定义一个 (增强) 类，称之为 Mixin 类。
    * ### 这个类，是做为增强功能，添加到子类中的，为了让其餘开发者，一看就知道这是个 Mixin 类，一般都要求开发者遵循规范，在类名末尾加上 Mixin。
    ```
    class Vehicle(object):
        pass

    class PlaneMixin(object):
        def fly(self):
            print('I am flying')

    class Airplane(Vehicle, PlaneMixin):
        pass
    ```
    * ### 使用 Mixin 类实现多重继承要遵循以下几个规范
        * ### 责任明确: 必须表示某一种功能，而不是某个物品。
        * ### 功能单一: 若有多个功能，那就写多个 Mixin 类；
        * ### 绝对独立: 不能依赖于子类的实现，子类即便没有继承这个 Mixin 类，也照样可以工作，就是缺少了某个功能。
* ### 不使用 Mixin 的弊端
    * ### 结构复杂: 单继承中一个类的父类是什么，父类的父类是什么非常明确，多继承一个类有多个父类，父类又有多个父类，继承关系复杂。
    * ### 优先顺序模糊: 多个父类中有同名方法，在开发过程中，容易造成思维混乱，子类不知道继承哪个父类，会增加开发难度。
    * ### 功能冲突: 多重继承有多个父类，但是子类只能继承一个，对于同名方法，就会导致另一个父类的方法失效。
<br />

Reference
=====
* ### 快速學會 Python 架站技術：活用 Django 4 建構動態網站的 16 堂課
<br />
