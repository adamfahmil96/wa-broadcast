from django.db import models

# Create your models here.
class Desa(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        db_table    = "desa"