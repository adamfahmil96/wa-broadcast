# Generated by Django 3.1.1 on 2020-10-13 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pesan', '0005_auto_20201012_1259'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='outbox',
            table='outbox',
        ),
        migrations.AlterModelTable(
            name='templates',
            table='templates',
        ),
    ]