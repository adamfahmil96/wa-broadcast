from django.db import models

from grup.models import Grup
from .enums import IsEnum, ContentType

# Create your models here.

class Templates(models.Model):
    group   = models.ForeignKey(Grup, on_delete=models.SET_NULL, null=True)
    name    = models.CharField(max_length=50)
    text    = models.TextField()

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        db_table    = "templates"


class Outbox(models.Model):
    machine_id      = models.IntegerField(null=True, default=1)
    is_group        = models.CharField(
        max_length  = 3,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True,
        default     = 'N'
    )
    group_name      = models.CharField(max_length=100, null=True)
    desa_name       = models.CharField(max_length=50, null=True)
    grup_name       = models.CharField(max_length=50, null=True)
    contact         = models.CharField(max_length=50, null=True)
    is_reply        = models.CharField(
        max_length  = 3,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True,
        default     = 'N'
    )
    content_type    = models.CharField(
        max_length  = 10,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True,
        default     = 'Text'
    )
    content_location= models.TextField(null=True)
    title_message   = models.CharField(max_length=50, null=True)
    message         = models.TextField(null=True)
    sent_at         = models.DateTimeField(null=True)
    processed       = models.CharField(
        max_length  = 3,
        choices     = [(tag, tag.value) for tag in IsEnum],
        null        = True,
        default     = 'N'
    )
    processed_at    = models.DateTimeField(null=True)
    created_at      = models.DateTimeField(null=True, auto_now_add=True)
    updated_at      = models.DateTimeField(null=True, auto_now_add=True)
    contact_parser  = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{}".format(self.id)
    
    class Meta:
        db_table    = "outbox"