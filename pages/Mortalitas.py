import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mortality Analytics - ActuWise", layout="wide")

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

st.title("Mortality Analytics & Curve Visualizer")
st.markdown("Analisis visual Tabel Mortalitas Indonesia (TMI) untuk memodelkan struktur intensitas mortalitas.")

ages = list(range(0, 101))
qx = [0.0005 + 0.00008 * (1.09 ** x) if x > 5 else 0.005 / (x+1) for x in ages]
qx = [min(q, 1.0) for q in qx]

lx = []
current_lx = 100000
for q in qx:
    lx.append(int(current_lx))
    current_lx *= (1 - q)

df_mortalitas = pd.DataFrame({
    'Usia (x)': ages,
    'lx (Jumlah Bertahan)': lx,
    'qx (Peluang Meninggal)': qx
}).set_index('Usia (x)')

usia_pilihan = st.slider("Pilih Rentang Usia Analisis", 0, 100, (20, 80))
df_filtered = df_mortalitas.loc[usia_pilihan[0]:usia_pilihan[1]]

col_g1, col_g2 = st.columns(2)
with col_g1:
    st.subheader("Kurva Kelangsungan Hidup (lx)")
    st.area_chart(df_filtered['lx (Jumlah Bertahan)'])
with col_g2:
    st.subheader("Kurva Intensitas Kematian (qx)")
    st.line_chart(df_filtered['qx (Peluang Meninggal)'])

st.markdown("---")
st.subheader("Data Mentah Tabel Mortalitas")
st.dataframe(df_filtered, use_container_width=True)
