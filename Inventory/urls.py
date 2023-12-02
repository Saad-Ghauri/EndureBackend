from django.urls import path 
from . import views

urlpatterns = [
    
    path('characteristics/', views.Characteristics_View, name='characteristics'),
    path('inventory/', views.Inventory_View, name='inventory'),
    # path('inventory/', views.Inventory_View, name='inventory'),
    path('accounting/', views.Accounting_View, name='accounting'),
    path('purchasing/', views.Purchasing_View, name='purchasing'),
    path('vendors/', views.Vendors_View, name='vendors'),
    # path('u1/', views.Utilization_view_11, name='u1'),
]