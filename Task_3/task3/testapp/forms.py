from django import forms
from testapp.models import resultmodel
from django.forms import fields

class studentForm(forms.ModelForm):
    class Meta:
        model = resultmodel
        fields = '__all__'

class resultForm(forms.Form):
    prn = forms.CharField(max_length = 20,label ='ENTER PRN')
