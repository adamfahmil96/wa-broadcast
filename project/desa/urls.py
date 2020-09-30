from django.urls import path, re_path

from .views import DesaListView, DesaFormView

urlpatterns = [
    path('', DesaListView.as_view(), name="index"),
    path('tambah', DesaFormView.as_view(), name="tambah"),
]