from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View

# Create your views here.
from .models import Templates
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
        self.context    = {
            'Judul' : 'Tambah Templates',
            'Subjudul'  : 'Masukkan Template Baru',
            'templates_form'    : self.form
        }
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        self.form   = TemplateForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()
        return redirect('pesan:templates')

def index(request):
    context = {
        'Judul': 'Kirim Pesan'
    }
    return render(request, 'pesan/index.html', context)