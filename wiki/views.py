import os
from datetime import datetime

from PIL import Image
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from wiki.models import Wiki
from django.shortcuts import render, redirect
from wiki.wikiforms import WikiModelForm


# Create your views here.
def wiki_index(request):
    wiki_id = str(request.GET.get('wiki_id'))
    # 判断wiki_id是否存在，只有这两者都存在，才回去查询和显示内容
    if wiki_id and wiki_id.isdecimal():
        wiki_object = Wiki.objects.filter(id=wiki_id).first()
        return render(request, 'wiki.html', {'wiki_object': wiki_object})

    return render(request,'wiki.html')


def wiki_add(request):
    if request.method == 'GET':
        form = WikiModelForm(request)
        return render(request,'wiki_form.html',{'form':form})

    form = WikiModelForm(request,data=request.POST)
    if form.is_valid():
        if form.instance.parent:
            form.instance.depth = form.instance.depth + 1
        else:
            form.instance.depth = 1
        form.save()
        return redirect('wiki_index')


def wiki_catalog(request):
    result = Wiki.objects.filter().values("id",'title','parent').order_by('depth','id')

    return JsonResponse({'status': True, 'result': list(result)})

def wiki_edit(request, wiki_id):
    wiki_object = Wiki.objects.filter(id=wiki_id).first()
    if not wiki_object:
        return redirect('wiki_index')
    if request.method == 'GET':
        form = WikiModelForm(request,instance=wiki_object)
        return render(request,'wiki_form.html',{'form':form})

    form = WikiModelForm(request,data=request.POST,instance=wiki_object)
    if form.is_valid():
        if form.instance.parent:
            form.instance.depth = form.instance.depth + 1
        else:
            form.instance.depth = 1
        form.save()
        return redirect('wiki_index')

def wiki_del(request,wiki_id):
    Wiki.objects.filter(id=wiki_id).delete()

    return redirect('wiki_index')

@csrf_exempt
@xframe_options_sameorigin
def wiki_upload(request):
    print("接收到图片")
    image_object = request.FILES.get('editormd-image-file')

    if image_object:
        image_object.name
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + image_object.name
        current_path = os.path.abspath(os.path.dirname(__file__))
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)

        filedir = os.path.join(father_path,'wiki/static/upload')

        newname = (os.path.join(filedir,filename))

        Image.open(image_object).save(newname)  # 使用pil打开传过来的图片并且将其保存
        host_name = request.get_host()      # 获取请求的网址的主机名和端口号。用于后面的组合
        image_url = 'http://' + host_name + '/' + ('/').join(newname.split('/')[-3:])

        data = {'success':1,'message':'图片上次成功','url':image_url}
        return JsonResponse(data,content_type='text/html')
    return JsonResponse()