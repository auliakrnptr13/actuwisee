import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman & Memaksa Layout Responsif Melebar
st.set_page_config(
    page_title="ActuWise - Actuarial Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="auto"
)

# 2. CSS Premium Berdasarkan Soft 3D Pastel UI Kit (Sangat Ramah Mobile/Laptop)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { 
        background-color: #F8F3F0 !important; 
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] { 
        background-color: #FFFFFF !important; 
        border-right: 1px solid #EFEAE6; 
    }
    
    /* Desain Banner Atas Minimalis */
    .dashboard-header {
        background: linear-gradient(135deg, #FBECE8 0%, #FFFFFF 100%);
        padding: 2rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        border: 1px solid #EFEAE6;
        box-shadow: 0 10px 30px rgba(236, 166, 150, 0.04);
    }
    .main-title {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: #ECA696;
        margin-bottom: 0.2rem;
    }
    .main-subtitle {
        font-size: 1rem;
        color: #8A8A8A;
    }
    
    /* Desain Kartu Kontainer 3D Lembut */
    .dashboard-card {
        background-color: #FFFFFF;
        border: 1px solid #F0EAE6;
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 8px 24px rgba(236, 166, 150, 0.04);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .dashboard-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(236, 166, 150, 0.08);
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #4A4A4A;
        margin-bottom: 1rem;
    }
    
    /* Metrik Kustom Estetik */
    .metric-label {
        font-size: 0.8rem;
        color: #9A9A9A;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value-terracotta {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ECA696;
        margin: 5px 0;
    }
    .metric-value-sage {
        font-size: 1.8rem;
        font-weight: 700;
        color: #9CC2BA;
        margin: 5px 0;
    }
    .metric-delta {
        font-size: 0.8rem;
        font-weight: 500;
    }
    .delta-up { color: #10B981; }
    .delta-down { color: #EF4444; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigasi Otomatis (Akan menyesuaikan Laptop / HP)
def render_sidebar():
    st.sidebar.markdown("<h2 style='color: #ECA696; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<hr style='margin-top:0; border-color:#EFEAE6;'>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<p style='color: #8A8A8A; font-size:0.8rem; font-weight:600; text-transform:uppercase; margin-bottom:0.8rem;'>Menu Navigasi</p>", unsafe_allow_html=True)
    
    # Navigasi Menu Utama (Home bertindak langsung sebagai Dashboard)
    st.sidebar.page_link("Home.py", label="Dashboard Utama", icon=":material/monitoring:")
    st.sidebar.page_link("pages/2_Premium_Calculator.py", label="Kalkulator Premi", icon=":material/calculate:")
    st.sidebar.page_link("pages/3_Mortality_Analytics.py", label="Analisis Mortalitas", icon=":material/analytics:")
    st.sidebar.page_link("pages/4_Life_Expectancy.py", label="Angka Harapan Hidup", icon=":material/hourglass_empty:")
    st.sidebar.page_link("pages/5_Insurance_Gap.py", label="Analisis Celah Proteksi", icon=":material/shield:")
    st.sidebar.page_link("pages/6_About.py", label="Tentang Aplikasi", icon=":material/info:")
    
    st.sidebar.markdown("<hr style='border-color:#EFEAE6; margin-top:3rem;'>### Aulia", unsafe_allow_html=True)

render_sidebar()

# ================================================
# INTERFACE UTAMA (LANGSUNG DASHBOARD)
# ================================================

# Banner Dashboard
st.markdown("""
<div class="dashboard-header">
    <div class="main-title">ActuWise Analytics</div>
    <div class="main-subtitle">Sistem Ringkasan Indikator Performa Utama & Manajemen Risiko Aktuaria</div>
</div>
""", unsafe_allow_html=True)

# Barisan Kartu Metrik Estetik (Otomatis membungkus rapi jika dibuka di HP)
m1, m2, m3, m4 = st.columns([1, 1, 1, 1])

with m1:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Total Premium Written</div>
        <div class="metric-value-terracotta">Rp 4.25 M</div>
        <div class="metric-delta"><span class="delta-up">↑ 14.2%</span> mtd</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Annuity Payout Exposure</div>
        <div class="metric-value-sage">Rp 1.82 M</div>
        <div class="metric-delta"><span class="delta-down">↓ 2.1%</span> mtd</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Average Reserve Fund</div>
        <div class="metric-value-terracotta">Rp 520 Jt</div>
        <div class="metric-delta"><span class="delta-up">↑ 5.8%</span> mtd</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Active Insured Lives</div>
        <div class="metric-value-sage">12,450</div>
        <div class="metric-delta"><span class="delta-up">↑ 8.3%</span> mtd</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Layout Grafik Berdampingan
g1, g2 = st.columns(2)

with g1:
    st.markdown('<div class="dashboard-card"><div class="card-title">Proyeksi Klaim vs Pendapatan Premi</div>', unsafe_allow_html=True)
    df_line = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
        'Pendapatan Premi': [400, 420, 450, 430, 470, 490],
        'Klaim Terbayar': [120, 150, 110, 190, 140, 160]
    }).set_index('Bulan')
    # Grafik area memberikan nuansa gelombang gradasi lembut seperti gambar referensimu
    st.area_chart(df_line)
    st.markdown('</div>', unsafe_allow_html=True)

with g2:
    st.markdown('<div class="dashboard-card"><div class="card-title">Distribusi Portofolio Produk</div>', unsafe_allow_html=True)
    df_bar = pd.DataFrame({
        'Produk': ['Term Life', 'Whole Life', 'Endowment', 'Annuity'],
        'Proporsi (%)': [40, 25, 20, 15]
    }).set_index('Produk')
    st.bar_chart(df_bar)
    st.markdown('</div>', unsafe_allow_html=True)    }
    .brand-title {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        color: #ECA696; /* Menggunakan warna terracotta khas gambar */
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
    }
    .brand-sub {
        font-size: 1.6rem !important;
        font-weight: 600;
        color: #4A4A4A;
        margin-bottom: 0.5rem;
    }
    .brand-tagline {
        font-size: 1.1rem;
        color: #8A8A8A;
        margin-bottom: 2rem;
    }
    
    /* Kartu Statistik Bergaya Soft 3D UI */
    .card-stat {
        background-color: #FFFFFF;
        border: 1px solid #F0EAE6;
        border-radius: 18px;
        padding: 1.8rem;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.02);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card-stat:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(236, 166, 150, 0.1);
    }
    .stat-num {
        font-size: 2.8rem !important;
        font-weight: 700;
        color: #9CC2BA; /* Warna Sage Green dari gambar */
    }
    .stat-num-alt {
        font-size: 2.8rem !important;
        font-weight: 700;
        color: #ECA696; /* Warna Terracotta dari gambar */
    }
    .stat-lbl {
        font-size: 0.95rem;
        color: #7A7A7A;
        font-weight: 500;
        margin-top: 5px;
    }
    
    /* Mempercantik info box streamlit agar bernuansa pastel */
    .stAlert {
        background-color: #FFFFFF !important;
        border: 1px solid #FBECE8 !important;
        border-radius: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigasi
def render_sidebar():
    st.sidebar.markdown("<h2 style='color: #ECA696; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<hr style='margin-top:0; border-color:#EFEAE6;'>", unsafe_allow_html=True)
    
    for _ in range(16): 
        st.sidebar.write("")
        
    st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>", unsafe_allow_html=True)
    col_user, col_out = st.sidebar.columns([2, 1])
    with col_user:
        st.markdown("<p style='margin:0; font-weight:600; color:#4A4A4A;'>Aulia</p>", unsafe_allow_html=True)
    with col_out:
        if st.button("Logout", key="lg_home", type="secondary", use_container_width=True):
            st.toast("Logged out")

render_sidebar()

# ================================================
# INTERFACE UTAMA
# ================================================

st.markdown("""
<div class="hero-box">
    <div class="brand-title">ActuWise</div>
    <div class="brand-sub">Wise Decisions for Your Financial Future</div>
    <div class="brand-tagline">Smart Actuarial & Financial Planning Platform</div>
</div>
""", unsafe_allow_html=True)

# Tombol masuk dengan penyesuaian posisi tengah
c1, c2, c3 = st.columns([1.5, 1, 1.5])
with c2:
    st.link_button("Masuk ke Dashboard", "/Dashboard", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Grid Statistik Bergaya 3D Soft Pastel
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown('<div class="card-stat"><div class="stat-num">100+</div><div class="stat-lbl">Simulasi Risiko</div></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="card-stat"><div class="stat-num-alt">6</div><div class="stat-lbl">Modul Utama</div></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="card-stat"><div class="stat-num">24/7</div><div class="stat-lbl">Akses Sistem</div></div>', unsafe_allow_html=True)

st.markdown("<br><hr style='border-color:#EFEAE6;'><br>", unsafe_allow_html=True)

# Deskripsi Modul Utama
st.markdown("<h3 style='text-align: center; color: #4A4A4A; font-weight:600; margin-bottom:2rem;'>Eksplorasi Modul Utama</h3>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    st.info("**Premium Calculator**\n\nKalkulasi Premi Tunggal Bersih menggunakan model komutasi aktuaria secara presisi.")
    st.info("**Insurance Gap**\n\nAnalisis celah proteksi finansial keluarga berdasarkan nilai ekonomi hidup.")
with f2:
    st.info("**Mortality Analytics**\n\nVisualisasi interaktif tabel mortalitas dengan hukum Makeham-Gompertz.")
    st.info("**Retirement Planning**\n\nSimulasi proyeksi dana pensiun di hari tua secara berkala.")
with f3:
    st.info("**Life Expectancy**\n\nEstimasi angka harapan hidup sisa menggunakan probabilitas kelangsungan hidup.")
    st.info("**Report Generator**\n\nEkspor ringkasan eksekutif hasil analisis ke dalam laporan ringkas.")
