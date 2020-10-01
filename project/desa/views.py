from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View

# Create your views here.
from .models import Desa
from .forms import DesaForm


class DesaListView(TemplateView):
    template_name   = 'desa/index.html'
    def get_context_data(self, *args, **kwargs):
        desas  = reversed(Desa.objects.all().order_by('id'))
        context = {
            'Judul'         : 'Lihat Desa',
            'Judul_Tabel'   : 'Tabel Desa',
            'Desas'         : desas,
        }
        return context


class DesaFormView(View):
    template_name   = 'desa/tambah.html'
    form    = DesaForm()
    mode    = None
    context = {}

    def get(self, *args, **kwargs):
        self.context = {
            'Judul'     : 'Tambah Desa',
            'Subjudul'  : 'Masukkan Desa Baru',
            'desa_form' : self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        self.form   = DesaForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('desa:index')