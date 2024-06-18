# archiwum/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Dokument, HistoriaZmian
from .forms import DokumentForm

def lista_dokumentow(request):
    dokumenty = Dokument.objects.all()
    return render(request, 'archiwum/lista_dokumentow.html', {'dokumenty': dokumenty})

@login_required
def dodaj_dokument(request):
    if request.method == "POST":
        form = DokumentForm(request.POST)
        if form.is_valid():
            dokument = form.save()
            HistoriaZmian.objects.create(dokument=dokument, opis="Dokument dodany", uzytkownik=request.user)
            return redirect('lista_dokumentow')
    else:
        form = DokumentForm()
    return render(request, 'archiwum/edytuj_dokument.html', {'form': form})

@login_required
def edytuj_dokument(request, pk):
    dokument = get_object_or_404(Dokument, pk=pk)
    if request.method == "POST":
        form = DokumentForm(request.POST, instance=dokument)
        if form.is_valid():
            form.save()
            HistoriaZmian.objects.create(dokument=dokument, opis="Dokument zmodyfikowany", uzytkownik=request.user)
            return redirect('lista_dokumentow')
    else:
        form = DokumentForm(instance=dokument)
    return render(request, 'archiwum/edytuj_dokument.html', {'form': form})

@login_required
def usun_dokument(request, pk):
    dokument = get_object_or_404(Dokument, pk=pk)
    dokument.delete()
    HistoriaZmian.objects.create(dokument=dokument, opis="Dokument usunięty", uzytkownik=request.user)
    return redirect('lista_dokumentow')

def szukaj_dokumentu(request):
    query = request.GET.get('query')
    if query:
        dokumenty = Dokument.objects.filter(tytul__icontains=query) | Dokument.objects.filter(rok__icontains=query) | Dokument.objects.filter(miejsce_przechowywania__icontains=query)
    else:
        dokumenty = Dokument.objects.all()
    return render(request, 'archiwum/lista_dokumentow.html', {'dokumenty': dokumenty})

def test_base(request):
    return render(request, 'base_generic.html')
