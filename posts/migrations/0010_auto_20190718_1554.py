# Generated by Django 2.2.3 on 2019-07-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190718_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ManyToManyField(related_name='post_related', to='posts.category'),
        ),
    ]