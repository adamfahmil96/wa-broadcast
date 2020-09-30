from django import forms

from .models import Desa

class DesaForm(forms.ModelForm):
    class Meta:
        model   = Desa
        fields  = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs   = {
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama desa',
                }
            )
        }