from django import forms

from carProject.car.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }
