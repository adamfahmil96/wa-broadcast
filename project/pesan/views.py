from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView

# Create your views here.
from .models import Templates, Outbox
from .forms import TemplateForm


class TemplateListView(TemplateView):
    template_name   = 'pesan/templates.html'

    def get_context_data(self, *args, **kwargs):
        templates   = reversed(Templates.objects.all().order_by('id'))
        context     = {
            'Judul': 'Lihat Templates',
            'Judul_Tabel': 'Tabel Templates',
            'Templates': templates,
        }
        return context


class TemplateFormView(View):
    template_name   = 'pesan/templates-tambah.html'
    form    = TemplateForm()
    mode    = None
    context = {}

    def get(self, *args, **kwargs):
        if self.mode == 'ubah':
            template_ubah   = Templates.objects.get(id=kwargs['ubah_id'])
            data            = template_ubah.__dict__
            self.form       = TemplateForm(initial=data, instance=template_ubah)
        self.context    = {
            'Judul' : 'Tambah Templates',
            'Subjudul'  : 'Masukkan Template Baru',
            'templates_form'    : self.form
        }
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        if kwargs.__contains__('ubah_id'):
            template_ubah   = Templates.objects.get(id=kwargs['ubah_id'])
            self.form       = TemplateForm(self.request.POST, instance=template_ubah)
        else:
            self.form   = TemplateForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('pesan:templates')


class TemplateDeleteView(RedirectView):
    pattern_name    = 'pesan:templates'
    permanent       = False
    query_string    = False

    def get_redirect_url(self, *args, **kwargs):
        hapus_id    = kwargs['hapus_id']
        Templates.objects.filter(id=hapus_id).delete()
        return super().get_redirect_url()


def index(request):
    context = {
        'Judul': 'Kirim Pesan'
    }
    return render(request, 'pesan/index.html', context)