"""newcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
import accounts
import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.allposts, name = 'allposts'),
   
    path('add/', views.addposts, name='addposts'),
    path('edit/<int:post_id>', views.editpost, name='editpost'),
    # path('test/', views.test),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('details/<str:slug>',views.post_details, name = 'post_details'),
]
