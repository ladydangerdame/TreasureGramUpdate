from django import forms
from .models import Treasure

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ('name', 'value', 'location', 'material')

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
