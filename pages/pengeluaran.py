import streamlit as st

st.title("Halaman Pengeluaran")

jumlah = st.number_input("Masukkan jumlah pengeluaran:", 0)

if st.button("Simpan"):
    st.error("Pengeluaran disimpan!")

if st.button("⬅️ Kembali"):
    st.switch_page("streamlit_app.py")
