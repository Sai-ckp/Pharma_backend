from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('inward', views.InwardViewSet)
router.register('outward', views.OutwardViewSet)
router.register('stock', views.StockStatementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stock-summary/', views.stock_summary, name='stock-summary'),
]