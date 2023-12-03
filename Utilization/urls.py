from django.urls import path 
from . import views

urlpatterns = [
  
    path('u1/', views.Utilization_1, name='u1'),
]