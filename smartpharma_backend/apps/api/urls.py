from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Import your viewsets
from apps.masters.views import (
    VendorViewSet,
    CustomerViewSet, 
    CategoryViewSet,
    UnitViewSet,
    ItemViewSet
)
from apps.inventory.views import InwardViewSet, OutwardViewSet, StockStatementViewSet
from apps.billing.views import BillViewSet
from apps.dashboard.views import DashboardViewSet

# Initialize the router
router = DefaultRouter()

# Register viewsets
router.register(r'vendors', VendorViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'units', UnitViewSet)
router.register(r'items', ItemViewSet)
router.register(r'inward', InwardViewSet)
router.register(r'outward', OutwardViewSet)
router.register(r'stock', StockStatementViewSet)
router.register(r'bills', BillViewSet)
router.register(r'dashboard', DashboardViewSet)

urlpatterns = [
    # JWT Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API Routes
    path('', include(router.urls)),
]