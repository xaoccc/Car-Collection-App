from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse

from carProject.car_owner.validators import char_validator

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2, "Username must be at least 2 chars long!"), char_validator])
    email = models.EmailField()
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, "Age requirement: 18 years and above.")], help_text="Age requirement: 18 years and above.")
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('index', args=[])

