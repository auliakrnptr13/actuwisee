
import streamlit as st

st.set_page_config(
    page_title="ActuWise",
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
    background-color: {BACKGROUND};
}}

.hero {{
    text-align:center;
    padding-top:40px;
    padding-bottom:40px;
}}

.hero-title {{
    font-size:55px;
    font-weight:bold;
    color:{PRIMARY};
}}

.hero-subtitle {{
    font-size:22px;
    color:{SECONDARY};
}}

.feature-card {{
    background:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    height:180px;
}}

</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([1,4])

with col1:

    try:
        st.image("assets/logo.png", width=120)
    except:
        st.markdown("## 🌿")

with col2:

    st.markdown(
        f"""
        <div style="padding-top:20px;">
        <h1 style="color:{PRIMARY}; margin-bottom:0;">
        ActuWise
        </h1>
        <p style="color:{SECONDARY}; font-size:20px;">
        Wise Decisions for Your Financial Future
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-title">
            Smart Actuarial Dashboard
        </div>

        <div class="hero-subtitle">
            Financial Planning • Insurance • Mortality Analytics
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.page_link(
    "pages/1_Dashboard.py",
    label="🚀 Enter Dashboard",
    use_container_width=True
)

st.write("")
st.write("")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class="feature-card">
    <h3>💰 Premium Calculator</h3>
    <p>
    Hitung estimasi premi berdasarkan profil pengguna.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="feature-card">
    <h3>📊 Mortality Analytics</h3>
    <p>
    Analisis probabilitas kematian dan survival.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="feature-card">
    <h3>🛡️ Insurance Gap</h3>
    <p>
    Evaluasi kecukupan perlindungan finansial.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("---")

st.caption(
    "© 2026 ActuWise • Wise Decisions for Your Financial Future"
)
