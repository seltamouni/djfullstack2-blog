"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from turtle import home
from django.contrib import admin
from django.urls import path
from posts.views import all_posts, edit_post, new_post, single_post, new_post, edit_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', all_posts, name='all_posts'),
    path('blog/<int:id>',single_post, name='single_post'),
    path('new',new_post,name='new_post'),
    path('blog/<int:id>/edit', edit_post, name='edit_post'),
    path('blog/<int:id>/delete', delete_post, name='delete_post')
    
]
