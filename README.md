### Student Grade Prediction 🎓

Projekt przewidywania ocen uczniów oparty na regresji logistycznej. 
Aplikacja zbudowana w Pythonie z użyciem Streamlit i FastAPI, 
danych SQLite oraz Docker.

### Technologie
- Python 3.11
- Streamlit
- FastAPI
- SQLite
- scikit-learn (regresja logistyczna)
- Docker & docker-compose

### Funkcjonalności
- Przewidywanie ocen uczniów
- Zapisywanie predykcji w bazie danych SQLite
- Przegląd historii poprzednich predykcji
- Czyszczenie bazy danych
- Całość uruchamiana w Dockerze dla prostoty

### Uruchomienie projektu

### W terminalu
1. Sklonuj repozytorium
```bash
git clone https://github.com/joannakowalska2507/GradesPredicted.git
```
```bash
cd GradesPredicted
```
2. Uruchom Docker Compose
```bash
docker compose up --build
 ```
