from django.core.management.base import BaseCommand
from vehicles.models import Vehicle  # Change 'vehicles' if your app folder name is different

class Command(BaseCommand):
    help = 'Seeds the database with the React vehicle mock data'

    def handle(self, *args, **options):
        vehicles_data = [
            {"name": "Xiaomi YU7", "type": "ev", "image": "/image/xiaomi-YU7.JPG", "price": 70},
            {"name": "Audi RS7", "type": "fuel", "image": "/image/Audi-RS7.jpg", "price": 180},
            {"name": "Aprilia RSV4", "type": "bike", "image": "/image/aprilia-rsv4.jpg", "price": 140},
            {"name": "BMW M4 AMG GT2", "type": "fuel", "image": "/image/bmw-m4-amg-gt2.jpg", "price": 220},
            {"name": "BMW M1000RR", "type": "bike", "image": "/image/bmw-M1000rr.webp", "price": 180},
            {"name": "Tesla Model 3", "type": "ev", "image": "/image/Tesla-Model3.webp", "price": 75},
            {"name": "BMW S1000RR", "type": "bike", "image": "/image/bmw-s1000rr.avif", "price": 150},
            {"name": "Xiaomi SU7", "type": "ev", "image": "/image/xiaomi-su7.jpg", "price": 90},
            {"name": "BMW M4", "type": "fuel", "image": "/image/bmw-m4.webp", "price": 160},
            {"name": "Audi EV", "type": "ev", "image": "/image/Audi-ev.avif", "price": 80},
            {"name": "Ducati Panigale V4", "type": "bike", "image": "/image/ducati-panigale-v4.jpg", "price": 170},
            {"name": "Ducati V4 Turisho", "type": "bike", "image": "/image/Ducati-V4-Turisho.webp", "price": 160},
            {"name": "BMW X5", "type": "fuel", "image": "/image/BMW-X5.avif", "price": 140},
            {"name": "Bugatti Chiron", "type": "fuel", "image": "/image/bugatti-chiron.avif", "price": 900},
            {"name": "Lexus RZ", "type": "ev", "image": "/image/Lexus-RZ.jpg", "price": 90},
            {"name": "Honda CBR1000RR", "type": "bike", "image": "/image/honda-cbr1000rr.jpg", "price": 130},
            {"name": "BYD Sealion 7", "type": "ev", "image": "/image/byd-sealion7.webp", "price": 65},
            {"name": "Lamborghini Huracan", "type": "fuel", "image": "/image/Lamborghini-Huracan.webp", "price": 500},
            {"name": "Kawasaki Ninja H2R", "type": "bike", "image": "/image/kawasaki-ninja-h2r.jpg", "price": 350},
            {"name": "Tesla Model S", "type": "ev", "image": "/image/Tesla-ModelS.webp", "price": 130},
            {"name": "Range Rover Defender", "type": "fuel", "image": "/image/Range-Rover-defender.webp", "price": 220},
            {"name": "Mercedes C300", "type": "fuel", "image": "/image/Mercedes-C300.webp", "price": 110},
            {"name": "BYD Yangwang U9", "type": "ev", "image": "/image/BYD-YangwangU9.webp", "price": 250},
            {"name": "Suzuki GSX-R1000", "type": "bike", "image": "/image/Suzuki-GSX-R1000.jpg", "price": 120},
            {"name": "Porsche 911", "type": "fuel", "image": "/image/porsche-911.webp", "price": 350},
            {"name": "Mazda EZ-6", "type": "ev", "image": "/image/mazda-EZ66.jpg", "price": 160},
            {"name": "Ferrari F8 Tributo", "type": "fuel", "image": "/image/Ferrari-F8-Tributo.jpeg", "price": 600},
            {"name": "Ford Mustang GT", "type": "fuel", "image": "/image/Ford-Mustang-GT.webp", "price": 180},
            {"name": "Yamaha R6", "type": "bike", "image": "/image/yamaha-r6.webp", "price": 110},
            {"name": "Ford Mustang", "type": "fuel", "image": "/image/Ford-Mustang.avif", "price": 150},
            {"name": "Yamaha R1M", "type": "bike", "image": "/image/yamaha-r1m.jpg", "price": 160}
        ]

        self.stdout.write(self.style.SUCCESS('🌱 Seeding vehicle assets into Django...'))
        count = 0
        
        for item in vehicles_data:
            # get_or_create prevents adding duplicates if you run this twice
            vehicle, created = Vehicle.objects.get_or_create(
                name=item["name"],
                defaults={
                    "type": item["type"],
                    "image": item["image"],
                    "price": item["price"]
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'✅ Complete! Seeded {count} new vehicles.'))