from django.urls import path, re_path

from .views import index, TemplateListView, TemplateFormView

urlpatterns = [
    path('', index, name="index"),
    path('templates/', TemplateListView.as_view(), name="templates"),
    path('templates/tambah/', TemplateFormView.as_view(), name="templates-tambah"),
]