# Generated by Django 3.1.2 on 2020-12-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0038_auto_20201228_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountstatus',
            old_name='lastRefreshTime',
            new_name='lastJwtRefreshTime',
        ),
    ]