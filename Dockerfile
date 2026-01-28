# Bazowy obraz Python
FROM python:3.11-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj wszystkie pliki projektu do kontenera
COPY . /app

# Zainstaluj wymagania
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
