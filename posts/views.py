from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Posts, category
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def allposts(request):
	post = Posts.objects.filter(author_id = request.user.id).order_by('-id')
	category1 = category.objects.all()
	return render(request, 'all_posts.html',{'posts':post,'category':category1})



@login_required(login_url = 'login')
def addposts(request):
	category1 = category.objects
	if request.method == 'POST':
		post = Posts()
		post.title = request.POST['title']
		post.pub_date = datetime.date.today()
		post.body = request.POST['body']
		post.status = request.POST['status']
		post.author_id = request.user.id
		post.category_id = request.POST['category_id']
		post.save()
		return redirect('allposts')

	else:
		
		return render(request,'add_posts.html',{'category':category1})
@login_required(login_url = 'login')
def editpost(request, post_id):
	
	category1 = category.objects
	
	try:
		post = Posts.objects.get(id=post_id,author_id=request.user.id)
	except Posts.DoesNotExist:
		
		return redirect('home')

	if request.method == 'POST':

		post = Posts.objects.get(id = post_id)
		post.title = request.POST['title']
		post.body  = request.POST['body']
		post.status = request.POST['status']
		post.category_id = request.POST['category_id']
		post.save()
		return redirect('home')
	return render(request,'edit_post.html',{'posts':post,'category':category1})

	

# def test(request):
# 	category1 = category.objects.all
# 	return render(request,'test.html',{'category':category1})
	
@login_required(login_url = 'login')
def delete(request, post_id):
	Posts.objects.filter(id = post_id, author_id = request.user.id).delete()
	return redirect('allposts')

