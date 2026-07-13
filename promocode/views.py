from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PromoCode
from .serializers import PromoCodeSerializer

@api_view(['GET', 'POST'])
def promocode_list(request):
    if request.method == 'GET':
        promocodes = PromoCode.objects.all().order_by('-created_at')
        serializer = PromoCodeSerializer(promocodes, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = PromoCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def promocode_detail(request, pk):
    try:
        promocode = PromoCode.objects.get(pk=pk)
    except PromoCode.DoesNotExist:
        return Response({'error': 'Promo code not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PromoCodeSerializer(promocode)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PromoCodeSerializer(promocode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        promocode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 🟢 ADD THIS NEW VALIDATION ROUTE FOR YOUR FRONTEND CUSTOMER CHECKOUT
@api_view(['GET'])
def validate_promocode(request):
    code_str = request.query_params.get('code', '').strip()
    
    if not code_str:
        return Response({'valid': False, 'error': 'No promotional code string provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
    try:
        promo = PromoCode.objects.get(codename__iexact=code_str)
        
        # 🟢 Directly rejects validation if the code is hidden/inactive
        if promo.status != 'active':
            return Response({
                'valid': False, 
                'error': 'This coupon is currently inactive and cannot be used.'
            }, status=status.HTTP_200_OK)
            
        return Response({
            'valid': True,
            'codename': promo.codename,
            'discount_percentage': promo.discount_percentage,
            'condition': promo.condition
        }, status=status.HTTP_200_OK)
        
    except PromoCode.DoesNotExist:
        return Response({'valid': False, 'error': 'Invalid promotional coupon code.'}, status=status.HTTP_200_OK)