# app.py

import streamlit as st
from PIL import Image
from model_utils import load_model, prepare_image, predict
import numpy as np

# Funktion zum Erstellen der Streamlit-Sidebar
def create_sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.header("Einstellungen")

# Hauptfunktion, die die Streamlit-Seite ausführt
def main():
    # Modell laden
    model = load_model("model/v1")


    # Streamlit-Seiteneinstellungen
    st.title('Pflanzenkrankheiten-Klassifikation')
    st.write('Laden Sie ein Bild einer Kartoffelpflanze hoch, um die Krankheit zu diagnostizieren.')

    # Sidebar erstellen
    create_sidebar()

    # Datei-Uploader, um ein Bild hochzuladen
    uploaded_file = st.file_uploader('Bild hochladen', type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Bild anzeigen
        image = Image.open(uploaded_file)
        st.image(image, caption='Hochgeladenes Bild', use_column_width=True)

        # Bild vorbereiten und Modellvorhersage erhalten
        prepared_image = prepare_image(image, (256, 256))
        predicted_class = predict(model, prepared_image)
        confidence = np.max(model.predict(prepared_image)) * 100
        
        # Vorhersage anzeigen
        st.write(f'Vorhersage: {predicted_class}' )
        st.write(f'Wahrscheinlichkeit: {confidence:.2f}%')

if __name__ == "__main__":
    main()