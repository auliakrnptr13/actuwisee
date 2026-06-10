import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Analisis Mortalitas 3D - ActuWise", layout="wide")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    html, body, [data-testid='stAppViewContainer'] {
        background-color: #FFF2F4 !important;
        font-family: 'Inter', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #C38B9B;'><i class='fa-solid fa-cube'></i> Analisis Mortalitas Ruang 3D</h2>", unsafe_allow_html=True)
st.markdown("<hr style='border-color:#FAD6DC;'>", unsafe_allow_html=True)

# Input Interaktif dari User
val_qx = st.number_input("Sesuaikan Faktor Risiko Kematian Dasar (q_x)", min_value=0.001, max_value=1.000, value=0.024, format="%.4f")

st.write("##### 🛠️ Pengaturan Dimensi Visualisasi")
tipe_grafik_3d = st.selectbox("Pilih Model Grafik 3D (Bisa Diputar/Digeser):", ["Grafik Batang Balok 3D", "Grafik Garis Ruang 3D"])

# Data untuk visualisasi 3D (Sumbu X: Kategori, Sumbu Y: Wilayah, Sumbu Z: Nilai Risiko)
kategori = ['Rasio Wilayah A', 'Rasio Wilayah B', 'Hasil Koreksi']
wilayah_index = [1, 2, 3] # Sumbu kedalaman ruang Y
nilai_risiko = [0.015, 0.032, float(val_qx)]

# MEMBUAT GRAFIK 3D INTERAKTIF
fig = go.Figure()

if tipe_grafik_3d == "Grafik Batang Balok 3D":
    # Membuat efek balok timbul menggunakan go.Bar3d alternatif (Mesh3d)
    for i in range(len(kategori)):
        # Membuat koordinat kubus/balok untuk efek 3D nyata
        fig.add_trace(go.Mesh3d(
            x=[i, i+0.5, i+0.5, i, i, i+0.5, i+0.5, i],
            y=[0, 0, 1, 1, 0, 0, 1, 1],
            z=[0, 0, 0, 0, nilai_risiko[i], nilai_risiko[i], nilai_risiko[i], nilai_risiko[i]],
            colorbar_title='Skala Risiko',
            colorscale=[[0, '#9CC2BA'], [1, '#D4A5B1']],
            intensity=[0, 0, 0, 0, 1, 1, 1, 1],
            name=kategori[i],
            showscale=False
        ))
else:
    # Grafik Garis Alur Ruang 3D
    fig.add_trace(go.Scatter3d(
        x=kategori,
        y=wilayah_index,
        z=nilai_risiko,
        mode='lines+markers',
        line=dict(color='#C38B9B', width=6),
        marker=dict(size=8, color='#6E8E85', opacity=0.9)
    ))

# Mengatur Tampilan Sudut Pandang Kamera Ruang 3D
fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        xaxis=dict(title='Komponen Data', backgroundcolor="rgb(255, 242, 244)", gridcolor="white", showbackground=True),
        yaxis=dict(title='Indeks Kedalaman', backgroundcolor="rgb(255, 242, 244)", gridcolor="white", showbackground=True),
        zaxis=dict(title='Tingkat Risiko (Z)', backgroundcolor="rgb(255, 242, 244)", gridcolor="white", showbackground=True),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)) # Sudut pandang awal 3D yang estetik
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Tampilkan grafik 3D di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.info("💡 Tips Dosen: Gunakan jarimu (di HP) atau klik kanan mouse (di Laptop) lalu geser untuk memutar grafik 3D ini ke segala arah!")
