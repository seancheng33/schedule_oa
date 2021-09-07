from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from usercenter import models
from usercenter.userforms import RegisterModelForm
from usercenter.userforms import LoginForm


# Create your views here.
def index(request):

    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})

    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user_object = models.UserInfo.objects.filter(Q(username=username)|Q(email=username)|Q(mobile_phone=username)).filter(password=password).first()
        if user_object:
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60*60*24*7)
            # url = reverse('index',kwargs={'form': form,'session': request.session})
            return redirect('index')

    form.add_error('username','用户名或密码错误')
    print(form)

    return render(request,'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})

    form = RegisterModelForm(data=request.POST)
    # print(form)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return JsonResponse({'status':True,'data':'/login/'})

    return JsonResponse({'status': False, 'error': form.errors})

def project_index(request):

    return render(request, 'project.html')
