from django.contrib import admin

from carProject.car_owner.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'age', 'first_name', 'last_name', 'profile_picture', 'password']
    search_fields = ['username']



