# Generated by Django 3.1.2 on 2021-01-31 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0055_auto_20210131_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pairingrecord',
            name='coordinate',
        ),
        migrations.AddField(
            model_name='pairingrecord',
            name='coordinateLat',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='pairingrecord',
            name='coordinateLng',
            field=models.FloatField(default=-1),
        ),
    ]