from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from carProject.car_owner.validators import char_validator, name_validator, password_validator


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2, "Username must be at least 2 chars long!"), char_validator], unique=True)
    email = models.EmailField(unique=True, error_messages={'unique': "This email is already in use! Provide a new one."})
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, "Age should be 18 years and above."), MaxValueValidator(100, 'Age cannot be more than 100.')], help_text="Age should be between 18 and 100 years old.")
    first_name = models.CharField(max_length=30, blank=True, null=True, validators=[name_validator])
    last_name = models.CharField(max_length=30, blank=True, null=True, validators=[name_validator])
    profile_picture = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=30, validators=[password_validator])

    def get_absolute_url(self):
        return reverse('index', args=[])

    def __str__(self):
        return self.username

    @property
    def total_car_price(self):
        return self.cars.aggregate(total_price=Sum('price'))['total_price'] or 0.0

