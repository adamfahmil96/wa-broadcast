from django.urls import path, re_path

from .views import DesaListView, DesaFormView, DesaDeleteView

urlpatterns = [
    path('', DesaListView.as_view(), name="index"),
    path('tambah', DesaFormView.as_view(), name="tambah"),
    re_path(r'^ubah/(?P<ubah_id>[0-9]+)/$', DesaFormView.as_view(mode='ubah'), name="ubah"),
    re_path(r'^hapus/(?P<hapus_id>[0-9]+)/$', DesaDeleteView.as_view(), name="hapus"),
]