from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Booking, Promo
from .serializers import BookingSerializer, PromoSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        promo_code = serializer.validated_data.get('promo_code')
        if promo_code and promo_code.strip() and promo_code.lower() != 'none':
            code = promo_code.strip()
            try:
                promo = Promo.objects.get(code__iexact=code)
                if promo.is_used:
                    raise ValidationError({'promo_code': 'This promo code has already been used.'})
                promo.is_used = True
                promo.save()
            except Promo.DoesNotExist:
                hardcoded_codes = ['LONG30', 'WEEKEND20', 'WEEKDAY25', 'NEW50', 'SUMMERRIDE', 'LUXURY15']
                if code.upper() not in hardcoded_codes:
                    raise ValidationError({'promo_code': 'Invalid promotional coupon code.'})
        
        serializer.save()

class PromoViewSet(viewsets.ModelViewSet):
    queryset = Promo.objects.all().order_by('-created_at')
    serializer_class = PromoSerializer

    @action(detail=False, methods=['get'], url_path='validate')
    def validate(self, request):
        code = request.query_params.get('code', '').strip().upper()
        if not code:
            return Response({'valid': False, 'error': 'No code provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            promo = Promo.objects.get(code__iexact=code)
            if promo.is_used:
                return Response({'valid': False, 'error': 'This promo code has already been used.'}, status=status.HTTP_200_OK)
            return Response({'valid': True, 'discount_percent': promo.discount_percent}, status=status.HTTP_200_OK)
        except Promo.DoesNotExist:
            hardcoded_codes = ['LONG30', 'WEEKEND20', 'WEEKDAY25', 'NEW50', 'SUMMERRIDE', 'LUXURY15']
            # If it's one of the hardcoded codes, let's treat it as valid but indicate database validation didn't override it.
            # We can return its details if we want or just say invalid to force DB-only, or return a fake response.
            # Wait, let's see how Rent.jsx handles validatePromoCode.
            # If Rent.jsx calls this API first, it can either check this API and then fallback, or the API can say "it is valid" if it's hardcoded.
            # Let's make the API support the hardcoded codes too to keep validation DRY!
            if code in hardcoded_codes:
                discount_map = {
                    'LONG30': 30,
                    'WEEKEND20': 20,
                    'WEEKDAY25': 25,
                    'NEW50': 50,
                    'SUMMERRIDE': 40,
                    'LUXURY15': 15,
                }
                return Response({'valid': True, 'discount_percent': discount_map[code]}, status=status.HTTP_200_OK)
            
            return Response({'valid': False, 'error': 'Invalid promotional coupon code.'}, status=status.HTTP_200_OK)