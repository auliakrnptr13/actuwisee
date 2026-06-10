import streamlit as st
import pandas as pd
import numpy as np

# 1. Konfigurasi Halaman & Tema Dasar
st.set_page_config(
    page_title="ActuWise v2.0",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injeksi CSS untuk menjinakkan warna hitam pada form input & tombol
st.markdown("""
<style>
    html, body, [data-testid='stAppViewContainer'] {
        background-color: #FFF0F2 !important;
        font-family: 'Inter', sans-serif;
    }
    [data-testid='stSidebarNav'] { display: none !important; }
    
    /* Memperbaiki Kotak Form agar tidak hitam */
    [data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 1px solid #FAD6DC !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }

    /* Memperbaiki semua Kolom Input Teks agar latar belakangnya Putih Bersih */
    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        color: #333333 !important;
        border-radius: 8px !important;
    }
    input[data-testid="stTextInputBase"] {
        background-color: #FFFFFF !important;
        color: #333333 !important;
    }
    
    /* Memperbaiki warna label teks di atas kolom agar terbaca jelas */
    .stTextInput label {
        color: #6E8E85 !important;
        font-weight: 600 !important;
    }

    /* Memperbaiki tombol Daftar/Masuk agar tidak hitam kusam */
    button[kind="formSubmit"] {
        background-color: #6E8E85 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    button[kind="formSubmit"]:hover {
        background-color: #D4A5B1 !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(212, 165, 177, 0.4) !important;
    }
    
    /* Gaya kotak tab login/register minimalis */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFFFFF !important;
        border-radius: 8px 8px 0px 0px !important;
        padding: 10px 25px !important;
        color: #6E8E85 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #D4A5B1 !important;
        color: white !important;
        font-weight: bold !important;
    }

    /* Desain Kartu Melayang dengan Efek Transisi Halus */
    .menu-card {
        background: #FFFFFF;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(212, 165, 177, 0.15);
        text-align: center;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        border: 1px solid rgba(255, 255, 255, 0.8);
    }
    
    /* Efek Ketika Kursor Menyentuh Kartu */
    .menu-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 36px rgba(110, 142, 133, 0.2);
        background: #FAFAFA;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session States untuk sistem login, database lokal, & pemilihan menu
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'menu_terpilih' not in st.session_state:
    st.session_state.menu_terpilih = "Dashboard Utama"
if 'database_pengguna' not in st.session_state:
    st.session_state.database_pengguna = {} 

# ==========================================
# FASE 1: GATEWAY KEAMANAN (LOGIN & REGISTER)
# ==========================================
if not st.session_state.logged_in:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        st.markdown("<h2 style='text-align: center; color: #D4A5B1; font-weight: 700;'>ActuWise Security Gateway</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #6E8E85; font-weight: 500; margin-top:0;'>Silakan masuk atau buat akun baru untuk mengakses platform</p>", unsafe_allow_html=True)
        
        tab_login, tab_register = st.tabs(["Masuk (Login)", "Daftar Akun (Register)"])
        
        # --- TAB LOGIN ---
        with tab_login:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("form_login"):
                login_user = st.text_input("Username atau Email", value="")
                login_pass = st.text_input("Password", type="password", value="")
                tombol_masuk = st.form_submit_button("Masuk", use_container_width=True)
                
                if tombol_masuk:
                    if login_user in st.session_state.database_pengguna and st.session_state.database_pengguna[login_user] == login_pass:
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Username/Email atau Password salah! Pastikan akun sudah terdaftar.")
                        
        # --- TAB REGISTER ---
        with tab_register:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("form_register"):
                reg_email = st.text_input("Alamat Email", value="")
                reg_user = st.text_input("Username Baru", value="")
                reg_pass = st.text_input("Password Baru", type="password", value="")
                tombol_daftar = st.form_submit_button("Daftar Akun", use_container_width=True)
                
                if tombol_daftar:
                    if reg_email == "" or reg_user == "" or reg_pass == "":
                        st.warning("Semua kolom data wajib diisi!")
                    elif reg_user in st.session_state.database_pengguna or reg_email in st.session_state.database_pengguna:
                        st.error("Username atau Email ini sudah terdaftar!")
                    else:
                        st.session_state.database_pengguna[reg_user] = reg_pass
                        st.session_state.database_pengguna[reg_email] = reg_pass
                        st.success("Akun berhasil dibuat! Silakan masuk melalui tab Login.")
                        
    st.stop()

# ==========================================
# FASE 2: DASHBOARD UTAMA SETELAH LOGIN SUKSES
# ==========================================
st.markdown("<h1 style='color: #D4A5B1; font-weight:700; margin-bottom:0; text-align: center;'>ActuWise Analytics 2.0</h1>", unsafe_allow_html=True)
st.caption("Wise Decisions for Your Financial Future")
st.markdown("<hr style='border-color:#FAD6DC; margin-bottom: 30px;'>", unsafe_allow_html=True)

st.markdown("<h4 style='color: #6E8E85; text-align: center; margin-bottom: 25px;'>Panel Navigasi Interaktif</h4>", unsafe_allow_html=True)

# GRID KARTU MENU INOVATIF
col_a1, col_a2, col_a3 = st.columns(3)
with col_a1:
    st.markdown("""
    <div class='menu-card' style='border-top: 6px solid #9CC2BA;'>
        <h4 style='margin: 0 0 8px 0; color:#6E8E85;'>Dashboard Utama</h4>
        <p style='font-size:12px; color:#8A8A8A; margin:0;'>Ringkasan Eksekutif & KPI Finansial</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Buka Dashboard Utama", use_container_width=True):
        st.session_state.menu_terpilih = "Dashboard Utama"

with col_a2:
    st.markdown("""
    <div class='menu-card' style='border-top: 6px solid #D4A5B1;'>
        <h4 style='margin: 0 0 8px 0; color:#D4A5B1;'>Kalkulator Premi</h4>
        <p style='font-size:12px; color:#8A8A8A; margin:0;'>Perhitungan Tarif Asuransi Jiwa</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Buka Kalkulator Premi", use_container_width=True):
        st.session_state.menu_terpilih = "Kalkulator Premi"

with col_a3:
    st.markdown("""
    <div class='menu-card' style='border-top: 6px solid #E2F0CB;'>
        <h4 style='margin: 0 0 8px 0; color:#6E8E85;'>Analisis Mortalitas</h4>
        <p style='font-size:12px; color:#8A8A8A; margin:0;'>Visualisasi Data Tabel Mortalitas</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Buka Analisis Mortalitas", use_container_width=True):
        st.session_state.menu_terpilih = "Analisis Mortalitas"

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

col_b1, col_b2, col_b3 = st.columns(3)
with col_b1:
    st.markdown("""
    <div class='menu-card' style='border-top: 6px solid #E2F0CB;'>
        <h4 style='margin: 0 0 8px 0; color:#6E8E85;'>Angka Harapan Hidup</h4>
        <p style='font-size:12px; color:#8A8A8A; margin:0;'>Model Mortalitas + Faktor Sakit</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Buka Model Harapan Hidup", use_container_width=True):
        st.session_state.menu_terpilih = "Angka Harapan Hidup"

with col_b2:
    st.markdown("""
    <div class='menu-card' style='border-top: 6px solid #9CC2BA;'>
        <h4 style='margin: 0 0 8px 0; color:#6E8E85;'>Celah Proteksi</h4>
        <p style='font-size:12px; color:#8A8A8A; margin:0;'>Analisis Kesenjangan Asuransi Pasar</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Buka Analisis Celah Proteksi", use_container_width=True):
        st.session_state.menu_terpilih = "Analisis Celah Proteksi"

with col_b3:
    st.markdown("""
    <div class='menu-card' style='border-top: 6px solid #D4A5B1;'>
        <h4 style='margin: 0 0 8px 0; color:#D4A5B1;'>Tentang Aplikasi</h4>
        <p style='font-size:12px; color:#8A8A8A; margin:0;'>Informasi Pengembang & Metodologi</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Buka Tentang Aplikasi", use_container_width=True):
        st.session_state.menu_terpilih = "Tentang Aplikasi"

st.markdown("<br><hr style='border-color:#FAD6DC;'><br>", unsafe_allow_html=True)

# ==========================================
# FASE 3: LOGIKA KONTEN DINAMIS (BEBAS RUMUS)
# ==========================================

# --- MENU 1: DASHBOARD UTAMA ---
if st.session_state.menu_terpilih == "Dashboard Utama":
    st.markdown(f"### Menu Aktif: {st.session_state.menu_terpilih}")
    
    st.write("##### Input Data Finansial (Simulasi Aktual)")
    in1, in2, in3 = st.columns(3)
    with in1:
        val1 = st.number_input("Pendapatan Premi Written (Miliar Rp)", min_value=0.0, value=0.0, step=0.1)
    with in2:
        val2 = st.number_input("Eksposur Klaim Anuitas (Miliar Rp)", min_value=0.0, value=0.0, step=0.1)
    with in3:
        val3 = st.number_input("Dana Cadangan Wajib Keharusan (Juta Rp)", min_value=0, value=0, step=10)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"<div style='background-color: #E8F1F5; padding: 20px; border-radius: 12px; border: 1px solid #D0E1E9;'><h5>Total Pendapatan Premi</h5><h2>Rp {val1:.2f} M</h2></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div style='background-color: #E8F1F5; padding: 20px; border-radius: 12px; border: 1px solid #D0E1E9;'><h5>Eksposur Klaim Anuitas</h5><h2>Rp {val2:.2f} M</h2></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div style='background-color: #E8F1F5; padding: 20px; border-radius: 12px; border: 1px solid #D0E1E9;'><h5>Dana Cadangan Wajib</h5><h2>Rp {val3} Jt</h2></div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    g1, g2 = st.columns(2)
    with g1:
        st.write("###### Tren Pemodelan Real-Time")
        df_line = pd.DataFrame({'Bulan': ['Awal', 'Proyeksi'], 'Pendapatan Premi': [0.0, float(val1)], 'Klaim Terbayar': [0.0, float(val2)]}).set_index('Bulan')
        st.area_chart(df_line, color=["#E2F0CB", "#9CC2BA"])
    with g2:
        st.write("###### Distribusi Komposisi")
        df_bar = pd.DataFrame({'Komponen': ['Premi', 'Klaim'], 'Nilai': [float(val1), float(val2)]}).set_index('Komponen')
        st.bar_chart(df_bar, color="#E2F0CB")

# --- MENU 2: KALKULATOR PREMI ---
elif st.session_state.menu_terpilih == "Kalkulator Premi":
    st.markdown(f"### Menu Aktif: {st.session_state.menu_terpilih}")
    with st.container(border=True):
        input_premi_dasar = st.number_input("Nilai Premi Dasar Utama (Rp)", min_value=0, value=0, step=10000)
        usia = st.slider("Usia Pemohon Aktual", 0, 70, 0)
        
        total_kalkulasi = 0.0 if (input_premi_dasar == 0 or usia == 0) else float(input_premi_dasar * (1 + (usia * 0.02)))
            
        st.markdown(f"<div style='background-color: #E2F0CB; padding: 25px; border-radius: 12px; text-align: center; border: 2px dashed #9CC2BA;'><h5>Estimasi Beban Premi Bulanan</h5><h1 style='color: #6E8E85; margin:10px 0;'>Rp {total_kalkulasi:,.0f}</h1></div>", unsafe_allow_html=True)

# --- MENU 3: ANALISIS MORTALITAS ---
elif st.session_state.menu_terpilih == "Analisis Mortalitas":
    st.markdown(f"### Menu Aktif: {st.session_state.menu_terpilih}")
    st.write("Input nilai estimasi probabilitas risiko kematian untuk penyesuaian proyeksi grafik populasi:")
    
    val_qx = st.number_input("Rasio Risiko Kematian Populasi", min_value=0.000, max_value=1.000, value=0.000, format="%.4f")
    df_mort = pd.DataFrame({'Metrik': ['Kondisi Dasar', 'Hasil Kalkulasi'], 'Tingkat Risiko': [0.0, float(val_qx)]}).set_index('Metrik')
    st.bar_chart(df_mort, color="#9CC2BA")

# --- MENU 4: ANGKA HARAPAN HIDUP ---
elif st.session_state.menu_terpilih == "Angka Harapan Hidup":
    st.markdown(f"### Menu Aktif: {st.session_state.menu_terpilih}")
    
    usia_input = st.number_input("Batas Usia Saat Ini", value=0, min_value=0, max_value=100)
    status_kesehatan = st.selectbox("Status Morbiditas Klinis", ["Belum Dipilih", "Sehat / Standard", "Sakit Ringan (Hipertensi/Asam Urat)", "Sakit Kronis (Jantung/Diabetes Melitus)"])
    
    if (usia_input == 0 or status_kesehatan == "Belum Dipilih"):
        harapan_hidup_terkoreksi = 0.0
        loading_factor = 0.0
        warna_grafik = "#8A8A8A"
    else:
        loading_factor = 1.0 if status_kesehatan == "Sehat / Standard" else (1.5 if status_kesehatan == "Sakit Ringan (Hipertensi/Asam Urat)" else 2.5)
        warna_grafik = "#9CC2BA" if loading_factor == 1.0 else ("#E2F0CB" if loading_factor == 1.5 else "#D4A5B1")
        harapan_hidup_terkoreksi = float(max(0, 80 - usia_input) / loading_factor)
        
    st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 12px; border-left: 8px solid {warna_grafik};'><h4>Sisa Angka Harapan Hidup Efektif</h4><h2>{harapan_hidup_terkoreksi:.1f} Tahun</h2><p style='margin:0;'>Indeks Variabel Beban Risiko: {loading_factor} kali</p></div>", unsafe_allow_html=True)

# --- MENU 5: ANALISIS CELAH PROTEKSI ---
elif st.session_state.menu_terpilih == "Analisis Celah Proteksi":
    st.markdown(f"### Menu Aktif: {st.session_state.menu_terpilih}")
    
    ideal = st.number_input("Kebutuhan Proteksi Ideal Portofolio (Miliar Rp)", min_value=0.0, value=0.0)
    riil = st.number_input("Realisasi Kepemilikan Polis Aktual (Miliar Rp)", min_value=0.0, value=0.0)
    
    df_gap = pd.DataFrame({'Kondisi': ['Kebutuhan Ideal', 'Kepemilikan Riil'], 'Nilai Proteksi (M)': [float(ideal), float(riil)]}).set_index('Kondisi')
    st.line_chart(df_gap, color=["#D4A5B1"])

# --- MENU 6: TENTANG APLIKASI ---
elif st.session_state.menu_terpilih == "Tentang Aplikasi":
    st.markdown(f"### Menu Aktif: {st.session_state.menu_terpilih}")
    st.markdown("""
    <div style='background-color: white; padding: 30px; border-radius: 12px; border-bottom: 5px solid #D4A5B1;'>
        <h4>ActuWise Platform v2.0</h4>
        <p>Aplikasi ini dikembangkan untuk mendemonstrasikan integrasi komparatif pemodelan aktuaria berbasis web secara modern, responsif, dan komersial.</p>
        <hr style='border-color:#f1f5f9;'>
        <p style='font-size: 14px; color:#8A8A8A; margin:0;'><b>Platform Developer:</b> Aulia Kurnia Putri</p>
    </div>
    """, unsafe_allow_html=True)

# Tombol Keluar Sistem
st.markdown("<br><br><br>", unsafe_allow_html=True)
if st.button("Keluar Aplikasi (Log Out)", use_container_width=True):
    st.session_state.logged_in = False
    st.session_state.menu_terpilih = "Dashboard Utama"
    st.rerun()
