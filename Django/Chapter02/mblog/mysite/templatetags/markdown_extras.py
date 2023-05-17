"""
建立過濾器並註冊在 Django 模板語言中

确保这段代码位于 Django 项目中 App 目录下的 templatetags 文件夹中
"""

import markdown

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


# 使用 register.filter 方法将 convert_markdown 过滤器注册到 Django 的模板标签库中
@register.filter
def convert_markdown(text):
    return markdown.markdown(text)
