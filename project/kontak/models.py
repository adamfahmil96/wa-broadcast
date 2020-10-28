from django.db import models
from django.db.models import Q

from grup.models import Grup
from desa.models import Desa


class KontakQuerySet(models.QuerySet):
    def search(self, query=None):
        qs  = self
        if (query is not None):
            or_lookup   = (Q(name__icontains=query) | Q(contact__icontains=query))
            qs          = qs.filter(or_lookup).distinct()
        return qs


class KontakManager(models.Manager):
    def get_queryset(self):
        return KontakQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)


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
    
    class Meta:
        db_table    = "contacts"
    
    objects     = KontakManager()