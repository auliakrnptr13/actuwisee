import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman & Memaksa Layout Melebar Profesional
st.set_page_config(page_title="Dashboard - ActuWise", layout="wide")

# 2. CSS Kustom untuk Efek Soft 3D UI Kit (Warna Pastel Sesuai Gambar Referensi)
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
    
    /* Desain Kontainer Kartu 3D Lembut */
    .dashboard-card {
        background-color: #FFFFFF;
        border: 1px solid #F0EAE6;
        border-radius: 20px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px rgba(236, 166, 150, 0.05);
        transition: transform 0.2s;
    }
    .dashboard-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(236, 166, 150, 0.08);
    }
    
    /* Tipografi Judul di Dalam Kartu */
    .card-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #4A4A4A;
        margin-bottom: 1rem;
    }
    
    /* Desain Teks Metrik Kustom (Menggantikan Metrik Kaku Streamlit) */
    .metric-label {
        font-size: 0.88rem;
        color: #8A8A8A;
        font-weight: 500;
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
        font-size: 0.85rem;
        font-weight: 600;
    }
    .delta-up { color: #10B981; }
    .delta-down { color: #EF4444; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigasi Bersih
st.sidebar.markdown("<h2 style='color: #ECA696; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>", unsafe_allow_html=True)
for _ in range(16): st.sidebar.write("")
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>### Aulia", unsafe_allow_html=True)

# 4. Header Halaman
st.markdown("<h1 style='color: #4A4A4A; font-weight:700; margin-bottom:0.2rem;'>Financial & Actuarial Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8A8A8A; font-size:1.05rem;'>Ringkasan eksekutif dan indikator performa utama portofolio manajemen risiko.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 5. Barisan Kartu Metrik Modern (4 Kolom Berjajar Rapi)
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Total Premium Written</div>
        <div class="metric-value-terracotta">Rp 4.25 M</div>
        <div class="metric-delta"><span class="delta-up">↑ 14.2%</span> vs bulan lalu</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Annuity Payout Exposure</div>
        <div class="metric-value-sage">Rp 1.82 M</div>
        <div class="metric-delta"><span class="delta-down">↓ 2.1%</span> vs bulan lalu</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Average Reserve Fund</div>
        <div class="metric-value-terracotta">Rp 520 Jt</div>
        <div class="metric-delta"><span class="delta-up">↑ 5.8%</span> vs bulan lalu</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="dashboard-card">
        <div class="metric-label">Active Insured Lives</div>
        <div class="metric-value-sage">12,450</div>
        <div class="metric-delta"><span class="delta-up">↑ 8.3%</span> vs bulan lalu</div>
    </div>
    """, unsafe_allow_html=True)

# 6. Bagian Grafik Berlapis di Dalam Kotak Kontainer Terpisah
g1, g2 = st.columns(2)

with g1:
    # Membungkus grafik Streamlit ke dalam div kartu buatan kita
    st.markdown('<div class="dashboard-card"><div class="card-title">Proyeksi Klaim vs Pendapatan Premi</div>', unsafe_allow_html=True)
    df_line = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
        'Pendapatan Premi': [400, 420, 450, 430, 470, 490],
        'Klaim Terbayar': [120, 150, 110, 190, 140, 160]
    }).set_index('Bulan')
    st.area_chart(df_line)
    st.markdown('</div>', unsafe_allow_html=True) # Menutup kontainer kartu

with g2:
    st.markdown('<div class="dashboard-card"><div class="card-title">Distribusi Portofolio Berdasarkan Produk</div>', unsafe_allow_html=True)
    df_bar = pd.DataFrame({
        'Produk': ['Term Life', 'Whole Life', 'Endowment', 'Annuity'],
        'Proporsi (%)': [40, 25, 20, 15]
    }).set_index('Produk')
    st.bar_chart(df_bar)
    st.markdown('</div>', unsafe_allow_html=True) # Menutup kontainer kartuwith g1:
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
