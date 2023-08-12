Chapter01 - 第一章: 模型层
=====
* ### ORM
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Django/Django%203.1/Chapter01/ORM.png)
* ### 模型的隐藏属性 "_state"
    * ### _state 属性指向一个 ModelState 类实例，它持续跟踪着模型实例的生命周期。
    * ### _state 自己又有 2 个属性: adding 和 db。
        * ### adding: 一个标识符，如果当前的模型实例还没有保存到数据库内，则为 True，否则为 False。
    * ### db: 一个字符串指向某个数据库，当前模型实例是从该数据库中读取出来的。
    * ### 对于一个新创建的模型实例: adding = True 并且 db = None。
    * ### 对于从某个数据库中读取出来的模型实例: adding = False 并且 db = '数据库名'。
* ### 模型方法: 如果有一段需要针对每个模型实例都有效的业务代码，应该把它们抽象成为一个函数，放到模型中成为模型方法，而不是在大量视图中重复编写这段代码，或者在视图中抽象成一个函数。
* ### 模型字段 fields: 字段是模型中最重要的内容之一，也是唯一必须的部分，在 Python 中表现为一个类属性，体现了数据表中的一个列。
    * ### 字段命名约束 (不可以 !): 為关键字、两个以上相鄰下划线和下划线结尾。
* ### 常用字段类型 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/Django/Basic/Chapter04)
* ### FileField
    ```
    class FileField(upload_to=None, max_length=100, **options)
    ```
    * ### 上传文件字段 (不能设置为主键)。
    * ### 默认情况下，该字段在 HTML 中表现为一个 ClearableFileInput 标签。
    * ### 在数据库内，实际保存的是一个字符串类型，默认最大长度 100，可以通过 max_length 参数自定义。
    * ### 真实的文件是保存在服务器的文件系统内的。
    * ### 当访问一个模型对象中的文件字段时，Django 会自动提供一个 FieldFile 实例作为文件的代理，通过这个代理，可以进行一些文件操作:
        * ### FieldFile.name: 获取文件名。
        * ### FieldFile.size: 获取文件大小。
        * ### FieldFile.url: 用于访问该文件的 url。
        * ### FieldFile.open(mode='rb'): 以类似 Python 文件操作的方式，打开文件。
        * ### FieldFile.close(): 关闭文件。
        * ### FieldFile.save(name, content, save=True): 保存文件。
        * ### FieldFile.delete(save=True): 删除文件。
* ### ImageField
    ```
    class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    ```
    * ### 用于保存图像文件的字段。
    * ### 该字段继承了 FileField，其用法和特性与 FileField 基本一样，但多了属性 height 和 width。
    * ### 默认情况下，该字段在 HTML 中表现为一个 ClearableFileInput 标签。
    * ### 在数据库内，实际保存的是一个字符串类型，默认最大长度 100，可以通过 max_length 参数自定义。
    * ### 真实的图片是保存在服务器的文件系统内的。
    * ### height_field 参数: 保存有图片高度信息的模型字段名。
    * ### width_field 参数: 保存有图片宽度信息的模型字段名。
    * ### 需安装 pillow 模块: ```pip install pillow```。
* ### 使用 FileField 或者 ImageField 字段步骤
    * ### 在 settings 文件中，配置 MEDIA_ROOT，作为上传文件在服务器中的基本路径。
    * ### 配置 MEDIA_URL 用 URL，指向上传文件的基本路径。
    * ### 添加 FileField 或者 ImageField 字段到模型中，定义 upload_to 参数，文件最终会放在 MEDIA_ROOT 目录的 "upload_to" 子目录中。
    * ### 假设有一个 ImageField字 段，名叫 mug_shot，在 Django 模板的 HTML 文件中，可以使用 ```{{ object.mug_shot.url }}``` 来获取该文件。
    * ### 可以通过 name 和 size 属性，获取文件的名称和大小信息。
    * ### 安全建议: 需注意檔案的内容與格式，避免安全漏洞，务必对所有的上传文件进行安全检查，确保它们不出问题。
* ### FilePathField
    ```
    class FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100, **options)
    ```
    * ### 一种用来保存文件路径信息的字段。
    * ### 在数据表内以字符串的形式存在，默认最大长度 100，可以通过 max_length 参数设置。
    * ### 包含参数
        * ### path: 必须指定的参数，表示一个系统绝对路径，通常是字符串，也可以是个可调用对象，比如函数。
        * ### match: 可选参数，正则表达式，用于过滤文件名，只匹配基本文件名，不匹配路径。
        * ### recursive: 可选参数，只能是 True 或 False，默认为 False，决定是否包含子目录，也就是是否递归。
        * ### allow_files: 可选参数，只能是 True 或 False，默认为 True，决定是否应该将文件名包括在内，和 allow_folders 其中，必须有一个为 True。
        * ### allow_folders: 可选参数，只能是 True 或 False，默认为 False，决定是否应该将目录名包括在内。
* ### UUIDField
    * ### 数据库无法自己生成 uuid，因此需要使用 default 参数。
* ### FileField vs. FilePathField
    * ### 如果只需要选择现有文件，可以使用 FilePathField；如果需要上传文件并保存在服务器上，可以使用 FileField。
    * ### 通常情况下，FileField 更常用，因为它更灵活，并且可以处理上传文件的情况。
