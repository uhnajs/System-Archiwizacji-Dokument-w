# archiwum/admin.py
from django.contrib import admin
from .models import Dokument, HistoriaZmian

admin.site.register(Dokument)
admin.site.register(HistoriaZmian)
