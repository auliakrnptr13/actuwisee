import streamlit as st

st.set_page_config(page_title="Insurance Gap - ActuWise", layout="wide")

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #F8F3F0 !important; }
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #EFEAE6; }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("<h2 style='color: #ECA696; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>", unsafe_allow_html=True)
for _ in range(16): st.sidebar.write("")
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>### Aulia", unsafe_allow_html=True)

st.title("Insurance Gap Analysis")
st.markdown("Mengukur celah proteksi keuangan (Capital Underinsurance) menggunakan Pendekatan Nilai Ekonomi Manusia.")

col_gap1, col_gap2 = st.columns(2)
with col_gap1:
    st.subheader("Parameter Keuangan & Kebutuhan")
    pendapatan = st.number_input("Pendapatan Bersih Tahunan (Rp)", min_value=0, value=120_000_000, step=10_000_000)
    pengeluaran_rutin = st.number_input("Pengeluaran Keluarga Tahunan (Rp)", min_value=0, value=80_000_000, step=5_000_000)
    tahun_proteksi = st.slider("Durasi Penggantian Pendapatan yang Diinginkan (Tahun)", 1, 30, 15)

with col_gap2:
    st.subheader("Proteksi Saat Ini")
    total_up_sekarang = st.number_input("Total Uang Pertanggungan Aktif Saat Ini (Rp)", min_value=0, value=300_000_000)
    inflasi = st.slider("Asumsi Inflasi / Tingkat Pertumbuhan (%)", 1, 12, 5) / 100

v_gap = 1 / (1 + inflasi)
annuity_factor = (1 - (v_gap ** tahun_proteksi)) / (1 - v_gap)
up_ideal = pengeluaran_rutin * annuity_factor
insurance_gap = up_ideal - total_up_sekarang

st.markdown("---")
st.subheader("Kesimpulan Analisis Finansial")

if insurance_gap > 0:
    st.warning(f"Kekurangan nilai proteksi (Insurance Gap) yang harus dipenuhi: Rp {insurance_gap:,.2f} (Total kebutuhan ideal: Rp {up_ideal:,.2f})")
    persen_siap = min(int((total_up_sekarang / up_ideal) * 100), 100)
    st.progress(persen_siap / 100, text=f"Tingkat Kecukupan Proteksi: {persen_siap}%")
else:
    st.success(f"Proteksi finansial sudah mencukupi. Nilai proteksi saat ini telah memenuhi standar kebutuhan nilai ekonomi ideal keluarga (Rp {up_ideal:,.2f}).")
