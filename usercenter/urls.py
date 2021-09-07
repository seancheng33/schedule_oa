from django.urls import path
from usercenter import views

# app_name = "usercenter"

urlpatterns = [
    path('', views.login, name='login'),
    path(r'register', views.register,name='register'),
    path(r'project', views.project_index,name='project_index'),
]