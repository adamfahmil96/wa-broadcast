from django.urls import path, re_path

from .views import KontakListView, KontakFormView

urlpatterns = [
    path('', KontakListView.as_view(), name="index"),
    path('tambah/', KontakFormView.as_view(), name="tambah"),
]