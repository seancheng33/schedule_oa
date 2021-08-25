from django.http import JsonResponse
from django.shortcuts import render
from django_redis import get_redis_connection

# Create your views here.
from usercenter.userforms import RegisterModelForm
from usercenter.userforms import LoginForm

def index():
    conn = get_redis_connection()

    pass

def login(request):


    form = LoginForm()


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


