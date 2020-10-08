from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView

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
        if self.mode == 'ubah':
            kontak_ubah = Contacts.objects.get(id=kwargs['ubah_id'])
            data        = kontak_ubah.__dict__
            self.form   = KontakForm(initial=data, instance=kontak_ubah)
        self.context    = {
            'Judul'         : 'Tambah Kontak',
            'Subjudul'      : 'Masukkan Kontak Baru',
            'kontak_form'   : self.form
        }
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        if kwargs.__contains__('ubah_id'):
            kontak_ubah = Contacts.objects.get(id=kwargs['ubah_id'])
            self.form   = KontakForm(self.request.POST, instance=kontak_ubah)
        else:
            self.form   = KontakForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('kontak:index')


class KontakDeleteView(RedirectView):
    pattern_name    = 'kontak:index'
    permanent       = False
    query_string    = False

    def get_redirect_url(self, *args, **kwargs):
        hapus_id    = kwargs['hapus_id']
        Contacts.objects.filter(id=hapus_id).delete()
        return super().get_redirect_url()