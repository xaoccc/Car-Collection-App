from django import forms

from carProject.car.models import Car


class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"
        return form

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price', 'owner']
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }

class CarDeleteForm(ReadonlyViewMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price', 'owner']
    def __init__(self, *args, **kwargs):
        super(CarDeleteForm, self).__init__(*args, **kwargs)
        self.fields['type'].disabled = True
        self.fields['type'].required = False





