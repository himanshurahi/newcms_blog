# Generated by Django 2.2.3 on 2019-07-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='null', max_length=255, unique=True),
        ),
    ]
