from django.urls import path, re_path

from .views import GrupListView, GrupFormView, GrupDeleteView

urlpatterns = [
    path('', GrupListView.as_view(), name="index"),
    path('tambah/', GrupFormView.as_view(), name="tambah"),
    re_path(r'^ubah/(?P<ubah_id>[0-9]+)/$', GrupFormView.as_view(mode='ubah'), name="ubah"),
    re_path(r'^hapus/(?P<hapus_id>[0-9]+)/$', GrupDeleteView.as_view(), name="hapus"),
]