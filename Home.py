import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman Utama
st.set_page_config(
    page_title="ActuWise - Actuarial Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="auto"
)

# 2. Fungsi Sidebar Navigasi Resmi Streamlit
def render_sidebar():
    st.sidebar.title("ActuWise")
    st.sidebar.caption("Smart Actuarial Platform")
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("Menu Navigasi")
    st.sidebar.page_link("Home.py", label="Dashboard Utama", icon=":material/monitoring:")
    st.sidebar.page_link("pages/Premium_Calculator.py", label="Kalkulator Premi", icon=":material/calculate:")
    st.sidebar.page_link("pages/Mortality_Analytics.py", label="Analisis Mortalitas", icon=":material/analytics:")
    st.sidebar.page_link("pages/Life_Expectancy.py", label="Angka Harapan Hidup", icon=":material/hourglass_empty:")
    st.sidebar.page_link("pages/Insurance_Gap.py", label="Analisis Celah Proteksi", icon=":material/shield:")
    st.sidebar.page_link("pages/About.py", label="Tentang Aplikasi", icon=":material/info:")
    
    st.sidebar.markdown("---")
    st.sidebar.write("**Platform Developer:**")
    st.sidebar.write("by Aulia Kurnia Putri")

render_sidebar()

# 3. Konten Utama Dashboard
st.title("ActuWise Analytics")
st.write("**Wise Decisions for Your Financial Future**")
st.caption("Sistem Ringkasan Indikator Performa Utama & Manajemen Risiko Aktuaria")
st.markdown("---")

# 4. Barisan Kartu Metrik Angka Ringkas
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Total Premium Written", value="Rp 4.25 M", delta="14.2% mtd")
with m2:
    st.metric(label="Annuity Payout Exposure", value="Rp 1.82 M", delta="-2.1% mtd", delta_color="inverse")
with m3:
    st.metric(label="Average Reserve Fund", value="Rp 520 Jt", delta="5.8% mtd")
with m4:
    st.metric(label="Active Insured Lives", value="12,450", delta="8.3% mtd")

st.markdown("---")

# 5. Blok Visualisasi Grafik & Fitur Export Data
g1, g2 = st.columns(2)
with g1:
    st.subheader("Proyeksi Klaim vs Pendapatan Premi")
    df_line = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'], 
        'Pendapatan Premi (Juta)': [400, 420, 450, 430, 470, 490], 
        'Klaim Terbayar (Juta)': [120, 150, 110, 190, 140, 160]
    }).set_index('Bulan')
    st.area_chart(df_line)
    
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
    st.subheader("Distribusi Portofolio Produk")
    df_bar = pd.DataFrame({
        'Produk': ['Term Life', 'Whole Life', 'Endowment', 'Annuity'], 
        'Proporsi (%)': [40, 25, 20, 15]
    }).set_index('Produk')
    st.bar_chart(df_bar)
