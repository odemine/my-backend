from django.core.management.base import BaseCommand
from promocode.models import PromoCode

class Command(BaseCommand):
    help = 'Seeds the database with the React PromoCode mock data'

    def handle(self, *ares, **options):
        promocode_data = [
            {"name": "Long Term Rental", "code" : "LONG30", "discount_percentage": 30, "condition": "Up to seven days", "description": "Rent any vehicle for 7 or more days and unlock our most generous discount."},
            {"name": "Weekend Special", "code" : "WEEKEND20", "discount_percentage": 20, "condition": "Friday, Saturday and Sunday", "description": "Rent any EV cars for 2 or 3 days over the weekend and enjoy a 20% discount."},
            {"name": "Weekday Deal", "code" : "WEEKDAY25", "discount_percentage": 25, "condition": "Monday to Thursday", "description": "Beat the weekend rush. Rent Monday through Thursday and enjoy 25% savings."},
            {"name": "New Customer", "code" : "NEW50", "discount_percentage": 50, "condition": "Welcome! Get 50% off for your first rental as a token of appreciation."},
            {"name": "Summer Ride", "code" : "SUMMERRIDE", "discount_percentage": 40, "condition": "For big bikes only and up to ten days", "description": "Rent any big bikes to explore new places this summer and save 40% off."},
            {"name": "Luxury Package", "code" : "LUXURY15", "discount_percentage": 15, "condition": "For vehicles price above 500", "description": "Upgrade your experience to our premium luxury vehicle tier and save 15%."},
        ]

        self.stdout.write(self.style.SUCCESS('🌱 Seeding promocode assets into Django...'))
        count = 0

        for item in promocode_data:
            promocode, created = PromoCode.objects.get_or_create(
                codename=item["code"], # Unique identifier lookup
                defaults={
                    "name": item["name"], # Now maps correctly to the model's new name field
                    "discount_percentage": item["discount_percentage"],
                    "condition": item["condition"],
                    "description": item["description"],
                    "status": "active"
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'✅ Complete! Seeded {count} new promocodes.'))