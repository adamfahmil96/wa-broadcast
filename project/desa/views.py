from django.shortcuts import render

# Create your views here.
from .models import Desa

def index(request):
    desas = Desa.objects.all()
    context = {
        'Judul': 'Lihat Desa',
        'Judul_Tabel': 'Tabel Desa',
        'Desas': desas,
    }
    return render(request, 'desa/index.html', context)