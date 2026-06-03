import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard - ActuWise", layout="wide")

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #F8F3F0 !important; }
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #EFEAE6; }
    div[data-testid="stMetricValue"] { font-size: 2rem !important; font-weight: 700 !important; color: #ECA696; }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("<h2 style='color: #ECA696; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>", unsafe_allow_html=True)
for _ in range(16): st.sidebar.write("")
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>### Aulia", unsafe_allow_html=True)

# Judul Dashboard
st.title("Financial & Actuarial Dashboard")
st.markdown("Ringkasan eksekutif dan indikator performa utama portofolio manajemen risiko.")
st.markdown("<br>", unsafe_allow_html=True)

# Layout Metrik
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Total Premium Written", value="Rp 4.25 M", delta="+14.2%")
m2.metric(label="Annuity Payout Exposure", value="Rp 1.82 M", delta="-2.1%")
m3.metric(label="Average Reserve Fund", value="Rp 520 Juta", delta="+5.8%")
m4.metric(label="Active Insured Lives", value="12,450", delta="+8.3%")

st.markdown("<br><hr style='border-color:#EFEAE6;'><br>", unsafe_allow_html=True)

# Grafik dengan data representasi warna estetik bawaan Streamlit
g1, g2 = st.columns(2)
with g1:
    st.subheader("Proyeksi Klaim vs Pendapatan Premi")
    df_line = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
        'Pendapatan Premi': [400, 420, 450, 430, 470, 490],
        'Klaim Terbayar': [120, 150, 110, 190, 140, 160]
    }).set_index('Bulan')
    # Menggunakan kurva area agar gradasi warna pastelnya menyerupai gambar yang kamu berikan
    st.area_chart(df_line)

with g2:
    st.subheader("Distribusi Portofolio Berdasarkan Produk")
    df_bar = pd.DataFrame({
        'Produk': ['Term Life', 'Whole Life', 'Endowment', 'Annuity'],
        'Proporsi (%)': [40, 25, 20, 15]
    }).set_index('Produk')
    st.bar_chart(df_bar)
