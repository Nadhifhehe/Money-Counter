import streamlit as st

import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME ----------------
if st.session_state.page == "home":
    st.title("Money Tracker")

    col1, col2 = st.columns(2)

with col1:
    if st.button("➡️ Ke Halaman Pemasukan"):
        st.session_state.page = "pemasukan"

with col2:
    if st.button("➡️ Ke Halaman Pengeluaran"):
        st.session_state.page = "pengeluaran"

# ---------------- PEMASUKAN ----------------
elif st.session_state.page == "pemasukan":
    st.title("Halaman Pemasukan")

    jumlah = st.number_input("Masukkan jumlah uang", 0)

    if st.button("Simpan"):
        st.success("Pemasukan disimpan!")

    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"

# ---------------- PENGELUARAN ----------------
elif st.session_state.page == "pengeluaran":
    st.title("Halaman Pengeluaran")

    jumlah = st.number_input("Masukkan jumlah pengeluaran", 0)

    if st.button("Simpan"):
        st.success("Pengeluaran disimpan!")

    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"
