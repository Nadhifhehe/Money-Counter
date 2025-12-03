import streamlit as st

# ---------------- INIT PAGE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME ----------------
if st.session_state.page == "home":
    st.title("Money Tracker")

    st.write("")

    # ✅ TOMBOL KIRI & KANAN (SEJAJAR & SIMETRIS)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Pemasukan", use_container_width=True):
            st.session_state.page = "pemasukan"

    with col2:
        if st.button("➖ Pengeluaran", use_container_width=True):
            st.session_state.page = "pengeluaran"

# ---------------- PEMASUKAN ----------------
elif st.session_state.page == "pemasukan":
    st.title("Halaman Pemasukan")

    jumlah = st.number_input("Masukkan jumlah uang", 0)

    if st.button("Simpan"):
        st.success("✅ Pemasukan disimpan!")

    st.write("")

    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"

# ---------------- PENGELUARAN ----------------
elif st.session_state.page == "pengeluaran":
    st.title("Halaman Pengeluaran")

    jumlah = st.number_input("Masukkan jumlah pengeluaran", 0)

    if st.button("Simpan"):
        st.success("✅ Pengeluaran disimpan!")

    st.write("")

    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"
