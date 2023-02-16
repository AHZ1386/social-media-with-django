from django import forms
from django.forms import TextInput, ModelForm,FileInput
from Account.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'password1', 
            'password2', 
            'biography',
            'profile_image',

            ]

class LoginFrom(forms.Form):

    class Meta:
        model = CustomUser
        fields= [ 
            'username', 
            'password',
        ]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'profile_image',
            'biography',
            'last_name',
            'first_name',
            'username',]
        