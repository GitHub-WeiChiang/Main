# Generated by Django 3.1.2 on 2020-12-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0004_auto_20201215_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
