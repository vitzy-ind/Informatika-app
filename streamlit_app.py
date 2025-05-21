import streamlit as st

st.title("indra")
st.write("halo")

st.image("IMG_20250521_144428.jpg", width=300)
st.write("cats shark")
st.sidebar.image("IMG_20250521_144428.jpg", width=200)
st.header("Genap/Ganjil")

angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"(angka) Genap")
else:
  st.write(f"(angka) Ganjil")
