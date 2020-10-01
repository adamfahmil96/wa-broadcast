from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View

# Create your views here.
from .models import Grup
from .forms import GrupForm


class GrupListView(TemplateView):
    template_name   = 'grup/index.html'
    
    def get_context_data(self, *args, **kwargs):
        grups = reversed(Grup.objects.all().order_by('id'))
        context = {
            'Judul': 'Lihat Grup',
            'Judul_Tabel': 'Tabel Grup',
            'Grups': grups,
        }
        return context


class GrupFormView(View):
    template_name   = 'grup/tambah.html'
    form    = GrupForm()
    mode    = None
    context = {}

    def get(self, *args, **kwargs):
        self.context = {
            'Judul'     : 'Tambah Grup',
            'Subjudul'  : 'Masukkan Grup Baru',
            'grup_form' : self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        self.form   = GrupForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('grup:index')