from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View, RedirectView

# Create your views here.
from .models import Templates, Outbox
from kontak.models import Contacts
from grup.models import Grup
from desa.models import Desa
from .forms import TemplateForm, SendForm


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

def sendMessage(request):
    send_form   = SendForm(request.POST or None)
    error       = None
    if request.method == 'POST':
        if send_form.is_valid():
            # get data from SendForm
            group           = send_form.cleaned_data.get('group')
            desa            = send_form.cleaned_data.get('desa')
            name_template   = send_form.cleaned_data.get('template_pesan')

            # get id for each 'grup' and 'desa'
            group_id    = Grup.objects.get(name=group).id
            desa_id     = Desa.objects.get(name=desa).id

            # get message from name template
            template_pesan  = Templates.objects.get(name=name_template).text
            
            # get contact from Contacts
            get_contacts= Contacts.objects.filter(group_id=group_id).filter(desa_id=desa_id).values('contact')
            store = None
            list_outbox = []
            for no_kontak in get_contacts:
                store = Outbox(contact=no_kontak.get('contact'), message=template_pesan)
                list_outbox.append(store)
            
            # save to Outbox
            Outbox.objects.bulk_create(list_outbox)

            return redirect('pesan:index')
        else:
            error = send_form.errors
    context = {
        'Judul'     : 'Kirim Pesan',
        'Subjudul'  : 'Mengirim Pesan Massal',
        'send_form' : send_form,
        'error'     : error
    }
    return render(request, 'pesan/index.html', context)