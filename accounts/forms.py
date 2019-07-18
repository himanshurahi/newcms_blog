from django import forms
from django.contrib.auth.models import User


class SignUp(forms.Form):
	email = forms.EmailField(label='')
	password = forms.CharField(max_length=32, widget=forms.PasswordInput, label = '')
	username = forms.CharField(max_length=15, label = '')
	



	def __init__(self, *args, **kwargs):
		super(SignUp, self).__init__(*args, **kwargs)
		self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Password'
		
		self.fields['password'].widget.attrs['class'] = 'form-control'