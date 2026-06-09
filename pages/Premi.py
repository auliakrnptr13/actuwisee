import streamlit as st

st.set_page_config(page_title="Kalkulator Premi", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    html, body, [data-testid='stAppViewContainer'] { background-color: #FFF0F2 !important; }
    [data-testid='stSidebarNav'] { display: none !important; }
    .result-box {
        background: white;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(212, 165, 177, 0.1);
        border-top: 5px solid #9CC2BA;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #6E8E85;'>Kalkulator Premi Asuransi</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #8A8A8A;'>Simulasi perhitungan komparatif beban dana berdasarkan profil risiko eksekutif</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    usia = st.number_input("Usia Pemohon (Tahun)", min_value=0, max_value=100, value=0)
    jenis_kelamin = st.selectbox("Klasifikasi Jenis Kelamin", ["Perempuan", "Laki-laki"])
with col2:
    uang_pertanggungan = st.number_input("Total Nilai Pertanggungan Ideal (Rp)", min_value=0, value=0, step=10000000)

premi = 0
if usia > 0 and uang_pertanggungan > 0:
    premi = uang_pertanggungan * 0.005
    if usia > 40: premiums *= 1.25
    if usia > 60: premiums *= 1.50
    if jenis_kelamin == "Laki-laki": premi *= 1.10

premi_bulanan = premi / 12

st.markdown("<br><h4 style='color: #6E8E85;'>Hasil Analisis Beban Dana</h4>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"<div class='result-box'><h5>Alokasi Premi Tahunan</h5><h2 style='color:#6E8E85;'>Rp {premi:,.0f}</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='result-box' style='border-top-color:#D4A5B1;'><h5 style='color:#D4A5B1;'>Alokasi Premi Bulanan</h5><h2 style='color:#D4A5B1;'>Rp {premi_bulanan:,.0f}</h2></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if premi == 0:
    st.info("Silakan lengkapi parameter di atas untuk memproses kalkulasi.")
elif premi < 5000000:
    st.success("Tingkat beban dana tergolong efisien dan berisiko rendah.")
else:
    st.warning("Tingkat beban dana masuk kategori tinggi. Diperlukan penyesuaian nilai portofolio.")
