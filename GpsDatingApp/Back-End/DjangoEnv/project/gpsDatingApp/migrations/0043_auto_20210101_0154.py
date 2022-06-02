# Generated by Django 3.1.2 on 2020-12-31 17:54

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0042_auto_20210101_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedinfo',
            name='constellation',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='advancedinfo',
            name='disposition',
            field=django_mysql.models.ListTextField(models.CharField(max_length=10), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='interest',
            field=django_mysql.models.ListTextField(models.CharField(max_length=10), default=[], size=None),
        ),
    ]