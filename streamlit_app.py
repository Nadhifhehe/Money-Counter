import streamlit as st
st.set_page_config(layout="centered")
# ---------- CONFIG ----------
st.set_page_config(
    page_title="Money Tracker",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .header {
            background-color: #7CDB5A;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        .saldo-card {
            background-color: #7CDB5A;
            padding: 25px;
            border-radius: 20px;
            color: white;
            margin-top: 20px;
        }
        .saldo-text {
            font-size: 18px;
        }
        .saldo-nominal {
            font-size: 36px;
            font-weight: bold;
        }
        .btn-box {
            display: flex;
            gap: 20px;
            margin-top: 20px;
        }
        .card {
            border-radius: 20px;
            padding: 20px;
        }
        .gray {
            background-color: #cccccc;
        }
        .red {
            background-color: #d85c5c;
        }
        .wishlist {
            background-color: #e7c3a1;
            text-align: center;
            margin-top: 20px;
            border-radius: 20px;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="header">Money Tracker ☰</div>', unsafe_allow_html=True)

# ---------- SALDO ----------
st.markdown("""
<div class="saldo-card">
    <div class="saldo-text">Saldo Sekarang:</div>
    <div class="saldo-nominal">Rp. XXX.XXX.XXX</div>
</div>
""", unsafe_allow_html=True)

# ---------- BUTTONS ----------
st.markdown("""
<div class="btn-box">
    <div style="background:#7CDB5A; padding:10px 30px; border-radius:12px; color:white; font-weight:bold;">
        Pemasukan
    </div>
    <div style="background:#7CDB5A; padding:10px 30px; border-radius:12px; color:white; font-weight:bold;">
        Pengeluaran
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- GRID LAYOUT ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card gray" style="height:200px;">🌀 Grafik (Dummy)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="wishlist">
        <h3>Wanted</h3>
        <div style="height:120px; background:#fff; border-radius:10px; margin:10px;"></div>
        <h3>Rp. XXXXX</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card red" style="height:380px;">📋 Riwayat Transaksi</div>', unsafe_allow_html=True)
