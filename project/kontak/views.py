from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View

# Create your views here.
from .models import Contacts
from .forms import KontakForm


class KontakListView(TemplateView):
    template_name   = 'kontak/index.html'

    def get_context_data(self, *args, **kwargs):
        kontaks = reversed(Contacts.objects.all().order_by('id'))
        context = {
            'Judul'         : 'Lihat Kontak',
            'Judul_Tabel'   : 'Tabel Kontak',
            'Kontaks'       : kontaks,
        }
        return context


class KontakFormView(View):
    template_name   = 'kontak/tambah.html'
    form    = KontakForm()
    mode    = None
    context = {}

    def get(self, *args, **kwargs):
        self.context    = {
            'Judul'         : 'Tambah Kontak',
            'Subjudul'      : 'Masukkan Kontak Baru',
            'kontak_form'   : self.form
        }
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        self.form   = KontakForm(self.request.POST)
        if self.form.is_valid():
            Contacts.objects.create(
                norm        = self.form.cleaned_data.get('norm'),
                name        = self.form.cleaned_data.get('name'),
                contact     = self.form.cleaned_data.get('contact'),
                group       = self.form.cleaned_data.get('group'),
                is_active   = 1,
                is_tester   = 0,
            )
        return redirect('kontak:index')