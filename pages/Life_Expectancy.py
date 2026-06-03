import streamlit as st
import pandas as pd

st.set_page_config(page_title="Life Expectancy - ActuWise", layout="wide")

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

st.title("Life Expectancy Projection")
st.markdown("Perhitungan angka harapan hidup masa depan ($e_x$) menggunakan integrasi numerik diskret probabilitas kelangsungan hidup.")

st.latex(r"e_x = \sum_{t=1}^{\omega - x} {}_tp_x")

usia_input = st.number_input("Masukkan Usia Saat Ini untuk Proyeksi", min_value=0, max_value=90, value=22)

ages = list(range(0, 110))
qx = [min(0.0005 + 0.00008 * (1.09 ** x), 1.0) for x in ages]

tpx_list = []
t_p_x = 1.0
for x in range(usia_input, 105):
    current_qx = qx[x]
    t_p_x *= (1 - current_qx)
    tpx_list.append(t_p_x)

ex = sum(tpx_list)

st.info(f"Seseorang yang saat ini berusia {usia_input} tahun, secara statistik diproyeksikan memiliki sisa angka harapan hidup tambahan selama {ex:.2f} tahun (Hingga mencapai total usia {usia_input + ex:.2f} tahun).")

st.subheader(f"Probabilitas Bertahan Hidup Hingga t-Tahun ke Depan (_tp_{{{usia_input}}})")
df_tpx = pd.DataFrame({
    'Tahun Ke-t': range(1, len(tpx_list) + 1),
    'Probabilitas Bertahan': tpx_list
}).set_index('Tahun Ke-t')
st.area_chart(df_tpx)
