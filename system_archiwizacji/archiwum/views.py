# archiwum/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Dokument, HistoriaZmian
from .forms import DokumentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# archiwum/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('lista_dokumentow')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('lista_dokumentow')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def lista_dokumentow(request):
    dokumenty = Dokument.objects.all()
    return render(request, 'lista_dokumentow.html', {'dokumenty': dokumenty})


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
    return render(request, 'dodaj_dokument.html', {'form': form})


# archiwum/views.py
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
    return render(request, 'edytuj_dokument.html', {'form': form})


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
    return render(request, 'lista_dokumentow.html', {'dokumenty': dokumenty})

def test_base(request):
    return render(request, 'base_generic.html')
