from django.urls import path
from usercenter import views

urlpatterns = [
    path('', views.register, name='register'),
    path('^register', views.register,name='register'),
]