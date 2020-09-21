from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tambah', views.tambah, name="tambah"),
]