from django import forms
from carProject.car_owner.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'first_name', 'last_name', 'profile_picture', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }