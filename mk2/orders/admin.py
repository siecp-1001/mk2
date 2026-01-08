from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'city', 'paid', 'created')
    list_filter = ('paid', 'created')
    search_fields = ('first_name', 'email')
