from django.shortcuts import render
from .models import Fish

from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fish = Fish.objects.all()
  return render(request, 'fish/index.html', { 'fish': fish })

