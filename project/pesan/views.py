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


class PesanMassalListView(TemplateView):
    template_name   = 'pesan/index.html'

    def get_context_data(self, *args, **kwargs):
        # get name of template
        name_template   = Templates.objects.all().values('name').distinct()
        
        # count sent_at based on name_template
        list_template   = []
        for name in name_template:
            name            = name.get('name')
            count_outbox    = Outbox.objects.filter(title_message=name).filter(created_at__isnull=False).filter(sent_at__isnull=False).count()
            each_list       = [name, count_outbox]
            list_template.append(each_list)
        context     = {
            'Judul': 'Lihat Pengiriman Pesan Massal',
            'Judul_Tabel': 'Tabel Pengiriman Pesan Massal',
            'list_template': list_template,
        }
        return context


def sendMessageMany(request):
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
            if desa is not None:
                desa_id     = Desa.objects.get(name=desa).id

            # get message from name template
            template_pesan  = Templates.objects.get(name=name_template).text
            
            # get contact from Contacts
            store = None
            list_outbox = []
            if desa is not None:
                get_contacts= Contacts.objects.filter(group_id=group_id).filter(desa_id=desa_id).values('contact')
                for no_kontak in get_contacts:
                    store = Outbox(contact=no_kontak.get('contact'), message=template_pesan, grup_name=group, desa_name=desa, title_message=name_template)
                    list_outbox.append(store)
            else:
                get_contacts= Contacts.objects.filter(group_id=group_id).values('contact')
                for no_kontak in get_contacts:
                    store = Outbox(contact=no_kontak.get('contact'), message=template_pesan, grup_name=group, title_message=name_template)
                    list_outbox.append(store)
            
            # save to Outbox
            Outbox.objects.bulk_create(list_outbox)

            return redirect('pesan:index')
        else:
            error = send_form.errors
    context = {
        'Judul'     : 'Kirim Pesan Massal',
        'Subjudul'  : 'Mengirim Pesan Massal',
        'send_form' : send_form,
        'error'     : error
    }
    return render(request, 'pesan/kirim-massal.html', context)