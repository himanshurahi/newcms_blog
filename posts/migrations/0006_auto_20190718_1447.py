# Generated by Django 2.2.3 on 2019-07-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190718_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='posts.category'),
        ),
    ]
