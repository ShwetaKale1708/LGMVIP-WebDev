from django.shortcuts import render,redirect
from testapp.models import resultmodel
from testapp.forms import studentForm,resultForm
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    
    return render(request,'testapp/home.html')

@login_required   
def teacher_view(request):
    results = resultmodel.objects.all()
    return render(request,'testapp/teachers.html',{'results':results})

@login_required
def create_view(request):
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/teacher')
    return render(request,'testapp/create.html',{'form':form})

@login_required
def delete_view(request,prn):
    student = resultmodel.objects.get(prn=prn)
    student.delete()
    return redirect('/teacher')

@login_required
def update_view(request,prn):
    student = resultmodel.objects.get(prn=prn)
    if request.method == 'POST':
        form = studentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/teacher')
    return render(request,'testapp/update.html',{ 'student':student})

def show_result_view(request):
    success = False
    form = forms.resultForm
    # return render(request,'testapp/home.html',{ 'forms':form})
    if request.method == 'POST':
        form = resultForm(request.POST)
        if form.is_valid():
            prn = form.cleaned_data.get('prn')
            try:
                student = resultmodel.objects.get(prn=prn)
                success = True
                return render(request,'testapp/result.html',{'success':success, 'student':student})
            except:
                pass
    form = forms.resultForm
    return render(request,'testapp/home.html',{'success':success, 'forms':form})
