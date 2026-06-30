from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, PromoViewSet

router = DefaultRouter()
router.register(r'promos', PromoViewSet, basename='promo')
router.register(r'', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]