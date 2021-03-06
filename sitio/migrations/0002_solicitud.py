# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-03 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=254)),
                ('servicio', models.CharField(choices=[('Servicio 1', 'Servicio1'), ('Servicio 2', 'Servicio2'), ('Servicio 3', 'Servicio3'), ('Servicio 4', 'Servicio4')], default='Servicio1', max_length=9)),
                ('descripcion', models.CharField(max_length=550, verbose_name='Descripción')),
            ],
        ),
    ]
