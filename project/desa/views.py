from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView

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
        if self.mode == 'ubah':
            desa_ubah   = Desa.objects.get(id=kwargs['ubah_id'])
            data        = desa_ubah.__dict__
            self.form   = DesaForm(initial=data, instance=desa_ubah)
        self.context = {
            'Judul'     : 'Tambah Desa',
            'Subjudul'  : 'Masukkan Desa Baru',
            'desa_form' : self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('ubah_id'):
            desa_ubah   = Desa.objects.get(id=kwargs['ubah_id'])
            self.form   = DesaForm(self.request.POST, instance=desa_ubah)
        else:
            self.form   = DesaForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('desa:index')


class DesaDeleteView(RedirectView):
    pattern_name    = 'desa:index'
    permanent       = False
    query_string    = False

    def get_redirect_url(self, *args, **kwargs):
        hapus_id    = kwargs['hapus_id']
        Desa.objects.filter(id=hapus_id).delete()
        return super().get_redirect_url()