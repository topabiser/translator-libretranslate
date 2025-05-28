import streamlit as st
import requests

st.title("Бесплатный переводчик на польский (LibreTranslate)")

def translate_libre(text):
    url = "https://translate.argosopentech.com/translate"
    data = {
        "q": text,
        "source": "auto",
        "target": "pl",
        "format": "text"
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()["translatedText"]
    except Exception as e:
        return f"Ошибка: {e}"

text = st.text_area("Введите текст для перевода:")

if st.button("Перевести"):
    if text.strip():
        translation = translate_libre(text)
        st.subheader("Перевод:")
        st.write(translation)
    else:
        st.warning("Пожалуйста, введите текст.")
