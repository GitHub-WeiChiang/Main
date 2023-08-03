import uuid

from django.db import models
from django.db import models

class MyUUIDModel(models.Model):
    # editable=False: 字段不能在後台管理界面中被編輯。
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

def user_directory_path(instance, filename):
    # 文件上传到 "MEDIA_ROOT/user_<id>/<filename>" 目录中
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    # 文件被传至 "MEDIA_ROOT/uploads" 目录，
    # MEDIA_ROOT 於 settings 文件中设置。
    upload = models.FileField(upload_to='uploads/')
    # # 增加时间划分
    # upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    # # 透過回调函数
    # upload = models.FileField(upload_to=user_directory_path)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    # on_delete=models.CASCADE: 进行级联删除
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    # baby_boomer_status 作为一个自定义的模型方法，
    # 可以被任何 Person 的实例调用，进行生日日期判断。
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."

        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    # full_name 模型方法被 Python 的属性装饰器转换成了一个类属性
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    # Python 的魔法方法，用于返回实例对象的打印字符串，
    # 为了让显示的内容更直观更易懂，往往會自定义这个方法。
    def __str__(self):
        return self.first_name + self.last_name
