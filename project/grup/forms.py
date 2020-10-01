from django import forms

from .models import Grup

class GrupForm(forms.ModelForm):
    class Meta:
        model   = Grup
        fields  = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs   = {
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama grup',
                }
            )
        }