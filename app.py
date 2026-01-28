import pandas as pd
import streamlit as st
import requests

st.set_page_config(
    page_title="Predykcja ocen",
    layout="wide",
    initial_sidebar_state="auto"
)


with st.sidebar:
    zakladka = st.radio("## Menu",
        ["Predykcja oceny", "Poprzednie predykcje", "Opis projektu"]
    )

if zakladka == "Predykcja oceny":
    st.markdown(
        "<h3 style='text-align: center;'>Predykcja oceny ucznia</h3>",
        unsafe_allow_html=True
    )
    st.markdown("#### Ustaw interesujące cię dane")


    math=st.slider("Wynik z matematyki",0,100,50)
    reading=st.slider("Ocena czytania",0,100,50)
    writing=st.slider("Ocena pisania",0,100,50)
    attendance=st.slider("Frekfencja",0,100,50)
    homework=st.slider("Procent wykonanych prac domowych",0,100,50)


    if st.button("Przewiduj"):

        payload = {"feature1": math, "feature2": reading, "feature3": writing, "feature4": attendance, "feature5": homework}
        try:
            response = requests.post("http://api:8000/predict", json=payload)
            if response.status_code == 200:
                result = response.json()
                if result['prediction'] == "Niedostateczny":
                    st.error(f"Przewidywana ocena: {result['prediction']}")
                else:
                    st.success(f"Przewidywana ocena: {result['prediction']}")
            else:
                st.error("Błąd połączenia z API")
        except:
            st.error("Nie udało się połączyć z FastAPI. Sprawdź czy serwer działa.")

elif zakladka=="Poprzednie predykcje":
    st.session_state.cleared = False
    API_URL = "http://api:8000/predictions"
    st.markdown(
        "<h3 style='text-align: center;'>Poprzednie predykcje</h3>",
        unsafe_allow_html=True
    )
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        if data:
            if st.button("🧹 Wyczyść bazę danych"):
                r = requests.delete("http://api:8000/predictions")
                st.success("Baza wyczyszczona")
                st.session_state.data = []  # natychmiast usuwa dane z widoku
                st.session_state.cleared = True

            if not st.session_state.cleared:
                df = pd.DataFrame(data)
                df.index = df.index + 1
                st.dataframe(df[['math', 'reading', 'writing', 'attendance', 'homework', 'grade']])
        else:
            st.markdown('Brak danych w bazie')
    else:
        st.error("Nie udało się pobrać danych z API")

elif zakladka=="Opis projektu":
    st.markdown(
        "<h3 style='text-align: center;'> System Predykcji Ocen Uczniów</h3>",
        unsafe_allow_html=True
    )
    st.markdown("""<div style="font-size:20px">Celem projektu było stworzenie interaktywnego systemu do przewidywania ocen uczniów na podstawie danych edukacyjnych, z użyciem regresji logistycznej.
            Projekt demonstruje cały proces: od przygotowania danych, przez budowę i trenowanie modelu, aż po integrację z interaktywnym frontendem w Streamlit oraz bazą danych SQLite</div> """,unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("""<div style="font-size:20px">Dane użyte w projekcie są sztucznie wygenerowane, symulujące typowe informacje edukacyjne, np. wyniki z testów, frekwencję, zadania domowe. Dane w trakcie ich generowania zostały celowo zanieczyszczone (braki wartości, błędy, nieprawidłowe formaty), aby zasymulować realistyczne scenariusze pracy z danymi.
            Przed treningiem modelu dane zostały oczyszczane oraz odpowiednio przygotowane przygotowywane.</div>""",unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown("""<div style="font-size:20px"> Zastosowany model to <b>regresja logistyczna</b>, która przewiduje prawdopodobieństwo uzyskania określonej oceny przez ucznia. </div>""", unsafe_allow_html=True )
    st.markdown(" ")
    st.markdown("""<div style="font-size:20px"><b>Architektura systemu</b>: 
    <br>Backend:
    <br><b>FastAPI</b> obsługuje komunikację między frontendem a bazą danych.
    <br><b>SQLite</b> jako baza danych przechowuje wszystkie poprzednie predykcje uczniów.
    <br><b>API</b> udostępnia endpointy do:
    <br>-pobierania listy poprzednich predykcji
    <br>-dodawania nowej predykcji 
    <br>-usuwania wszystkich zapisanych predykcji 
    <br>Frontend:
    <br><b>Streamlit</b> umożliwia interaktywną pracę użytkownika:</div>""",unsafe_allow_html=True )