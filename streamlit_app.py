import streamlit as st

st.title("indra")
st.write("halo")

st.image("IMG_20250521_144428.jpg", width=300)
st.write("cats shark")
st.sidebar.image("IMG_20250521_144428.jpg", width=200)
st.header("Genap/Ganjil")

angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"Genap")
else:
  st.write(f"Ganjil")

st.sidebar.write("gtwsih")

st.title("Aplikasi Sederhana")

# Menggunakan layout kolom
col1, col2 = st.columns(2)

with col1:
    st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
    angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

    if (angka % 2) == 0:
        st.write(f"{angka} adalah Bilangan Genap")
    else:
        st.write(f"{angka} adalah Bilangan Ganjil")

with col2:
    st.header("Aplikasi menghitung Total Belanja")

    def hitung_total(harga, jumlah):
        return harga * jumlah
