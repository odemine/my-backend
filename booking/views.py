from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Booking, Promo
from .serializers import BookingSerializer
from promocode.models import PromoCode

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        promo_code = serializer.validated_data.get('promo_code')
        if promo_code and promo_code.strip() and promo_code.lower() != 'none':
            code_str = promo_code.strip()
            try:
                promo = PromoCode.objects.get(codename__iexact=code_str)
                if promo.status == 'inactive' or promo.status == 'expired':
                    raise ValidationError({'promo_code': f'This promo code is currently {promo.status}.'})
                    
            except PromoCode.DoesNotExist:
                raise ValidationError({'promo_code': 'Invalid promotional coupon code.'})

        serializer.save()


