# System Archiwizacji Dokumentów

Ten projekt jest systemem archiwizacji dokumentów opartym na Django. Umożliwia dodawanie, edytowanie, usuwanie i przeglądanie dokumentów oraz wyszukiwanie ich według różnych kryteriów. System śledzi również historię zmian dokumentów.

## Wymagania

- Python 3.x
- Django 3.x lub nowszy

## Instalacja

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/twoje-repozytorium/system-archiwizacji-dokumentow.git
    cd system-archiwizacji-dokumentow
    ```

2. Utwórz wirtualne środowisko i zainstaluj wymagania:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Na Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Wykonaj migracje:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Uruchom serwer deweloperski:
    ```bash
    python manage.py runserver
    ```

5. Otwórz przeglądarkę i przejdź do `http://127.0.0.1:8000`, aby zobaczyć działający system.


