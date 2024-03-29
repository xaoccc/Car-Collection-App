from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Car(models.Model):
    CAR_TYPE = [
        ('Minibus', 'Minibus'),
        ('Crossover', 'Crossover'),
        ('Sports Car', 'Sports Car'),
        ('Other', 'Other'),
        ('Pickup', 'Pickup'),
    ]


    type = models.CharField(choices=CAR_TYPE)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(validators=[MinValueValidator(1980, "Year must be between 1980 and 2049!"), MaxValueValidator(2049, "Year must be between 1980 and 2049!")])
    image_url = models.URLField(unique=True, error_messages={'unique': "This image URL is already in use! Provide a new one."})
    price = models.FloatField(validators=[MinValueValidator(1.0, "Price must be at least 1.0!"), MaxValueValidator(135000000.0, "Price must be at most 135000000.0!")])
    owner = models.ForeignKey('car_owner.Profile', on_delete=models.CASCADE, related_name='cars', editable=False)

    def get_absolute_url(self):
        return reverse('car-catalogue', args=[])

    def __str__(self):
        return f"{self.model} [{self.year}]"
