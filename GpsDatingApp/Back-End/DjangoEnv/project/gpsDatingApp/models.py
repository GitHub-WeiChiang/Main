from django.db import models
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField

from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.randomCode.RandomCodeGeneratorSingleton import RandomCodeGeneratorSingleton
from gpsDatingApp.randomCode.RandomCodeType import RandomCodeType

import uuid
import os

# Create your models here.

class registerInfo(models.Model):
    userId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(max_length = 50, unique = True)
    registerTime = models.DateTimeField()
    registerCity = models.CharField(max_length = 50)
    registerDistrict = models.CharField(max_length = 50, default = "")
    registerCoordinateLng = models.FloatField(default = -1)
    registerCoordinateLat = models.FloatField(default = -1)

class basicInfo(models.Model):
    userId = models.UUIDField(primary_key = True)
    rolePermission = models.CharField(max_length = 20, default = "")
    nickname = models.CharField(max_length = 20, default = "")
    birthday = models.DateField(default = "1970-01-01")
    sex = models.CharField(max_length = 20, default = "")
    interest = ListTextField(
        base_field = models.CharField(max_length = 20),
        default = []
    )

class advancedInfo(models.Model):
    userId = models.UUIDField(primary_key = True)
    introduction = models.TextField(default = "")
    school = models.CharField(max_length = 50, default = "")
    department = models.CharField(max_length = 50, default = "")
    country = models.CharField(max_length = 20, default = "")
    city = models.CharField(max_length = 20, default = "")

class matchingInfo(models.Model):
    userId = models.UUIDField(primary_key = True)
    matchingAge = ListCharField(
        base_field = models.IntegerField(),
        max_length = 5,
        default = []
    )
    # 男女: 0、男男: 1、女女: 2、都可: 3
    matchingKind = models.IntegerField(default = -1)

class friendListInfo(models.Model):
    userId = models.UUIDField(primary_key = True)
    friendList = ListTextField(
        base_field = models.CharField(max_length = 36),
        default = []
    )

class blockadeListInfo(models.Model):
    userId = models.UUIDField(primary_key = True)
    blockadeList = ListTextField(
        base_field = models.CharField(max_length = 36),
        default = []
    )

def avatar_directory_path(instance, filename):
    root: str = "avatar"
    ext: str = filename.split(".")[-1]
    prefix: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.FILE_NAME_PREFIX_CODE)
    filename: str = "{}.{}".format(prefix + "-" + str(uuid.uuid4()), ext)
    return os.path.join(root, str(instance.userId), filename)

class avatar(models.Model):
    userId = models.UUIDField(primary_key = True)
    image = models.ImageField(upload_to = avatar_directory_path, null = True, default = None)

def life_sharing_directory_path(instance, filename):
    root: str = "lifeSharing"
    ext: str = filename.split(".")[-1]
    prefix: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.FILE_NAME_PREFIX_CODE)
    filename: str = "{}.{}".format(prefix + "-" + str(uuid.uuid4()), ext)
    return os.path.join(root, str(instance.userId), filename)

class lifeSharing(models.Model):
    userId = models.UUIDField()
    num = models.IntegerField()
    image = models.ImageField(upload_to = life_sharing_directory_path, null = True, default = None)

class lifeSharingOrder(models.Model):
    userId = models.UUIDField()
    order = ListCharField(
        base_field = models.IntegerField(),
        max_length = 11,
        default = [0, 1, 2, 3, 4, 5]
    )

class accountStatus(models.Model):
    userId = models.UUIDField(primary_key = True)
    isCompleteFirstSetting = models.BooleanField(default = False)
    # use enum
    enableFunction = ListTextField(
        base_field = models.IntegerField(),
        default = []
    )
    lastJwtRefreshTime = models.DateTimeField()

class pairingRecord(models.Model):
    userIdA = models.UUIDField()
    userIdB = models.UUIDField()
    time = models.DateTimeField()
    city = models.CharField(max_length = 50, default = "")
    district = models.CharField(max_length = 50, default = "")
    coordinateLng = models.FloatField(default = -1)
    coordinateLat = models.FloatField(default = -1)

class reservation(models.Model):
    email = models.EmailField(unique = True, max_length = 50)
    reserveTime = models.DateTimeField()
    reserveCity = models.CharField(max_length = 50)
    isRegister = models.BooleanField(default = False)
