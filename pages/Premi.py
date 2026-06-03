import streamlit as st
import pandas as pd

st.set_page_config(page_title="Premium Calculator - ActuWise", layout="wide")

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #F8F3F0 !important; }
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #EFEAE6; }
    div[data-testid="stMetricValue"] { font-size: 2rem !important; font-weight: 700 !important; color: #ECA696; }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("<h2 style='color: #ECA696; font-weight:700; margin-bottom:0;'>ActuWise</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #9A9A9A; font-size:0.85rem; margin-top:0;'>Smart Actuarial Platform</p>", unsafe_allow_html=True)
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>", unsafe_allow_html=True)
for _ in range(16): st.sidebar.write("")
st.sidebar.markdown("<hr style='border-color:#EFEAE6;'>### Aulia", unsafe_allow_html=True)

st.title("Premium Calculator (Asuransi Jiwa Berjangka)")
st.markdown("Perhitungan Premi Tunggal Bersih ($A^1_{x:\\overline{n}|}$) berdasarkan Model Pendanaan Diskonto Aktuaria.")

col_in1, col_in2, col_in3 = st.columns(3)
with col_in1:
    usia = st.number_input("Usia Tertanggung (x)", min_value=20, max_value=70, value=30)
with col_in2:
    jangka_waktu = st.number_input("Jangka Waktu Proteksi (n tahun)", min_value=1, max_value=40, value=10)
with col_in3:
    bunga = st.slider("Tingkat Bunga Teknis / Diskonto (i)", min_value=0.01, max_value=0.15, value=0.05, step=0.01)

uang_pertanggungan = st.number_input("Uang Pertanggungan (Sum Assured - Rp)", min_value=10_000_000, value=100_000_000, step=10_000_000)

tingkat_diskonto = 1 / (1 + bunga)
usia_rentang = list(range(usia, usia + jangka_waktu))
qx_list = [0.001 * (1.06 ** t) for t in range(jangka_waktu)]
px_list = [1 - q for q in qx_list]

nsp = 0.0
t_p_x = 1.0

for t in range(jangka_waktu):
    v_t_1 = tingkat_diskonto ** (t + 1)
    current_qx = qx_list[t]
    nsp += v_t_1 * t_p_x * current_qx
    t_p_x *= px_list[t]

premi_tunggal_bersih = nsp * uang_pertanggungan
premi_tahunan_bersih = premi_tunggal_bersih / (((1 - (tingkat_diskonto ** jangka_waktu)) / (1 - tingkat_diskonto)) * 0.7)

st.markdown("---")
st.subheader("Hasil Estimasi Aktuaria")

res_col1, res_col2 = st.columns(2)
with res_col1:
    st.metric(label="Premi Tunggal Bersih (Net Single Premium)", value=f"Rp {premi_tunggal_bersih:,.2f}")
with res_col2:
    st.metric(label="Estimasi Premi Tahunan (Level Premium)", value=f"Rp {premi_tahunan_bersih:,.2f}")

st.subheader("Tabel Proyeksi Risiko Tahunan")
df_proyeksi = pd.DataFrame({
    'Tahun Ke-t': range(1, jangka_waktu + 1),
    'Usia Tercapai': usia_rentang,
    'Peluang Meninggal (qx)': qx_list,
    'Faktor Diskonto (v^t)': [tingkat_diskonto ** t for t in range(1, jangka_waktu + 1)]
}).set_index('Tahun Ke-t')
st.dataframe(df_proyeksi, use_container_width=True)
