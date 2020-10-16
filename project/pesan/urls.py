from django.urls import path, re_path

from .views import PesanMassalListView, TemplateListView, TemplateFormView, TemplateDeleteView, sendMessageMany

urlpatterns = [
    path('', PesanMassalListView.as_view(), name="index"),
    path('templates/', TemplateListView.as_view(), name="templates"),
    path('templates/tambah/', TemplateFormView.as_view(), name="templates-tambah"),
    path('kirim/massal/', sendMessageMany, name="kirim-massal"),
    re_path(r'^templates/ubah/(?P<ubah_id>[0-9]+)/$', TemplateFormView.as_view(mode='ubah'), name="templates-ubah"),
    re_path(r'^templates/hapus/(?P<hapus_id>[0-9]+)/$', TemplateDeleteView.as_view(), name="templates-hapus"),
]