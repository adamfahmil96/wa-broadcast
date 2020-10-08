from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView

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
        if self.mode == 'ubah':
            grup_ubah   = Grup.objects.get(id=kwargs['ubah_id'])
            data        = grup_ubah.__dict__
            self.form   = GrupForm(initial=data, instance=grup_ubah)
        self.context = {
            'Judul'     : 'Tambah Grup',
            'Subjudul'  : 'Masukkan Grup Baru',
            'grup_form' : self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('ubah_id'):
            grup_ubah   = Grup.objects.get(id=kwargs['ubah_id'])
            self.form   = GrupForm(self.request.POST, instance=grup_ubah)
        else:
            self.form   = GrupForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('grup:index')


class GrupDeleteView(RedirectView):
    pattern_name    = 'grup:index'
    permanent       = False
    query_string    = False

    def get_redirect_url(self, *args, **kwargs):
        hapus_id    = kwargs['hapus_id']
        Grup.objects.filter(id=hapus_id).delete()
        return super().get_redirect_url()