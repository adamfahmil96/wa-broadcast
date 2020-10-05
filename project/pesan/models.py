from django.db import models

from grup.models import Grup
from .enums import IsEnum, ContentType

# Create your models here.

class Templates(models.Model):
    group   = models.ForeignKey(Grup, on_delete=models.SET_NULL, null=True)
    name    = models.CharField(max_length=50)
    text    = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)


class Outbox(models.Model):
    machine_id      = models.IntegerField(null=True)
    is_group        = models.CharField(
        max_length  = 3,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True
    )
    group_name      = models.CharField(max_length=100, null=True)
    contact         = models.CharField(max_length=50, null=True)
    is_reply        = models.CharField(
        max_length  = 3,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True
    )
    content_type    = models.CharField(
        max_length  = 10,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True
    )
    content_location= models.TextField(null=True)
    message         = models.TextField(null=True)
    sent_at         = models.DateTimeField(null=True)
    processed       = models.CharField(
        max_length  = 3,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True
    )
    processed_at    = models.DateTimeField(null=True)
    created_at      = models.DateTimeField(null=True)
    updated_at      = models.DateTimeField(null=True)
    contact_parser  = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{}".format(self.id)