# System Archiwizacji Dokumentów

## Opis

System Archiwizacji Dokumentów to aplikacja webowa umożliwiająca zarządzanie dokumentami, ich katalogowanie oraz śledzenie stanu i historii zmian. Projekt został zrealizowany z wykorzystaniem frameworka Django.

## Funkcje

- **Autoryzacja użytkowników**: Rejestracja, logowanie i wylogowywanie użytkowników.
- **Zarządzanie dokumentami**: Dodawanie, edytowanie, usuwanie i wyszukiwanie dokumentów.
- **Historia dokumentów**: Śledzenie zmian dokumentów, wypożyczeń i zwrotów.
- **Stylizacja**: Użycie Bootstrap do stylizacji formularzy i przycisków.

## Instalacja

1. Sklonuj repozytorium:

    ```bash
    git clone https://github.com/TwojeUzytkownik/System-Archiwizacji-Dokumentow.git
    cd System-Archiwizacji-Dokumentow
    ```

2. Utwórz i aktywuj wirtualne środowisko:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # na Windows: .venv\Scripts\activate
    ```

3. Zainstaluj wymagane pakiety:

    ```bash
    pip install -r requirements.txt
    ```

4. Wykonaj migracje bazy danych:

    ```bash
    python manage.py migrate
    ```

5. Uruchom serwer deweloperski:

    ```bash
    python manage.py runserver
    ```

6. Otwórz przeglądarkę i przejdź do `http://127.0.0.1:8000/`.

## Użycie

1. **Rejestracja**: Użytkownicy mogą się zarejestrować, klikając na link "Zarejestruj się" na stronie głównej.
2. **Logowanie**: Zalogowani użytkownicy mogą zarządzać dokumentami.
3. **Dodawanie dokumentów**: Po zalogowaniu użytkownik może dodawać nowe dokumenty, klikając na link "Dodaj Dokument".
4. **Edytowanie i usuwanie dokumentów**: Dokumenty mogą być edytowane lub usuwane z listy dokumentów.
5. **Historia dokumentów**: Historia zmian, wypożyczeń i zwrotów dokumentów jest dostępna dla każdego dokumentu.
6. **Wyszukiwanie**: Użytkownicy mogą wyszukiwać dokumenty według tytułu, roku lub miejsca przechowywania.
