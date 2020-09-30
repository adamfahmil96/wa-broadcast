from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

# Create your views here.
from .models import Desa
from .forms import DesaForm

class DesaListView(TemplateView):
    template_name   = ''

def index(request):
    desas = reversed(Desa.objects.all().order_by('id'))
    context = {
        'Judul': 'Lihat Desa',
        'Judul_Tabel': 'Tabel Desa',
        'Desas': desas,
    }
    return render(request, 'desa/index.html', context)

def tambah(request):
    desa_form = DesaForm(request.POST or None)
    error = None
    valid = False
    context = {
        'Judul': 'Tambah Desa',
        'Subjudul': 'Masukkan Desa Baru',
        'desa_form': desa_form,
        'error': error,
    }
    if request.method == 'POST':
        if desa_form.is_valid():
            desa_form.save()
            return redirect('desa:index')
        else:
            error = desa_form.errors
            context['error'] = error
    return render(request, 'desa/tambah.html', context)