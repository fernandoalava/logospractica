# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contacto(models.Model):

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    alumnos = models.ManyToManyField(Alumno)
