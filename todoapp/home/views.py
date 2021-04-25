from django.shortcuts import render, HttpResponse
from .models import Task

# Create your views here.
def home(request):
    task = Task.objects.all()
    return render(request, 'home.html', {'task': task})