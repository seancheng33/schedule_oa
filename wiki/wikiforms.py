from django import forms
from wiki.models import Wiki

class WikiModelForm(forms.ModelForm):
    class Meta:
        model = Wiki
        exclude = ['depth']

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)