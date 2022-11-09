from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Fish, Enrichment
from .forms import FeedingForm

from django.http import HttpResponse

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def fish_index(request):
  fish = Fish.objects.filter(user=request.user)
  return render(request, 'fish/index.html', { 'fish': fish })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  enrichments_fish_doesnt_have = Enrichment.objects.exclude(id__in = fish.enrichments.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'fish/detail.html', { 'fish': fish, 'feeding_form': feeding_form, 'enrichments': enrichments_fish_doesnt_have })

class FishCreate(LoginRequiredMixin, CreateView):
  model = Fish
  fields = ['name', 'type', 'description', 'age']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = '__all__'

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fish/'

@login_required
def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('fish_detail', fish_id=fish_id)

class EnrichmentCreate(LoginRequiredMixin, CreateView):
  model = Enrichment
  fields = '__all__'

class EnrichmentList(LoginRequiredMixin, ListView):
  model = Enrichment

class EnrichmentDetail(LoginRequiredMixin, DetailView):
  model = Enrichment

class EnrichmentUpdate(LoginRequiredMixin, UpdateView):
  model = Enrichment
  fields = ['name', 'color']

class EnrichmentDelete(LoginRequiredMixin, DeleteView):
  model = Enrichment
  success_url = '/enrichments/'

@login_required
def assoc_enrichment(request, fish_id, enrichment_id):
  Fish.objects.get(id=fish_id).enrichments.add(enrichment_id)
  return redirect('fish_detail', fish_id=fish_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('fish_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)