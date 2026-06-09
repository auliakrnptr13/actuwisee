import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Analisis Celah Proteksi", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    html, body, [data-testid='stAppViewContainer'] { background-color: #FFF0F2 !important; }
    [data-testid='stSidebarNav'] { display: none !important; }
    .gap-box {
        background: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #D4A5B1;'>Kesenjangan Perlindungan Finansial</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #8A8A8A;'>Mengidentifikasi selisih antara kecukupan dana ideal dan realisasi aset proteksi aktif</p>", unsafe_allow_html=True)
st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    pendapatan = st.number_input("Pendapatan Bersih Bulanan (Rp)", min_value=0, value=0, step=1000000)
    tanggungan = st.number_input("Jumlah Anggota Keluarga Tanggungan", min_value=0, value=0)
with c2:
    proteksi_saat_ini = st.number_input("Nilai Polis Aktif Saat Ini (Rp)", min_value=0, value=0, step=1000000)

kebutuhan_ideal = (pendapatan * 12 * 10) + (tanggungan * 100000000)
selisih_gap = kebutuhan_ideal - proteksi_saat_ini

st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f"<div class='gap-box'><h5>Total Kebutuhan Ideal</h5><h3 style='color:#6E8E85;'>Rp {kebutuhan_ideal:,.0f}</h3></div>", unsafe_allow_html=True)
with m2:
    st.markdown(f"<div class='gap-box'><h5>Total Proteksi Riil</h5><h3 style='color:#6E8E85;'>Rp {proteksi_saat_ini:,.0f}</h3></div>", unsafe_allow_html=True)
with m3:
    warna = "#D4A5B1" if selisih_gap > 0 else "#9CC2BA"
    st.markdown(f"<div class='gap-box' style='background:#FFF5F6;'><h5>Defisit Celah Proteksi</h5><h3 style='color:{warna};'>Rp {selisih_gap:,.0f}</h3></div>", unsafe_allow_html=True)
