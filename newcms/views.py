from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from posts.models import Posts, category,likes
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
	category1 = category.objects.all()
	
	posts = Posts.objects.filter(status = 'published').order_by('-id')
	print(posts)
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	
	posts = paginator.get_page(page)

	return render(request,'templates/home.html',{'posts':posts,'category':category1})



@login_required(login_url = 'login')
def like(request,post_id):
	like = likes()
	if request.method == 'POST':
		like_check = likes.objects.filter(user_id = request.user.id, post_id = post_id)
		if like_check:
			messages.error(request,'You Already Upvoted')
			return redirect('home')
		else:
			posts = Posts.objects.get(id = post_id)
			posts.like_count += 1
			like.user_id = request.user.id
			like.post_id = post_id
			like.save()
			posts.save()
			return redirect('home')

		



def search_post(request):
	search_post = request.GET['q']
	category1 = category.objects.all()
	try:
		post = Posts.objects.filter(title__icontains = search_post, status = 'published')
		return render(request, 'templates/search_result.html',{'posts':post,'search':search_post,'category':category1})
	except category.DoesNotExist:
		return render(request, 'templates/home.html',{'error':'No Result Found','search':search_post,'category':category1})


def contact(request):
	category1 = category.objects.all()
	return render(request, 'templates/contact.html',{'category':category1})


def about(request):
	category1 = category.objects.all()
	return render(request, 'templates/about.html',{'category':category1})
		
