# Generated by Django 3.1.2 on 2020-12-21 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orla', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orla',
            options={'ordering': ('apellidos',)},
        ),
    ]
