from rest_framework import viewsets
from .models import PromoCode
from .serializers import PromoCodeSerializer

class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer