from django.contrib import admin

from mysite.models import Post, NewTable, Product

# Register your models here.

admin.site.register(Post)
admin.site.register(NewTable)
admin.site.register(Product)
