from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def tasks(request):
    data=Task.objects.all()
    if request.method=='POST':
        task=request.POST.get(task)
        status=request.POST.get(status)
        data=Task(task=task,status=status)
        data.save()
        return redirect('tasks')

    return render(request,'task.html',{'data':data})

def taskdelete(request,pk):
    data=Task.objects.get(id=pk)
    data.delete()
    return render(request,'task.html')

def taskedit(request,pk):
    if request.method=='POST':
        data=Task.objects.get(id=pk)
        data.task=request.POST['task']
        data.status=request.POST['status']
        data.save()

    return render(request,'taskedit.html')