from django import forms

class DesaForm(forms.Form):
    name = forms.CharField(
        label       = 'Nama Desa',
        max_length  = 100,
        widget      = forms.TextInput(
            attrs   = {
                'class': 'form-control',
                'placeholder': 'Masukkan nama desa',
            }
        )
    )