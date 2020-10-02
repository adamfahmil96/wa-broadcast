from django import forms

from .models import Templates

class TemplateForm(forms.ModelForm):
    class Meta:
        model   = Templates
        fields  = ['group', 'name', 'text']
        labels  = {
            'group': 'Grup',
            'name': 'Nama Template',
            'text': 'Isi Template',
        }
        widgets = {
            'group': forms.Select(
                attrs   = {
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs   = {
                    'class': 'form-control',
                    'placeholder': 'Masukkan Nama Template',
                }
            ),
            'text': forms.Textarea(
                attrs   = {
                    'class': 'form-control',
                }
            )
        }