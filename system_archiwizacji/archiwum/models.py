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
    dokument = models.ForeignKey(Dokument, on_delete=models.CASCADE)
    opis = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    wypozyczony = models.BooleanField(default=False)
    data_wypozyczenia = models.DateTimeField(null=True, blank=True)
    data_zwrotu = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.dokument.tytul} - {self.opis} - {self.data}"