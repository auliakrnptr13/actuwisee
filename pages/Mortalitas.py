
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Mortality Analytics",
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
    f"<h1 style='color:{PRIMARY};'>📊 Mortality Analytics</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Analisis probabilitas kematian dan survival"
)

st.markdown("---")

ages = list(range(0,101))

qx = []

for age in ages:

    if age < 1:
        qx.append(0.025)

    elif age < 10:
        qx.append(0.0015)

    elif age < 20:
        qx.append(0.0018)

    elif age < 30:
        qx.append(0.0022)

    elif age < 40:
        qx.append(0.0030)

    elif age < 50:
        qx.append(0.0050)

    elif age < 60:
        qx.append(0.0085)

    elif age < 70:
        qx.append(0.0160)

    elif age < 80:
        qx.append(0.0420)

    elif age < 90:
        qx.append(0.1050)

    else:
        qx.append(0.2200)

df = pd.DataFrame({
    "Usia": ages,
    "qx": qx
})

df["px"] = 1 - df["qx"]

usia = st.slider(
    "Pilih Usia",
    min_value=0,
    max_value=100,
    value=0
)

qx_value = df[df["Usia"] == usia]["qx"].values[0]
px_value = df[df["Usia"] == usia]["px"].values[0]

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Probabilitas Kematian (qx)</h4>
        <h2>{qx_value:.4f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class='metric-card'>
        <h4>Probabilitas Bertahan Hidup (px)</h4>
        <h2>{px_value:.4f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

fig = px.line(
    df,
    x="Usia",
    y="qx",
    title="Kurva Mortalitas"
)

fig.update_traces(
    line_width=4
)

fig.update_layout(
    paper_bgcolor=BACKGROUND,
    plot_bgcolor="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

with st.expander("📋 Data Mortalitas"):

    st.dataframe(
        df,
        use_container_width=True
    )

st.markdown("### 📌 Interpretasi")

if usia < 30:

    st.success(
        "Risiko mortalitas relatif rendah."
    )

elif usia < 60:

    st.info(
        "Risiko mortalitas mulai meningkat seiring bertambahnya usia."
    )

else:

    st.warning(
        "Risiko mortalitas meningkat signifikan pada usia lanjut."
    )
    
st.markdown("---")

st.caption(
    "ActuWise • Wise Decisions for Your Financial Future"
)
