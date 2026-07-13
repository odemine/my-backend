from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PromoCodeViewSet  # Or whatever your view name is inside views.py

router = DefaultRouter()
router.register(r'', PromoCodeViewSet, basename='promocodes')

urlpatterns = [
    path('', include(router.urls)),
]