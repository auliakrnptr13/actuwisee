
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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

.card {{
    background:white;
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}}

.card-title {{
    color:{SECONDARY};
    font-size:15px;
}}

.card-value {{
    color:{PRIMARY};
    font-size:28px;
    font-weight:bold;
}}

</style>
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <h1 style='color:{PRIMARY};'>
    📊 Dashboard Overview
    </h1>
    """,
    unsafe_allow_html=True
)

st.caption("Wise Decisions for Your Financial Future")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>Premi Estimasi</div>
        <div class='card-value'>Rp 0</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>Mortalitas (qx)</div>
        <div class='card-value'>0.0000</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>Life Expectancy</div>
        <div class='card-value'>80 Tahun</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>Insurance Gap</div>
        <div class='card-value'>Rp 0</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

st.subheader("📈 Mortality Trend")

usia = [20, 30, 40, 50, 60, 70, 80]

qx = [
    0.002,
    0.003,
    0.005,
    0.009,
    0.016,
    0.042,
    0.105
]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=usia,
        y=qx,
        mode="lines+markers",
        name="qx"
    )
)

fig.update_layout(
    title="Kurva Mortalitas",
    paper_bgcolor=BACKGROUND,
    plot_bgcolor="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📋 Ringkasan Sistem")

st.info(
    """ActuWise adalah platform aktuaria berbasis web
yang membantu pengguna melakukan simulasi premi,
analisis mortalitas, life expectancy,
dan insurance gap secara interaktif.
"""
)

st.write("")
st.write("")

st.subheader("🚀 Quick Access")

a, b, c = st.columns(3)

with a:
    st.page_link(
        "pages/2_Premi.py",
        label="💰 Premium Calculator"
    )

with b:
    st.page_link(
        "pages/3_Mortalitas.py",
        label="📊 Mortality Analytics"
    )

with c:
    st.page_link(
        "pages/5_Insurance_Gap.py",
        label="🛡️ Insurance Gap"
    )

st.markdown("---")

st.caption(
    "© 2026 ActuWise • Wise Decisions for Your Financial Future"
)
