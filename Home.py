import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="ActuWise - Actuarial Platform",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Implementasi CSS Berdasarkan Gambar Soft 3D UI Kit
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Latar belakang dasar mengikuti warna hangat di gambar */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8F3F0 !important;
    }
    
    /* Menyesuaikan Sidebar agar serasi */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #EFEAE6;
    }
    
    /* Hero Box dengan efek Soft Gradasi 3D Pastel */
    .hero-box {
        text-align: center;
        padding: 4rem 2rem 2rem 2rem;
        background: linear-gradient(135deg, #FBECE8 0%, #FFFFFF 100%);
        border-radius: 24px;
        margin-bottom: 3rem;
        border: 1px solid #EFEAE6;
        box-shadow: 0 10px 30px rgba(236, 166, 150, 0.05);
    }
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
