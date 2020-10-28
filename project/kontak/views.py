from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView
from django.views.generic import ListView

# Create your views here.
from .models import Contacts
from .forms import KontakForm


class KontakListView(ListView):
    model       = Contacts
    ordering    = ['-id']
    paginate_by = 5
    extra_context   = {
        'Judul'         : 'Lihat Kontak',
        'Judul_Tabel'   : 'Tabel Kontak',
        'Total_Kontak'  : Contacts.objects.all().count(),
    }
    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs  = self.kwargs
        return super().get_context_data(*args, **kwargs)


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

class KontakCariListView(ListView):
    model           = Contacts
    template_name   = 'kontak/cari_list.html'
    ordering        = ['id']
    count           = 0
    extra_context   = {
        'Judul'         : 'Cari Kontak',
    }
    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs              = self.kwargs
        context             = super().get_context_data(*args, **kwargs)
        context['count']    = self.count or 0
        context['query']    = self.request.GET.get('q')
        return context
    
    def get_queryset(self):
        request = self.request
        query   = request.GET.get('q', None)
        if query is not None:
            kontak_results  = Contacts.objects.search(query)
            qs              = sorted(kontak_results, key=lambda instance: instance.pk, reverse=True)
            self.count      = len(qs)
            print(qs)
            return qs
        return Contacts.objects.none()