# system_archiwizacji/urls.py
from django.contrib import admin
from django.urls import path
from archiwum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_dokumentow, name='lista_dokumentow'),
    path('dokument/nowy/', views.dodaj_dokument, name='dodaj_dokument'),
    path('dokument/edytuj/<int:pk>/', views.edytuj_dokument, name='edytuj_dokument'),
    path('dokument/usun/<int:pk>/', views.usun_dokument, name='usun_dokument'),
    path('szukaj/', views.szukaj_dokumentu, name='szukaj_dokumentu'),
    path('test_base/', views.test_base, name='test_base'),
]
