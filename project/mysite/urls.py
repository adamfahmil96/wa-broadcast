from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('grup/', include('grup.urls')),
    path('kontak/', include('kontak.urls')),
    path('pesan/', include('pesan.urls')),
    path('admin/', admin.site.urls),
]
