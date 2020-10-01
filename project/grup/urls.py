from django.urls import path, re_path

from .views import GrupListView, GrupFormView

urlpatterns = [
    path('', GrupListView.as_view(), name="index"),
    path('tambah', GrupFormView.as_view(), name="tambah"),
]