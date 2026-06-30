from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        
        # If the logged-in user is a Django superuser/staff (Admin), show everything!
        if user.is_staff or user.is_superuser:
            return Customer.objects.all()
            
        # If authenticated as a standard customer, filter by their email account identity
        if user.is_authenticated:
            return Customer.objects.filter(email=user.email)
            
        # Otherwise (for frontend anonymous requests), return all records so the admin panel lists them
        return Customer.objects.all()

    # Custom endpoint to handle the toggle suspension button click
    @action(detail=True, methods=['patch'])
    def toggle_suspend(self, request, pk=None):
        customer = self.get_object()
        # Ensure you have an 'is_suspended' BooleanField on your Customer model if tracking this
        customer.is_suspended = not getattr(customer, 'is_suspended', False)
        customer.save()
        return Response({'status': 'suspension status updated', 'is_suspended': customer.is_suspended})