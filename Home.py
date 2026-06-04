import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman Utama
st.set_page_config(
    page_title="ActuWise - Actuarial Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="auto"
)

# 2. Desain Tema Warna Kustom (Pink Pastel, Dusty Pink, Sage, & Biru Pastel)
# Metode ini diisolasi ketat agar 100% aman dari SyntaxError
st.markdown("<style>html, body, [data-testid='stAppViewContainer'] { background-color: #FFF0F2 !important; font-family: 'Inter', sans-serif; }</style>", unsafe_allow_html=True)
st.markdown("<style>[data-testid='stSidebar'] { background-color: #FFFFFF !important; border-right: 1px solid #FAD6DC; }</style>", unsafe_allow_html=True)
st.markdown("<style>.stMetric { background-color: #E8F1F5 !important; padding: 1.2rem !important; border-radius: 16px !important; border: 1px solid #D0E1E9 !important; }</style>", unsafe_allow_html=True)

# 3. Fungsi Sidebar Navigasi Persis Tampilan Gambar 1 dengan Sentuhan Dusty Pink
def render_sidebar():
    # Judul ActuWise berwarna Dusty Pink yang anggun
    st.sidebar.markdown("<h2 style='color: #D4A5B1; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<hr style='margin-top:0; border-color:#FAD6DC;'>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<p style='color: #8A8A8A; font-size:0.8rem; font-weight:600; text-transform:uppercase; margin-bottom:0.8rem;'>MENU NAVIGASI</p>", unsafe_allow_html=True)
    
    # Jalur Link disamakan dengan isi folder GitHub kamu (Menggunakan Emoji agar 100% muncul)
    st.sidebar.page_link("Home.py", label="Dashboard Utama", icon="📈")
    st.sidebar.page_link("pages/Premi.py", label="Kalkulator Premi", icon="🧮")
    st.sidebar.page_link("pages/Mortalitas.py", label="Analisis Mortalitas", icon="📊")
    st.sidebar.page_link("pages/Life_Expectancy.py", label="Angka Harapan Hidup", icon="⏳")
    st.sidebar.page_link("pages/Insurance_Gap.py", label="Analisis Celah Proteksi", icon="🛡️")
    st.sidebar.page_link("pages/About.py", label="Tentang Aplikasi", icon="ℹ️")
    
    st.sidebar.markdown("<hr style='border-color:#FAD6DC; margin-top:3rem;'>", unsafe_allow_html=True)
    
    # Identitas Pembuat Aplikasi berwarna Dusty Pink
    st.sidebar.markdown("<p style='font-size: 0.85rem; color: #8A8A8A; margin-bottom: 0;'>Platform Developer:</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-weight: 700; color: #D4A5B1; margin-top: 0; font-size: 1.1rem;'>by Aulia Kurnia Putri</p>", unsafe_allow_html=True)

render_sidebar()

# 4. Konten Utama Dashboard dengan Judul Berwarna Dusty Pink
st.markdown("<h1 style='color: #D4A5B1; font-weight:700; margin-bottom:0;'>ActuWise Analytics</h1>", unsafe_allow_html=True)
st.write("**Wise Decisions for Your Financial Future**")
st.caption("Sistem Ringkasan Indikator Performa Utama & Manajemen Risiko Aktuaria")
st.markdown("<hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)

# 5. Barisan Kartu Metrik Angka Ringkas (Otomatis Berlatar Belakang Biru Pastel)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Total Premium Written", value="Rp 4.25 M", delta="14.2% mtd")
with m2:
    st.metric(label="Annuity Payout Exposure", value="Rp 1.82 M", delta="-2.1% mtd", delta_color="inverse")
with m3:
    st.metric(label="Average Reserve Fund", value="Rp 520 Jt", delta="5.8% mtd")
with m4:
    st.metric(label="Active Insured Lives", value="12,450", delta="8.3% mtd")

st.markdown("<br>", unsafe_allow_html=True)

# 6. Blok Visualisasi Grafik Warna Hijau Sage & Fitur Export Data
g1, g2 = st.columns(2)
with g1:
    st.markdown("<h3 style='color: #6E8E85;'>Proyeksi Klaim vs Pendapatan Premi</h3>", unsafe_allow_html=True)
    df_line = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'], 
        'Pendapatan Premi': [400, 420, 450, 430, 470, 490], 
        'Klaim Terbayar': [120, 150, 110, 190, 140, 160]
    }).set_index('Bulan')
    
    # Grafik Area menggunakan warna Hijau Sage kustom (Hex: #9CC2BA)
    st.area_chart(df_line, color=["#9CC2BA", "#6E8E85"])
    
    # Fitur Export Excel / CSV
    csv_data = df_line.to_csv().encode('utf-8')
    st.download_button(
        label="📊 Export Data Proyeksi ke Excel (CSV)",
        data=csv_data,
        file_name="Proyeksi_Klaim_ActuWise.csv",
        mime="text/csv",
        use_container_width=True
    )

with g2:
    st.markdown("<h3 style='color: #6E8E85;'>Distribusi Portofolio Produk</h3>", unsafe_allow_html=True)
    df_bar = pd.DataFrame({
        'Produk': ['Term Life', 'Whole Life', 'Endowment', 'Annuity'], 
        'Proporsi (%)': [40, 25, 20, 15]
    }).set_index('Produk')
    
    # Grafik Batang menggunakan warna Hijau Sage kustom (Hex: #9CC2BA)
    st.bar_chart(df_bar, color="#9CC2BA")
