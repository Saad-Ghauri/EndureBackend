from django.urls import path 
from . import views

urlpatterns = [
  
    path('u1/', views.Utilization_1, name='u1'),
    path('u2/', views.Utilization_2, name='u2'),
    path('u3/', views.Utilization_3, name='u3'),
    path('u4/', views.Utilization_4, name='u4'),
    path('u5/', views.Utilization_5, name='u5'),
    path('u6/', views.Utilization_6, name='u6'),
]