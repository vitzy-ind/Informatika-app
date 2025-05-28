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

    harga_barang = st.number_input("Masukkan Harga Barang:", value=0, step=1000)
    jumlah_barang = st.number_input("Masukkan Jumlah Barang:", value=0, step=1)
    total_harga = hitung_total(harga_barang, jumlah_barang)

    if total_harga > 100000:
        total_harga_diskon = total_harga - 0.05 * total_harga
        st.write(f"Total Harga (dengan diskon): Rp. {total_harga_diskon:,.0f}")
    else:
        st.write(f"Total Harga: Rp. {total_harga:,.0f}")

    bayar = st.number_input("Masukkan Jumlah Uang:", value=0, step=10000)

    if bayar >= total_harga:
        kembalian_uang = bayar - total_harga
        st.write(f"Uang Kembalian: Rp. {kembalian_uang:,.0f}")
    else:
        st.write("Uang yang anda bayarkan kurang ")
