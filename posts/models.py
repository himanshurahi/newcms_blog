from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


# Create your models here.

status_choice = (
	('draft','draft'),
	('published','published'),
)

class category(models.Model):
	title = models.CharField(max_length=255, default='null')

class Posts(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(choices = status_choice,max_length=255)
	category = models.ForeignKey(category, on_delete=models.CASCADE, default = '')
	like_count = models.IntegerField(default='0')
	


class likes(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)
	
	




