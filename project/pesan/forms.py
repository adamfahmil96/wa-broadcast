from django import forms

from .models import Templates
from grup.models import Grup
from desa.models import Desa

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


class SendForm(forms.Form):
    group   = forms.ModelChoiceField(
        queryset    = Grup.objects.all(),
        widget      = forms.Select(
            attrs       = {
                'class': 'form-control'
            }
        )
    )
    desa    = forms.ModelChoiceField(
        queryset    = Desa.objects.all(),
        widget      = forms.Select(
            attrs   = {
                'class': 'form-control'
            }
        ),
        required=False
    )
    template_pesan  = forms.ModelChoiceField(
        queryset    = Templates.objects.all(),
        widget      = forms.Select(
            attrs   = {
                'class': 'form-control'
            }
        )
    )