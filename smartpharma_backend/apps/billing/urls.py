from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('bills', views.BillViewSet, basename='bill')

urlpatterns = [
    # Default router URLs
    path('', include(router.urls)),
    
    # Custom billing endpoints
    path('generate-bill-number/', views.generate_bill_number, name='generate-bill-number'),
   
]