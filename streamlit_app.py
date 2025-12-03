import streamlit as st

kiri, kanan = st.columns([1, 1], gap="large")

with kiri:
    st.markdown("### Grafik")
    st.markdown("### Wanted")

with kanan:
    st.markdown("### Riwayat Transaksi")
