"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'Blog.views.home', name='home'),
                       url(r'^about/$','Blog.views.about',name='about'),
                       url(r'^articles/(?P<article_id>[0-9]+)/$','Blog.views.show_article', name = 'article')
                      )
