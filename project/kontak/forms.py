from django import forms

from .models import Contacts


class KontakForm(forms.ModelForm):
    class Meta:
        model   = Contacts
        fields  = ['norm', 'name', 'contact', 'group', 'desa']
        labels  = {
            'norm': 'No RM',
            'name': 'Nama',
            'contact': 'No HP',
            'group': 'Grup',
        }
        widgets = {
            'norm': forms.TextInput(
                attrs   = {
                    'class': 'form-control',
                    'placeholder': 'Masukkan No RM',
                }
            ),
            'name': forms.TextInput(
                attrs   = {
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama kontak',
                }
            ),
            'contact': forms.TextInput(
                attrs   = {
                    'class': 'form-control',
                    'placeholder': 'Masukkan No HP',
                }
            ),
            'group': forms.Select(
                attrs   = {
                    'class': 'form-control',
                    'id': 'id_group',
                }
            ),
            'desa': forms.Select(
                attrs   = {
                    'class': 'form-control',
                    'id': 'id_desa',
                }
            ),
        }