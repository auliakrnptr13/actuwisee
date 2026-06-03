
import streamlit as st

st.set_page_config(
    page_title="About ActuWise",
    page_icon="🌿",
    layout="wide"
)

PRIMARY = "#0A3323"
SECONDARY = "#105666"
CARD = "#839958"
BACKGROUND = "#F7F4D5"
ACCENT = "#D3968C"

st.markdown(f"""
<style>

.stApp {{
    background-color:{BACKGROUND};
}}

.info-card {{
    background:white;
    padding:25px;
    border-radius:20px;
    margin-bottom:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}}

</style>
""", unsafe_allow_html=True)
st.markdown(
    f"<h1 style='color:{PRIMARY};'>🌿 About ActuWise</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Wise Decisions for Your Financial Future"
)

st.markdown("---")

try:
    st.image(
        "assets/logo.png",
        width=180
    )
except:
    st.info("Logo ActuWise belum tersedia.")

st.markdown("""
<div class='info-card'>

<h3>📌 Tentang ActuWise</h3>

ActuWise adalah aplikasi berbasis web yang membantu pengguna melakukan simulasi dan analisis aktuaria secara interaktif.

Fitur utama:

• Premium Calculator

• Mortality Analytics

• Life Expectancy Analysis

• Insurance Gap Analysis

• Interactive Dashboard

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>

<h3>⚙️ Teknologi</h3>

<ul>
<li>Python</li>
<li>Streamlit</li>
<li>Pandas</li>
<li>Plotly</li>
<li>GitHub</li>
<li>Streamlit Community Cloud</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>

<h3>👩‍🎓 Pengembang</h3>

<b>Aulia Kurnia Putri</b>

Program Studi Matematika

ActuWise dikembangkan sebagai implementasi konsep aktuaria dan analisis data berbasis web.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>

<h3>🎯 Visi</h3>

Menjadi platform edukatif yang membantu masyarakat memahami risiko, proteksi asuransi, dan perencanaan keuangan dengan pendekatan aktuaria yang mudah dipahami.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.caption(
    "© 2026 ActuWise • Wise Decisions for Your Financial Future"
)
