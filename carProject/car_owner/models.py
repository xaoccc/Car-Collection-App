from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(validators=(MinValueValidator(18), "Age requirement: 18 years and above."))
    profile_picture = models.URLField(blank=True, null=True)
    car = models.OneToOneField('Car', on_delete=models.CASCADE)