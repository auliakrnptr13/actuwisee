import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analisis Kematian", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    html, body, [data-testid='stAppViewContainer'] { background-color: #FFF0F2 !important; }
    [data-testid='stSidebarNav'] { display: none !important; }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #D4A5B1;'>Analisis Tren Demografi Risiko</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #8A8A8A;'>Metrik pemetaan probabilitas ketahanan hidup dan laju fatalitas populasi</p>", unsafe_allow_html=True)
st.markdown("---")

ages = list(range(0, 101))
rasio_kematian = [0.025 if a<1 else 0.0015 if a<10 else 0.0022 if a<30 else 0.005 if a<50 else 0.042 if a<80 else 0.22 for a in ages]

df = pd.DataFrame({"Usia": ages, "Rasio Kematian": rasio_kematian})
df["Rasio Bertahan Hidup"] = 1 - df["Rasio Kematian"]

usia_pilihan = st.slider("Pilih Parameter Usia Target", 0, 100, 25)

val_kematian = df[df["Usia"] == usia_pilihan]["Rasio Kematian"].values[0]
val_bertahan = df[df["Usia"] == usia_pilihan]["Rasio Bertahan Hidup"].values[0]

c1, c2 = st.columns(2)
with c1:
    st.markdown(f"<div class='metric-card' style='border-top: 4px solid #D4A5B1;'><h5>Rasio Kerentanan Kematian</h5><h2>{val_kematian:.4f}</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card' style='border-top: 4px solid #9CC2BA;'><h5>Rasio Peluang Bertahan Hidup</h5><h2>{val_bertahan:.4f}</h2></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
fig = px.line(df, x="Usia", y="Rasio Kematian", title="Kurva Eksponensial Risiko Berdasarkan Kematian")
fig.update_layout(paper_bgcolor="#FFF0F2", plot_bgcolor="white")
st.plotly_chart(fig, use_container_width=True)
