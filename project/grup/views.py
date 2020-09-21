from django.shortcuts import render

# Create your views here.
from .models import Grup

def index(request):
    grups = Grup.objects.all()
    context = {
        'Judul': 'Lihat Grup',
        'Judul_Tabel': 'Tabel Grup',
        'Grups': grups,
    }
    return render(request, 'grup/index.html', context)

def tambah(request):
    context = {
        'Judul': 'Tambah Grup',
        'Subjudul': 'Masukkan Grup Baru',
    }
    return render(request, 'grup/tambah.html', context)