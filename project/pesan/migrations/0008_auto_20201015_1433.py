# Generated by Django 3.1.1 on 2020-10-15 07:33

from django.db import migrations, models
import pesan.enums


class Migration(migrations.Migration):

    dependencies = [
        ('pesan', '0007_auto_20201015_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='outbox',
            name='grup_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='outbox',
            name='is_group',
            field=models.CharField(choices=[(pesan.enums.IsEnum['Y'], 'Y'), (pesan.enums.IsEnum['N'], 'N')], default='N', max_length=3, null=True),
        ),
    ]