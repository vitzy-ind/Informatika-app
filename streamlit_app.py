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

tab1,tab2,tab3,tab4=st.tabs(['a','b','c','d'])
with tab1:
    st.write('halo')
with tab2:
    st.write('ba')
with tab3:
    st.write('ha')
with tab4:
    st.write('ho')
