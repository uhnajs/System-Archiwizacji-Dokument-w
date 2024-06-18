# archiwum/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Dokument(models.Model):
    tytul = models.CharField(max_length=200)
    rok = models.PositiveIntegerField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    kategoria = models.CharField(max_length=100)
    miejsce_przechowywania = models.CharField(max_length=200)
    liczba_egz = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tytul} ({self.rok})"

class HistoriaZmian(models.Model):
    dokument = models.ForeignKey(Dokument, on_delete=models.CASCADE, related_name='historia_zmian')
    opis = models.CharField(max_length=200)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zmiana: {self.opis} ({self.data})"
