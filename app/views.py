from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    titles=Task.objects.all()
    return render(request,'login.html',{'tasks':titles})

def post(request):
    if request.method == 'POST':
        task=request.POST.get('title')
        Task.objects.create(title=task)
        print(f' "{task}" - Task created successfully')
        messages.success(request,'TASK CREATED SUCCESSFULLY')
        return redirect('index')
    return render(request,'post.html')

def update(request,id):
    task=Task.objects.get(id=id)
    if request.method == 'POST':
        new_title=request.POST.get('title')
        task.title=new_title
        task.save()
        print(f'"{task}" - Task updated successfully')
        messages.success(request,'TASK UPDATED SUCCESSFULLY.')
        return redirect('index')
    return render(request,'update.html')

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    print(f'"{task}" - Task deleted successfully')
    messages.success(request,'TASK DELETED SUCCESSFULLY')
    return redirect('index')

def complete(request,id):
    task=Task.objects.get(id=id)
    if request.method =='POST':
        task.completed=not task.completed
        task.save()
        if task.completed == True:
            messages.success(request,'TASK MARKED AS COMPLETED')
        else:
            messages.success(request,'TASK MARKED AS INCOMPLETE')
    return redirect('index')