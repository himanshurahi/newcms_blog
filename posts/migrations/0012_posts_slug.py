# Generated by Django 2.2.3 on 2019-07-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20190718_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
