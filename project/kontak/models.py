from django.db import models

from grup.models import Grup
from desa.models import Desa

# Create your models here.
class Contacts(models.Model):
    norm        = models.CharField(max_length=50, null=True, blank=True)
    name        = models.CharField(max_length=50)
    contact     = models.CharField(max_length=50)
    group       = models.ForeignKey(Grup, on_delete=models.SET_NULL, null=True)
    desa        = models.ForeignKey(Desa, on_delete=models.SET_NULL, null=True, blank=True)
    is_active   = models.IntegerField(default=1)
    is_tester   = models.IntegerField(default=0)

    def __str__(self):
        return "{}. {} - {}".format(self.id, self.name, self.contact)