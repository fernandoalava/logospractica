# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from logoweb.contactos.models import Contacto


def consultar_contactos(request):
    context = {
        "contactos": Contacto.objects.all()
    }
    return render(request, "index.html", context)
