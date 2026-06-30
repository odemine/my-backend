from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehicle

@api_view(['GET'])
def vehicle_list(request):
    queryset = Vehicle.objects.all()
    data = []
    for vehicle in queryset:
        data.append({
            "id": vehicle.id,
            "name": vehicle.name,
            "type": vehicle.vehicle_type,
            "image": vehicle.image,
            "price": vehicle.price,
            "badge": {
                "icon": vehicle.badge_icon,
                "label": vehicle.badge_label
            }
        })
    return Response(data)
@api_view(['POST']) # 🚀 Make sure to include the @ symbol!
def create_booking(request):
    data = request.data
    vehicle = Vehicle.objects.get(id=data['vehicle_id'])
    
    booking = Booking.objects.create(
        vehicle=vehicle,
        pickup_date=data['pickup_date'],
        dropoff_date=data['dropoff_date'],
        total_price=data['total_price']
    )
from .models import Vehicle

@api_view(['POST'])
def add_vehicle(request):
    data = request.data
    # This creates a new entry in your database
    new_vehicle = Vehicle.objects.create(
        name=data['name'],
        vehicle_type=data['vehicle_type'],
        image=data['image'],
        price=data['price'],
        badge_icon=data['badge_icon'],
        badge_label=data['badge_label']
    )
    return Response({"message": "Vehicle added successfully!", "id": new_vehicle.id})