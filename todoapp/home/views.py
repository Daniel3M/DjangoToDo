from django.shortcuts import render, HttpResponse
from .models import Task
from .forms import TasForm

# Create your views here.
def home(request):
    if request.method=='POST':
        form = TasForm(request.POST)
        if form.is_valid():
            form.save()

    task = Task.objects.all()
    form = TasForm()
    print(form)
    return render(request, 'home.html', {'task': task, 'form': form})