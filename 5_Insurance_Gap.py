
import streamlit as st
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Insurance Gap",
    page_icon="🛡️",
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

st.markdown(
    f"<h1 style='color:{PRIMARY};'>🛡️ Insurance Gap Analysis</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Analisis kecukupan perlindungan asuransi"
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    penghasilan = st.number_input(
        "Penghasilan Bulanan (Rp)",
        min_value=0,
        value=0,
        step=1000000
    )

    tanggungan = st.number_input(
        "Jumlah Tanggungan",
        min_value=0,
        value=0
    )

with col2:

    proteksi_saat_ini = st.number_input(
        "Proteksi Saat Ini (Rp)",
        min_value=0,
        value=0,
        step=1000000
    )

kebutuhan_proteksi = (
    penghasilan * 12 * 10
) + (
    tanggungan * 100_000_000
)

insurance_gap = kebutuhan_proteksi - proteksi_saat_ini


c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Kebutuhan Proteksi</h4>
        <h2>Rp {kebutuhan_proteksi:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Proteksi Saat Ini</h4>
        <h2>Rp {proteksi_saat_ini:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Insurance Gap</h4>
        <h2>Rp {insurance_gap:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=["Kebutuhan"],
        y=[kebutuhan_proteksi],
        name="Kebutuhan"
    )
)

fig.add_trace(
    go.Bar(
        x=["Proteksi"],
        y=[proteksi_saat_ini],
        name="Proteksi"
    )
)

fig.update_layout(
    title="Perbandingan Kebutuhan dan Proteksi",
    paper_bgcolor=BACKGROUND,
    plot_bgcolor="white",
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("### 📌 Interpretasi")

if kebutuhan_proteksi == 0:

    st.info(
        "Masukkan data untuk melihat hasil analisis."
    )

elif insurance_gap > 0:

    st.error(
        f"Terdapat kekurangan perlindungan sebesar Rp {insurance_gap:,.0f}"
    )

elif insurance_gap == 0:

    st.success(
        "Proteksi sudah sesuai kebutuhan."
    )

else:

    st.success(
        "Proteksi melebihi kebutuhan minimum."
    )

st.markdown("### 💡 Rekomendasi")

if tanggungan >= 3:

    st.warning(
        "Pertimbangkan peningkatan nilai pertanggungan karena jumlah tanggungan cukup banyak."
    )

elif tanggungan > 0:

    st.info(
        "Pastikan keluarga memiliki perlindungan yang memadai."
    )

else:

    st.info(
        "Fokus dapat diarahkan pada kesehatan dan dana pensiun."
    )
st.markdown("---")

st.caption(
    "ActuWise • Wise Decisions for Your Financial Future"
)
