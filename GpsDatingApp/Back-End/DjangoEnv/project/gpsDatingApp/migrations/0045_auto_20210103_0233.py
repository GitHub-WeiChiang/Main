# Generated by Django 3.1.2 on 2021-01-02 18:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0044_auto_20210103_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountstatus',
            name='lastJwtRefreshTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 18, 33, 35, 263265, tzinfo=utc)),
        ),
    ]