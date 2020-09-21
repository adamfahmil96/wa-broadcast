from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Desa
from .forms import DesaForm

def index(request):
    desas = reversed(Desa.objects.all().order_by('id'))
    context = {
        'Judul': 'Lihat Desa',
        'Judul_Tabel': 'Tabel Desa',
        'Desas': desas,
    }
    return render(request, 'desa/index.html', context)

def tambah(request):
    desa_form = DesaForm()
    context = {
        'Judul': 'Tambah Desa',
        'Subjudul': 'Masukkan Desa Baru',
        'desa_form': desa_form,
    }
    if request.method == 'POST':
        Desa.objects.create(
            name = request.POST.get('name'),
        )
        return HttpResponseRedirect("/desa")
    return render(request, 'desa/tambah.html', context)