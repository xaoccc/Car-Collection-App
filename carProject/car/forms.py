from django import forms
from carProject.car.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }

class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
    def __init__(self, *args, **kwargs):
        super(CarDeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = ['readonly']

        self.fields['type'].disabled = True
        self.fields['type'].required = False





