from django.db import models

# Create your models here.

class Product(models.Model):
    # Tuple
    SIZES = (
        # 實際儲存內容: 對應項目說明
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    # Stock Keeping Unit: 存貨單位
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    # Quantity: 數量
    qty = models.IntegerField(default=0)
    
    # 產生資料項目以 name 欄位內容顯示
    def __str__(self):
        return self.name

class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()

# 繼承自 models.Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
