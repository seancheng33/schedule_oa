from django.urls import path
from wiki import views

# app_name = "wiki"
#
urlpatterns = [
    path('', views.wiki_index, name='wiki_index'),
    path('add', views.wiki_add, name='wiki_add'),
    path('catalog', views.wiki_catalog, name='wiki_catalog'),
    # path('detail', views.wiki_detail, name='wiki_detail'),
    path('edit/(?P<wiki_id>\d+)', views.wiki_edit, name='wiki_edit'),
    path('del/(?P<wiki_id>\d+)', views.wiki_del, name='wiki_del'),
    path('upload', views.wiki_upload, name='wiki_upload'),
]