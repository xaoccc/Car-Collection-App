from django import forms
from carProject.car_owner.models import Profile


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }