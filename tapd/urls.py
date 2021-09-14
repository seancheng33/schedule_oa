"""tapd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from captcha import views
from usercenter.views import login, index, logout
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('index',index,name='index'),
    path(r'captcha/', include('captcha.urls')),
    path(r'refresh/$', views.captcha_refresh, name='captcha-refresh'),
    path(r'usercenter/',include('usercenter.urls')),
    path(r'login/',login,name='login'),
    path(r'logout/', logout, name='logout'),
    path(r'wiki/', include('wiki.urls')),
]
