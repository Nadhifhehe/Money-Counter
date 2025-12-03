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

