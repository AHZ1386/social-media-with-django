
from django.forms import ModelForm, TextInput
from .models import twitt


class TwitteFrom(ModelForm):
    class Meta:
        model = twitt
        fields = ['text',]
        widgets = {
            'text': TextInput(attrs={'class': 'form-control'}),
            }
