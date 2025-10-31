from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('vendors', views.VendorViewSet)
router.register('customers', views.CustomerViewSet)
router.register('categories', views.CategoryViewSet)
router.register('units', views.UnitViewSet)
router.register('items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]