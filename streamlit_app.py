import streamlit as st

# ---------------- HOME ----------------
if st.session_state.page == "home":
    st.title("Money Tracker")

if "page" not in st.session_state:
    st.session_state.page = "home"
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Pemasukan"):
        st.session_state.page = "pemasukan"

with col2:
    if st.button("➖ Pengeluaran"):
        st.session_state.page = "pengeluaran"   
