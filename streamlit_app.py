import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.write("Ini di kiri")

with col2:
    st.write("Ini di kanan")
