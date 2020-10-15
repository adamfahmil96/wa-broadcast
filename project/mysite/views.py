from django.shortcuts import render
from django.views.generic.base import TemplateView

# import models
from kontak.models import Contacts
from pesan.models import Templates
from grup.models import Grup
from desa.models import Desa


class DashboardListView(TemplateView):
    template_name   = 'index.html'

    def get_context_data(self, *args, **kwargs):
        kontaks     = Contacts.objects.all()
        templates   = Templates.objects.all()
        grups       = Grup.objects.all()
        desas       = Desa.objects.all()
        
        list_data = [
            ['danger', 'Jumlah Kontak', str(kontaks.count()) + ' kontak', 'fa-phone'],
            ['primary', 'Jumlah Template Pesan', str(templates.count()) + ' template', 'fa-inbox'],
            ['warning', 'Jumlah Grup', str(grups.count()) + ' grup', 'fa-users'],
            ['info', 'Jumlah Desa', str(grups.count()) + ' desa', 'fa-flag'],
        ]

        context = {
            'list_data' : list_data,
        }

        return context

def index(request):
    return render(request, 'index.html')