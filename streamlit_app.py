import streamlit as st
st.set_page_config(layout="centered")
st.title ("Money Tracker")
if st.button("➡️ Ke Halaman Pemasukan"):
    st.switch_page("pages/pemasukan.py")
    
if st.button("➡️ Ke Halaman Pengeluaran"):
    st.switch_page("pages/pengeluaran.py")
