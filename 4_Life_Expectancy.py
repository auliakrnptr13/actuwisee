
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Life Expectancy",
    page_icon="🌱",
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

.metric-card {{
    background:white;
    padding:20px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
    f"<h1 style='color:{PRIMARY};'>🌱 Life Expectancy Analysis</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Estimasi harapan hidup berdasarkan usia saat ini"
)

st.markdown("---")

usia = st.number_input(
    "Masukkan Usia Saat Ini",
    min_value=0,
    max_value=100,
    value=0
)

harapan_hidup = max(0, 80 - usia)

usia_akhir = usia + harapan_hidup

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Sisa Harapan Hidup</h4>
        <h2>{harapan_hidup} Tahun</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Estimasi Usia Akhir</h4>
        <h2>{usia_akhir} Tahun</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=["Usia Saat Ini"],
        y=[usia],
        name="Saat Ini"
    )
)

fig.add_trace(
    go.Bar(
        x=["Estimasi Akhir"],
        y=[usia_akhir],
        name="Estimasi"
    )
)

fig.update_layout(
    title="Perbandingan Usia Saat Ini dan Estimasi Usia Akhir",
    paper_bgcolor=BACKGROUND,
    plot_bgcolor="white",
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("### 📌 Interpretasi")

if usia == 0:

    st.info(
        "Masukkan usia untuk melihat estimasi harapan hidup."
    )

elif usia < 30:

    st.success(
        "Usia masih muda, periode perencanaan keuangan masih sangat panjang."
    )

elif usia < 50:

    st.info(
        "Mulai penting mempertimbangkan proteksi dan investasi jangka panjang."
    )

else:

    st.warning(
        "Perencanaan pensiun dan kesehatan menjadi prioritas utama."
    )

st.markdown("---")

st.caption(
    "ActuWise • Wise Decisions for Your Financial Future"
)
