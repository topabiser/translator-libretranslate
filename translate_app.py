import streamlit as st
import requests

st.title("Бесплатный переводчик на польский (LibreTranslate)")

def translate_libre(text):
    url = "https://translate.astian.org/translate"
    data = {
        "q": text,
        "source": "auto",
        "target": "pl",
        "format": "text"
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        return response.json()["translatedText"]
    except requests.exceptions.Timeout:
        return "Ошибка: сервер перевода не ответил (тайм-аут). Попробуйте позже."
    except requests.exceptions.RequestException as e:
        return f"Ошибка при подключении: {e}"

text = st.text_area("Введите текст для перевода:")

if st.button("Перевести"):
    if text.strip():
        with st.spinner("Перевожу..."):
            translation = translate_libre(text)
        st.subheader("Перевод:")
        st.write(translation)
    else:
        st.warning("Пожалуйста, введите текст.")
