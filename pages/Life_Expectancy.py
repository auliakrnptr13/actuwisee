import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Ekspektasi Hidup", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    html, body, [data-testid='stAppViewContainer'] { background-color: #FFF0F2 !important; }
    [data-testid='stSidebarNav'] { display: none !important; }
    .card-display {
        background: white;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(212, 165, 177, 0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #6E8E85;'>Analisis Angka Harapan Hidup</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #8A8A8A;'>Proyeksi matematis sisa durasi hidup produktif berdasarkan profil kesehatan kronis</p>", unsafe_allow_html=True)
st.markdown("---")

usia_saat_ini = st.number_input("Input Batas Usia Pemohon Saat Ini", min_value=0, max_value=100, value=0)
sisa_harapan = max(0, 80 - usia_saat_ini)
estimasi_akhir = usia_saat_ini + sisa_harapan

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='card-display' style='border-left: 6px solid #9CC2BA;'><h5>Sisa Proyeksi Harapan Hidup</h5><h2>{sisa_harapan} Tahun</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='card-display' style='border-left: 6px solid #D4A5B1;'><h5>Estimasi Target Batas Usia</h5><h2>{estimasi_akhir} Tahun</h2></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if usia_saat_ini == 0:
    st.info("Silakan input parameter usia untuk memunculkan analisis komparatif.")
elif usia_saat_ini < 40:
    st.success("Kategori usia produktif awal. Durasi investasi jangka panjang sangat direkomendasikan.")
else:
    st.warning("Prioritas utama dialihkan ke jaminan kesehatan masa pensiun.")
