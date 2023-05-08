from django.db import models

# Create your models here.

# Table
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    # Settings
    class Meta:
        # 回傳順序 (以欄位 pub_date 遞減方式排序)
        ordering = ('-pub_date',)

    # 產生資料項目以 title 欄位內容顯示
    def __str__(self):
        return self.title
