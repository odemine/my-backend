import os
import sys
import django

# This tells Python to look one level up from the script location so it finds 'vehicles'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BACKEND.settings')
django.setup()

from promocode.models import PromoCode
from vehicles.models import Vehicle
vehicles_data = [
    {"name": "Xiaomi YU7", "vehicle_type": "ev", "image": "/image/xiaomi-YU7.JPG", "price": 70, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Audi RS7", "vehicle_type": "fuel", "image": "/image/Audi-RS7.jpg", "price": 180, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Aprilia RSV4", "vehicle_type": "bike", "image": "/image/aprilia-rsv4.jpg", "price": 140, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "BMW M4 AMG GT2", "vehicle_type": "fuel", "image": "/image/bmw-m4-amg-gt2.jpg", "price": 220, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "BMW M1000RR", "vehicle_type": "bike", "image": "/image/bmw-M1000rr.webp", "price": 180, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "Tesla Model 3", "vehicle_type": "ev", "image": "/image/Tesla-Model3.webp", "price": 75, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "BMW S1000RR", "vehicle_type": "bike", "image": "/image/bmw-s1000rr.avif", "price": 150, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "Xiaomi SU7", "vehicle_type": "ev", "image": "/image/xiaomi-su7.jpg", "price": 90, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "BMW M4", "vehicle_type": "fuel", "image": "/image/bmw-m4.webp", "price": 160, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Audi EV", "vehicle_type": "ev", "image": "/image/Audi-ev.avif", "price": 80, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Ducati Panigale V4", "vehicle_type": "bike", "image": "/image/ducati-panigale-v4.jpg", "price": 170, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "Ducati V4 Turisho", "vehicle_type": "bike", "image": "/image/Ducati-V4-Turisho.webp", "price": 160, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "BMW X5", "vehicle_type": "fuel", "image": "/image/BMW-X5.avif", "price": 140, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Bugatti Chiron", "vehicle_type": "fuel", "image": "/image/bugatti-chiron.avif", "price": 900, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Lexus RZ", "vehicle_type": "ev", "image": "/image/Lexus-RZ.jpg", "price": 90, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Honda CBR1000RR", "vehicle_type": "bike", "image": "/image/honda-cbr1000rr.jpg", "price": 130, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "BYD Sealion 7", "vehicle_type": "ev", "image": "/image/byd-sealion7.webp", "price": 65, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Lamborghini Huracan", "vehicle_type": "fuel", "image": "/image/Lamborghini-Huracan.webp", "price": 500, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Kawasaki Ninja H2R", "vehicle_type": "bike", "image": "/image/kawasaki-ninja-h2r.jpg", "price": 350, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "Tesla Model S", "vehicle_type": "ev", "image": "/image/Tesla-ModelS.webp", "price": 130, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Range Rover Defender", "vehicle_type": "fuel", "image": "/image/Range-Rover-defender.webp", "price": 220, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Mercedes C300", "vehicle_type": "fuel", "image": "/image/Mercedes-C300.webp", "price": 110, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "BYD Yangwang U9", "vehicle_type": "ev", "image": "/image/BYD-YangwangU9.webp", "price": 250, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Suzuki GSX-R1000", "vehicle_type": "bike", "image": "/image/Suzuki-GSX-R1000.jpg", "price": 120, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "Porsche 911", "vehicle_type": "fuel", "image": "/image/porsche-911.webp", "price": 350, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Mazda EZ-6", "vehicle_type": "ev", "image": "/image/mazda-EZ66.jpg", "price": 160, "badge_icon": "fas fa-bolt", "badge_label": "EV"},
    {"name": "Ferrari F8 Tributo", "vehicle_type": "fuel", "image": "/image/Ferrari-F8-Tributo.jpeg", "price": 600, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Ford Mustang GT", "vehicle_type": "fuel", "image": "/image/Ford-Mustang-GT.webp", "price": 180, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Yamaha R6", "vehicle_type": "bike", "image": "/image/yamaha-r6.webp", "price": 110, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"},
    {"name": "Ford Mustang", "vehicle_type": "fuel", "image": "/image/Ford-Mustang.avif", "price": 150, "badge_icon": "fas fa-gas-pump", "badge_label": "Fuel"},
    {"name": "Yamaha R1M", "vehicle_type": "bike", "image": "/image/yamaha-r1m.jpg", "price": 160, "badge_icon": "fas fa-motorcycle", "badge_label": "Bike"}
]

promocode_data = [
    {"name": "Long Term Rental", "code" : "LONG30", "discount_percentage": 30, "description": "Rent any vehicle for 7 or more days and unlock our most generous discount."},
    {"name": "Weekend Special", "code" : "WEEKEND20", "discount_percentage": 20, "description": "Rent any EV cars for 2 or 3 days over the weekend and enjoy a 20% discount."},
    {"name": "Weekday Deal", "code" : "WEEKDAY25", "discount_percentage": 25, "description": "Beat the weekend rush. Rent Monday through Thursday and enjoy 25% savings."},
    {"name": "New Customer", "code" : "NEW50", "discount_percentage": 50, "description" : "Welcome! Get 50% off for your first rental as a token of appreciation."},
    {"name": "Summer Ride", "code" : "SUMMERRIDE", "discount_percentage": 40, "description": "Rent any big bikes to explore new places this summer and save 40% off."},
    {"name": "Luxury Package", "code" : "LUXURY15", "discount_percentage": 15, "description": "Upgrade your experience to our premium luxury vehicle tier and save 15%."},
]

# --- Run Vehicles Seeding ---
print("Seeding vehicles into database...")
for item in vehicles_data:
    Vehicle.objects.get_or_create(
        name=item["name"],
        type=item["vehicle_type"],
        image=item["image"],
        price=item["price"]
    )
print("Vehicles seeding complete!")

# --- Run Promocodes Seeding ---
print("\nClearing old PromoCodes to prevent skipped values...")
PromoCode.objects.all().delete()  # Deletes any existing bad/empty data first

print("Seeding new promocodes into database...")
promo_count = 0
for item in promocode_data:
    # Creating records with the proper names and codes
    PromoCode.objects.create(
        name=item["name"],                  # Maps correctly to your new 'name' column
        code=item["code"],                  # Maps correctly to 'code' column
        discount_percentage=item["discount_percentage"],
        description=item["description"],
        status="active"
    )
    promo_count += 1
print(f"PromoCodes seeding complete! Successfully seeded {promo_count} codes.")