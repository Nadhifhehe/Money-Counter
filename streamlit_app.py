import streamlit as st
st.set_page_config(layout="centered")

kiri, kanan = st.columns([1, 1], gap="large")

with kiri:
    st.markdown("### Grafik")
    st.markdown("### Wanted")

with kanan:
    st.markdown("### Riwayat Transaksi")
st.markdown("""
<style>
.box {
    background-color: #ddd;
    border-radius: 16px;
    padding: 20px;
    height: 300px;
}
</style>
""", unsafe_allow_html=True)
with kiri:
    st.markdown('<div class="box">Grafik</div>', unsafe_allow_html=True)

with kanan:
    st.markdown('<div class="box">Riwayat</div>', unsafe_allow_html=True)
