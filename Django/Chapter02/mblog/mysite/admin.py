from django.contrib import admin
from mysite.models import Post

# Register your models here.

# 自訂 Post 顯示方式 (繼承自 admin.ModelAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

# 納管
admin.site.register(Post, PostAdmin)
