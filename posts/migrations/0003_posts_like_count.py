# Generated by Django 2.2.3 on 2019-07-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190717_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='like_count',
            field=models.IntegerField(default='0'),
        ),
    ]