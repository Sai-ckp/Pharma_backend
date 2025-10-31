from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.sales_report, name='sales-report'),
    path('inventory/', views.inventory_report, name='inventory-report'),
]
