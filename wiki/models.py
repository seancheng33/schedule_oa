from django.db import models
from django import forms

# Create your models here.
class Wiki(models.Model):
    # profile = models.ForeignKey(verbose_name='项目',to='Project',on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='内容')

    depth = models.IntegerField(verbose_name='深度',default=1)

    parent = models.ForeignKey(verbose_name='父级文字',to='Wiki', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title


    def __init__(self,*args, **kwagrs):
        super().__init__(*args, **kwagrs)