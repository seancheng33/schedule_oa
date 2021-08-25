from django.urls import path
from usercenter import views

urlpatterns = [
    path('', views.login, name='login'),
    path(r'register', views.register,name='register'),
]