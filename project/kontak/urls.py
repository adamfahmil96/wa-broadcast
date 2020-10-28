from django.urls import path, re_path

from .views import KontakListView, KontakCariListView, KontakFormView, KontakDeleteView

urlpatterns = [
    path('', KontakListView.as_view(), name="index"),
    path('cari/', KontakCariListView.as_view(), name="cari"),
    path('tambah/', KontakFormView.as_view(), name="tambah"),
    re_path(r'^ubah/(?P<ubah_id>[0-9]+)/$', KontakFormView.as_view(mode='ubah'), name="ubah"),
    re_path(r'^hapus/(?P<hapus_id>[0-9]+)/$', KontakDeleteView.as_view(), name="hapus"),
]