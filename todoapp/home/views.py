from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Task
from .forms import TaskForm, UpdateForm

# Create your views here.
def home(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    tasks = Task.objects.all()
    #print(task.count())
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

def edit(request, id=id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        form = UpdateForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home:home')


    form = UpdateForm(request.POST or None, instance=task)
    print(form)
    return render(request, 'edit.html', {'form': form})