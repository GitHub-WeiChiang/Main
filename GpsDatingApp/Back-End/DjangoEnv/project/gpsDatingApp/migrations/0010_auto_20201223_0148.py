# Generated by Django 3.1.2 on 2020-12-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0009_remove_pairingrecord_serialnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='advancedInfo',
            fields=[
                ('userId', models.UUIDField(primary_key=True, serialize=False)),
                ('introduction', models.TextField(blank=True)),
                ('school', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('place', models.CharField(blank=True, max_length=20)),
                ('constellation', models.IntegerField()),
                ('disposition', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='basicInfo',
            fields=[
                ('userId', models.UUIDField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20)),
                ('birthday', models.DateTimeField()),
                ('sex', models.BooleanField()),
                ('sexori', models.BooleanField()),
                ('interest', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='matchingInfo',
            fields=[
                ('userId', models.UUIDField(primary_key=True, serialize=False)),
                ('matchingAge', models.CharField(max_length=10)),
                ('matchingkind', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='socialInfo',
            fields=[
                ('userId', models.UUIDField(primary_key=True, serialize=False)),
                ('friend', models.TextField(blank=True)),
                ('blockade', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='friendInfo',
        ),
        migrations.DeleteModel(
            name='userInfo',
        ),
        migrations.RemoveField(
            model_name='registerinfo',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='lifesharing',
            name='image',
            field=models.ImageField(upload_to='lifePhotos/'),
        ),
        migrations.AlterField(
            model_name='profilepicture',
            name='image',
            field=models.ImageField(upload_to='profilePhotos/'),
        ),
        migrations.AlterField(
            model_name='registerinfo',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserveLocate',
            field=models.CharField(max_length=10),
        ),
    ]
