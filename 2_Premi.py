
import streamlit as st

st.set_page_config(
    page_title="Premium Calculator",
    page_icon="💰",
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

.result-card {{
    background:white;
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}}

</style>
""", unsafe_allow_html=True)

st.markdown(
    f"<h1 style='color:{PRIMARY};'>💰 Premium Calculator</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Simulasi premi asuransi berdasarkan profil pengguna"
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    usia = st.number_input(
        "Usia",
        min_value=0,
        max_value=100,
        value=0
    )

    jenis_kelamin = st.selectbox(
        "Jenis Kelamin",
        ["Perempuan", "Laki-laki"]
    )

with col2:

    uang_pertanggungan = st.number_input(
        "Uang Pertanggungan (Rp)",
        min_value=0,
        value=0,
        step=10000000
    )

premi = 0

if usia > 0 and uang_pertanggungan > 0:

    premi = uang_pertanggungan * 0.005

    if usia > 40:
        premi *= 1.25

    if usia > 60:
        premi *= 1.50

    if jenis_kelamin == "Laki-laki":
        premi *= 1.10

premi_bulanan = premi / 12

st.markdown("## 📊 Hasil Simulasi")

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
        <div class='result-card'>
        <h3>Premi Tahunan</h3>
        <h2>Rp {premi:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class='result-card'>
        <h3>Premi Bulanan</h3>
        <h2>Rp {premi_bulanan:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.subheader("📌 Interpretasi")

if premi == 0:

    st.info(
        "Masukkan data terlebih dahulu untuk melakukan simulasi."
    )

elif premi < 5000000:

    st.success(
        "Premi relatif ringan."
    )

elif premi < 10000000:

    st.warning(
        "Premi berada pada kategori menengah."
    )

else:

    st.error(
        "Premi cukup tinggi, pertimbangkan evaluasi kebutuhan proteksi."
    )

st.markdown("---")

st.caption(
    "ActuWise • Wise Decisions for Your Financial Future"
)