* ### 关系类型字段: 多对一 (ForeignKey)
    ```
    class ForeignKey(to, on_delete, **options)
    ```
    * ### 外键需要两个位置参数，一个是关联的模型，另一个是 on_delete。
    * ### 在 Django 2.0 版本后，on_delete 属于必填参数。
    * ### 外键要定义在 "多" 的一方。
    * ### 若关联的模型位于当前模型之后，则需要通过字符串的方式进行引用。
        ```
        class Car(models.Model):
            manufacturer = models.ForeignKey(
                'Manufacturer',
                on_delete=models.CASCADE,
            )

        class Manufacturer(models.Model):
            pass
        ```
    * ### 若关联的对象在另外一个 app 中，可以显式的指出。
        ```
        class Car(models.Model):
            manufacturer = models.ForeignKey(
                'app.Manufacturer',
                on_delete=models.CASCADE,
            )
        ```
    * ### 递归外键: 评论系统
        ```
        models.ForeignKey('self', on_delete=models.CASCADE)
        ```
    * ### Django 会为每一个外键添加 "_id" 后缀。
* ### 外键重要参数: on_delete
    * ### Django 2.0 后不可省略，需显式指定。
    * ### CASCADE: 同 SQL 的 ON DELETE CASCADE 约束，进行级联删除。
    * ### PROTECT: 阻止删除操作並引發 ProtectedError 异常。
    * ### SET_NULL: 将外键字段设为 null (字段需设置 null=True)。
        ```
        user = models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            blank=True,
            null=True,
        )
        ```
    * ### SET_DEFAULT: 将外键字段设为默认值 (字段需设置 default 参数)。
    * ### DO_NOTHING: 什么也不做。
    * ### SET(): 设置为一个传递给 SET() 的值或者一个回调函数的返回值。
        ```
        from django.conf import settings
        from django.contrib.auth import get_user_model
        from django.db import models

        def get_sentinel_user():
            return get_user_model().objects.get_or_create(username='deleted')[0]

        class MyModel(models.Model):
            user = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.SET(get_sentinel_user),
            )
        ```
    * ### RESTRICT: Django3.1 新增，难以理解，与 PROTECT 不同，大多数情况下同样不允许删除，但是在某些特殊情况下可以删除。
        ```
        class Artist(models.Model):
            name = models.CharField(max_length=10)

        class Album(models.Model):
            artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

        class Song(models.Model):
            artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
            album = models.ForeignKey(Album, on_delete=models.RESTRICT)
        ```
        ```
        >>> artist_one = Artist.objects.create(name='artist one')
        >>> artist_two = Artist.objects.create(name='artist two')
        >>> album_one = Album.objects.create(artist=artist_one)
        >>> album_two = Album.objects.create(artist=artist_two)
        >>> song_one = Song.objects.create(artist=artist_one, album=album_one)
        >>> song_two = Song.objects.create(artist=artist_one, album=album_two)
        >>> album_one.delete()
        # Raises RestrictedError.
        >>> artist_two.delete()
        # Raises RestrictedError.
        >>> artist_one.delete()
        (4, {'Song': 2, 'Album': 1, 'Artist': 1})
        ```
* ### 外键重要参数: limit_choices_to
    * ### 限制外键所能关联的对象，只能用于 Django 的 ModelForm 和 admin 后台，对其它场合无限制功能。
    * ### 假设有一个模型 Author 和一个模型 Book，并且想要在 Book 模型中使用外键来引用 Author，但是只希望选择那些已经出版了至少一本书的作者，可以使用 limit_choices_to 选项来实现这一点，确保用户在选择书的作者时只能看到符合条件的作者选项。
    ```
    from django.db import models

    class Author(models.Model):
        name = models.CharField(max_length=100)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, limit_choices_to={'books__gt': 0})
    ```
* ### 外键重要参数: related_name
    * ### 用于关联对象反向引用模型的名称。
    * ### 这个参数我们可以不设置，Django 会默认以模型的小写加上 "_set" 作为反向关联名。
    * ### 如果不想为外键设置一个反向关联名称，可以将这个参数设置为 "+"。
* ### 外键重要参数: related_query_name
    * ### 反向关联查询名，用于从目标模型反向过滤模型对象的名称。
    ```
    from django.db import models

    class Author(models.Model):
        name = models.CharField(max_length=100)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    ```
    ```
    # 获取作者的所有书籍

    author = Author.objects.get(id=1)
    books_by_author = author.books.all()
    ```
    ```
    # 获取作者的书籍数量

    author = Author.objects.get(id=1)
    book_count = author.books.count()
    ```
* ### 外键重要参数: to_field
    * ### 默认情况下，外键都是关联到被关联对象的主键上 (一般为 id)。
    * ### 如果指定这个参数，可以关联到指定的字段上，但是该字段必须具有 unique=True 属性，也就是具有唯一属性。
* ### 外键重要参数: db_constraint
    * ### 默认情况下，这个参数被设为 True，表示遵循数据库约束。
    * ### 如果设为 False，那么将无法保证数据的完整性和合法性。
    * ### 以下面场景可能需要将它设置为 False
        * ### 有历史遗留的不合法数据，没办法的选择。
        * ### 正在分割数据表。
    * ### 当它为 False 且试图访问一个不存在的关系对象时，会抛出 DoesNotExist 异常。
* ### 外键重要参数: swappable
    * ### 允许在 Django 中创建可插拔的模型，最常见的用途是创建自定义的用户模型以实现可定制的用户认证系统。
    * ### 这使得開發者可以根据项目的特定需求对 Django 进行更深入的定制。
    ```
    from django.contrib.auth.models import AbstractUser

    class CustomUser(AbstractUser):
        # 添加自定义字段或方法

        class Meta:
            swappable = 'AUTH_USER_MODEL'
    ```
* ### 关系类型字段: 多对多 (ManyToManyField)
    * ### To Be Continued...
<br />
