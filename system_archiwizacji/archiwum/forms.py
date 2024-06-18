# archiwum/forms.py
from django import forms
from .models import Dokument

class DokumentForm(forms.ModelForm):
    class Meta:
        model = Dokument
        fields = ['tytul', 'rok', 'kategoria', 'miejsce_przechowywania', 'liczba_egz']
