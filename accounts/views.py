from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

from django.contrib import auth
from . import forms
import re
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


# Create your views here.

def login(request):
	
	if request.method  == 'POST':
		try:
			username = User.objects.get(email = request.POST['email'])
		except User.DoesNotExist:
			return render(request,'login.html',{'error':'Wrong Email OR Password'})
		

		f = auth.authenticate(username = username.username, password = request.POST['password'])
		
		if f is not None:
			auth.login(request,f)
			return redirect('home')
		else:
			return render(request,'login.html',{'error':'Wrong Username or password'})
	else:
		return render(request, 'login.html')


def signup(request):
	
	if request.method == 'POST':
		if request.POST['username'] and request.POST['email'] and request.POST['password']:
			try:
				User.objects.get(username = request.POST['username'])
				return render(request,'signup.html',{'error':'Username Already Exist'})
			except User.DoesNotExist:
				if re.match('^[a-zA-z0-9]+$', request.POST['username']):
					

					User.objects.create_user(username = request.POST['username'],password = request.POST['password'],email = request.POST['email'])
					return render(request,'login.html',{'success':'You can Login Now'})
				

				else:
					return render(request,'signup.html',{'error':'Username Error'})

	else:
		return render(request,'signup.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
	else:
		return redirect('home')
	