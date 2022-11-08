from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fish/', views.fish_index, name='fish_index'),
  path('fish/<int:fish_id>/', views.fish_detail, name='fish_detail'),
  path('fish/create/', views.FishCreate.as_view(), name='fish_create'),
  path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
  path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
  path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('enrichments/create/', views.EnrichmentCreate.as_view(), name='enrichments_create'),
  path('enrichments/<int:pk>/', views.EnrichmentDetail.as_view(), name='enrichments_detail'),
  path('enrichments/', views.EnrichmentList.as_view(), name='enrichments_index'),
  path('enrichments/<int:pk>/update/', views.EnrichmentUpdate.as_view(), name='enrichments_update'),
  path('enrichments/<int:pk>/delete/', views.EnrichmentDelete.as_view(), name='enrichments_delete')
]