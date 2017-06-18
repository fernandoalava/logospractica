# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from logoweb.contactos.models import Contacto, Alumno, Materia


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ['nombre']


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    pass
