import streamlit as st

# Judul aplikasi
st.title("Hello Streamlit!")

# Teks biasa
st.write("Ini adalah aplikasi Streamlit pertamaku 😄")

# Input sederhana
name = st.text_input("Siapa namamu?")
if name:
    st.write(f"Halo, {name}!")

# Slider contoh
age = st.slider("Umurmu berapa?", 0, 100, 25)
st.write(f"Kamu berumur {age} tahun")
