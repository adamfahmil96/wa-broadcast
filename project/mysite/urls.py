from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('desa/', include(('desa.urls', 'desa'), namespace="desa")),
    path('grup/', include(('grup.urls', 'grup'), namespace="grup")),
    path('kontak/', include(('kontak.urls', 'kontak'), namespace="kontak")),
    path('pesan/', include(('pesan.urls', 'pesan'), namespace="pesan")),
    path('admin/', admin.site.urls),
]
