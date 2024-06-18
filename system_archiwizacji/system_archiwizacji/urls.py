# system_archiwizacji/urls.py
from django.contrib import admin
from django.urls import path
from archiwum import views as archiwum_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', archiwum_views.lista_dokumentow, name='lista_dokumentow'),
    path('dokument/nowy/', archiwum_views.dodaj_dokument, name='dodaj_dokument'),
    path('dokument/edytuj/<int:pk>/', archiwum_views.edytuj_dokument, name='edytuj_dokument'),
    path('dokument/usun/<int:pk>/', archiwum_views.usun_dokument, name='usun_dokument'),
    path('szukaj/', archiwum_views.szukaj_dokumentu, name='szukaj_dokumentu'),
    path('login/', archiwum_views.login_view, name='login'),
    path('logout/', archiwum_views.logout_view, name='logout'),
    path('register/', archiwum_views.register, name='register'),
]
