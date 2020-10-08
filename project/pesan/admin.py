from django.contrib import admin

# Register your models here.
from .models import Templates, Outbox

admin.site.register(Templates)
admin.site.register(Outbox)