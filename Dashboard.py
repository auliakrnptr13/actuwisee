import streamlit as st
import pandas as pd
import numpy as np
import os

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="ActuWise",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded" # Sidebar otomatis terbuka di laptop, fleksibel di HP
)

# INJEKSI CSS: Warna Premium & Gaya Kartu About
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [data-testid='stAppViewContainer'] {
        background-color: #FFF2F4 !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* BANNER SELAMAT DATANG */
    .welcome-box {
        background: linear-gradient(135deg, #FFD6E0 0%, #FAD6DC 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(212, 165, 177, 0.2);
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.7);
    }

    /* KARTU ABOUT DI BAWAH */
    .about-section {
        background: #FFFFFF;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(212, 165, 177, 0.15);
        border-left: 6px solid #D4A5B1;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧭 NAVIGASI DI BILAH SAMPING (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("<h3 style='color: #C38B9B; font-weight:700;'>Navigation Panel</h3>", unsafe_allow_html=True)
    st.write("Silakan pilih halaman analisis:")
    
    # Menu pilihan menggunakan radio button yang estetik di sidebar
    menu_terpilih = st.radio(
        "Pilih Menu:",
        [
            "📊 Dashboard Utama", 
            "🧮 Kalkulator Premi", 
            "📈 Analisis Mortalitas", 
            "🧬 Angka Harapan Hidup", 
            "🔍 Celah Proteksi"
        ]
    )

# ==========================================
# HEADER & BANNER SELAMAT DATANG (HALAMAN UTAMA)
# ==========================================
st.markdown("""
<div class='welcome-box'>
    <h1 style='color: #C38B9B; font-weight:700; margin:0; font-size: 32px;'>🌿 Selamat Datang di ActuWise v2.0</h1>
    <p style='color: #6E8E85; font-weight: 600; margin-top: 8px; font-size: 16px; letter-spacing: 0.5px;'>
        Wise Decisions for Your Financial Future
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"<h3 style='color: #C38B9B;'>📌 {menu_terpilih}</h3>", unsafe_allow_html=True)
st.markdown("<hr style='border-color:#FAD6DC; margin-bottom: 25px;'>", unsafe_allow_html=True)


# ==========================================
# LOGIKA KONTEN DINAMIS & INTERAKTIF
# ==========================================

# --- MENU 1: DASHBOARD UTAMA ---
if "Dashboard Utama" in menu_terpilih:
    st.write("##### Input Data Finansial (Simulasi Aktual)")
    in1, in2 = st.columns(2)
    with in1:
        val1 = st.number_input("Pendapatan Premi Tercatat (Miliar Rp)", min_value=0.0, value=12.5, step=0.1)
    with in2:
        val2 = st.number_input("Eksposur Klaim Anuitas (Miliar Rp)", min_value=0.0, value=4.2, step=0.1)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 🌟 FITUR BARU: PILIHAN BENTUK GRAFIK
    st.write("##### 🛠️ Pengaturan Visualisasi")
    tipe_grafik = st.selectbox("Pilih Bentuk Grafik Tren Finansial:", ["Grafik Garis (Line Chart)", "Grafik Area (Area Chart)", "Grafik Batang (Bar Chart)"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Data simulasi untuk grafik
    df_tren = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr'], 
        'Pendapatan Premi': [5.0, 8.0, 10.0, float(val1)], 
        'Klaim Terbayar': [1.0, 2.0, 3.0, float(val2)]
    }).set_index('Bulan')
    
    # Logika perubahan bentuk grafik berdasarkan pilihan user
    if tipe_grafik == "Grafik Garis (Line Chart)":
        st.line_chart(df_tren, color=["#9CC2BA", "#D4A5B1"])
    elif tipe_grafik == "Grafik Area (Area Chart)":
        st.area_chart(df_tren, color=["#9CC2BA", "#D4A5B1"])
    elif tipe_grafik == "Grafik Batang (Bar Chart)":
        st.bar_chart(df_tren, color=["#9CC2BA", "#D4A5B1"])

# --- MENU 2: KALKULATOR PREMI ---
elif "Kalkulator Premi" in menu_terpilih:
    with st.container(border=True):
        input_premi_dasar = st.number_input("Nilai Uang Pertanggungan Dasar (Rp)", min_value=0, value=100000000, step=10000000)
        usia = st.slider("Usia Pemohon Saat Ini", 15, 70, 25)
        
        total_kalkulasi = float(input_premi_dasar * (0.002 + (usia * 0.0001)))
        st.markdown(f"<div style='background-color: #E2F0CB; padding: 25px; border-radius: 12px; text-align: center; border: 2px dashed #9CC2BA;'><h5>Estimasi Kontribusi Premi Tahunan</h5><h1 style='color: #6E8E85; margin:10px 0;'>Rp {total_kalkulasi:,.0f}</h1></div>", unsafe_allow_html=True)

# --- MENU 3: ANALISIS MORTALITAS ---
elif "Analisis Mortalitas" in menu_terpilih:
    val_qx = st.number_input("Sesuaikan Faktor Risiko Kematian Dasar", min_value=0.001, max_value=1.000, value=0.024, format="%.4f")
    
    tipe_grafik_mort = st.radio("Pilih Model Grafik Mortalitas:", ["Batang (Bar)", "Garis (Line)"])
    
    df_mort = pd.DataFrame({'Metrik': ['Rasio Wilayah A', 'Rasio Wilayah B', 'Hasil Koreksi'], 'Tingkat Risiko': [0.015, 0.032, float(val_qx)]}).set_index('Metrik')
    
    if tipe_grafik_mort == "Batang (Bar)":
        st.bar_chart(df_mort, color="#9CC2BA")
    else:
        st.line_chart(df_mort, color="#9CC2BA")

# --- MENU 4: ANGKA HARAPAN HIDUP ---
elif "Angka Harapan Hidup" in menu_terpilih:
    usia_input = st.number_input("Masukkan Usia Responden", value=22, min_value=0, max_value=90)
    status_kesehatan = st.selectbox("Kondisi Riwayat Medis", ["Sehat Tanpa Gejala / Standard", "Sakit Ringan Terkontrol", "Sakit Kronis Komplikasi"])
    
    loading_factor = 1.0 if "Standard" in status_kesehatan else (1.4 if "Ringan" in status_kesehatan else 2.2)
    harapan_hidup_terkoreksi = float(max(0, 78 - usia_input) / loading_factor)
        
    st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 12px; border-left: 8px solid #9CC2BA;'><h4>Sisa Ekspektasi Sisa Umur Produktif</h4><h2>{harapan_hidup_terkoreksi:.1f} Tahun</h2><p style='margin:0; color:#8A8A8A;'>Koefisien Pengali Risiko Kesehatan: {loading_factor}x</p></div>", unsafe_allow_html=True)

# --- MENU 5: ANALISIS CELAH PROTEKSI ---
elif "Celah Proteksi" in menu_terpilih:
    ideal = st.number_input("Kebutuhan Dana Proteksi Keluarga Ideal (Rp)", min_value=0.0, value=500000000.0, step=50000000.0)
    riil = st.number_input("Polis yang Sudah Dimiliki Saat Ini (Rp)", min_value=0.0, value=150000000.0, step=50000000.0)
    
    celah = float(max(0.0, ideal - riil))
    st.markdown(f"<div style='background-color: #FFF0F2; padding: 20px; border-radius: 12px; border: 1px solid #FAD6DC; margin-bottom:20px;'><h5>Defisit Celah Proteksi Finansial (Insurance Gap)</h5><h2 style='color:#D4A5B1;'>Rp {celah:,.0f}</h2></div>", unsafe_allow_html=True)
    
    tipe_grafik_gap = st.selectbox("Ubah Tampilan Grafik Celah:", ["Grafik Garis", "Grafik Area"])
    df_gap = pd.DataFrame({'Kondisi': ['Kebutuhan Ideal', 'Nilai Riil'], 'Nilai Rupiah': [float(ideal), float(riil)]}).set_index('Kondisi')
    
    if tipe_grafik_gap == "Grafik Garis":
        st.line_chart(df_gap, color=["#6E8E85"])
    else:
        st.area_chart(df_gap, color=["#6E8E85"])


# ==========================================
# 📋 BAGIAN ABOUT (MENETAP DI BAWAH HALAMAN)
# ==========================================
st.markdown("<br><br><hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #6E8E85;'>ℹ️ Tentang Platform & Pengembang</h4>", unsafe_allow_html=True)

col_abt1, col_abt2 = st.columns(2)
with col_abt1:
    st.markdown("""
    <div class='about-section' style='border-left-color: #9CC2BA;'>
        <h5 style='color: #6E8E85; margin-top: 0; font-weight: 600;'>Sistem Kerja ActuWise</h5>
        <p style='font-size: 14px; color: #5A5A5A; line-height: 1.6; margin: 0;'>
            ActuWise dirancang khusus untuk mempermudah visualisasi pemodelan matematika aktuaria, 
            perhitungan estimasi premi asuransi, sisa angka harapan hidup, serta mendeteksi 
            kesenjangan celah proteksi keuangan secara interaktif dan modern.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_abt2:
    st.markdown("""
    <div class='about-section'>
        <h5 style='color: #C38B9B; margin-top: 0; font-weight: 600;'>Otoritas Pengembang</h5>
        <p style='font-size: 15px; color: #2D3748; margin-bottom: 4px;'><b>Aulia Kurnia Putri</b></p>
        <p style='font-size: 13px; color: #6E8E85; margin-top: 0;'>Program Studi Matematika, Universitas Andalas</p>
        <p style='font-size: 12px; color: #A0AEC0; border-top: 1px solid #EDF2F7; padding-top: 8px; margin-top: 12px; margin-bottom: 0;'>
            Arsitektur: Python Core • Streamlit UI • Interactive Chart Engine
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 ActuWise • Wise Decisions for Your Financial Future")
