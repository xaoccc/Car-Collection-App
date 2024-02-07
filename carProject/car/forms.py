from django import forms

from carProject.car.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
