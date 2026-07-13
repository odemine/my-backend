from django.urls import path
from . import views

urlpatterns = [
    path('', views.promocode_list, name='promocode_list'),
    path('validate/', views.validate_promocode, name='validate_promocode'),  # 🟢 Added path
    path('<int:pk>/', views.promocode_detail, name='promocode_detail'),
]