from django import forms

from carProject.car.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price', 'owner']
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }

class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {
            'type': forms.TextInput(attrs={'disabled': 'disabled'}),
            'model': forms.TextInput(attrs={'readonly': 'readonly'}),
            'year': forms.TextInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
            'price': forms.TextInput(attrs={'readonly': 'readonly'}),
        }



