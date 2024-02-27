from django.contrib import admin

# Register your models here.
from carProject.car.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ['type', 'model', 'year', 'price', 'image_url']