from django.db import models

from grup.models import Grup

# Create your models here.

class Templates(models.Model):
    group   = models.ForeignKey(Grup, on_delete=models.SET_NULL, null=True)
    name    = models.CharField(max_length=50)
    text    = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)