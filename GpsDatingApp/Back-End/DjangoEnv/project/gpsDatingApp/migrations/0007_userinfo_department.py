# Generated by Django 3.1.2 on 2020-12-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0006_auto_20201218_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='department',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
