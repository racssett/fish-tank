from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  return render(request, 'fish/index.html', { 'fish': fish })


class Fish: 
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

fish = [
  Fish('Lolo', 'clownfish', 'Kinda funny.', 3),
  Fish('Sachi', 'angel fish', 'Looks like an angel.', 0),
  Fish('Fancy', 'starfish', 'Happy orange star.', 4),
  Fish('Bonk', 'unknown', 'Blubs loudly.', 6)
]