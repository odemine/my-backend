from django.contrib import admin
from .models import PromoCode

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    # This displays all your requested columns in a table layout
    list_display = ('codename', 'discount_percentage', 'condition', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('codename',)