import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ELEVEN DATA", layout="wide")

# ------------------ CABECERA ------------------
st.markdown(
    """
    <style>
    body {
        background-color: #111; /* fondo oscuro */
    }
    h1 {
        font-size: 60px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo y título
col1, col2 = st.columns([1,6])
with col1:
    st.image("https://raw.githubusercontent.com/kekis-aguilar/Data-XI/88f7bfee363408bba592025e74c9ea453148cf95/Eleven_Data.png", width=100)
with col2:
    st.markdown(
        """
        <h1 style='text-align: left; 
                   font-size: 60px;
                   background: -webkit-linear-gradient(#00ff99, #00ccff);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   font-family: Arial Black, sans-serif;'>
            ELEVEN DATA
        </h1>
        <h3 style='text-align: left; color: gray;'>Edición Septiembre 2025</h3>
        """,
        unsafe_allow_html=True
    )

# ------------------ HERO IMAGE ------------------
st.image("https://images.unsplash.com/photo-1521412644187-c49fa049e84d", use_column_width=True)

st.markdown("""
<p style='text-align: center; font-size: 20px;'>
Bienvenido a la revista digital de <b>estadísticas y análisis de fútbol</b>.  
Explora comparativas, dashboards y artículos exclusivos sobre tus jugadores favoritos.
</p>
""", unsafe_allow_html=True)

# ------------------ NOTICIAS DESTACADAS ------------------
st.subheader("📰 Noticias Destacadas")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1508098682722-e99c43a406b2", use_column_width=True)
    st.markdown("**Messi sigue imparable**")
    st.caption("El astro argentino rompe otro récord histórico en goles y asistencias.")

with col2:
    st.image("https://images.unsplash.com/photo-1522770179533-24471fcdba45", use_column_width=True)
    st.markdown("**Cristiano desafía el tiempo**")
    st.caption("A sus 40 años, CR7 sigue demostrando vigencia en la élite.")

with col3:
    st.image("https://images.unsplash.com/photo-1521412644187-c49fa049e84d", use_column_width=True)
    st.markdown("**Mbappé, el heredero**")
    st.caption("El francés lidera la nueva generación y se acerca a la cima mundial.")

# ------------------ DASHBOARD ------------------
st.subheader("📊 Dashboard de Estadísticas")

data = {
    "Jugador": ["Messi", "Cristiano", "Mbappé", "Haaland"],
    "Goles": [30, 28, 25, 27],
    "Asistencias": [12, 9, 10, 5],
    "Partidos": [28, 30, 26, 25]
}
df = pd.DataFrame(data)

st.dataframe(df)

fig, ax = plt.subplots()
ax.bar(df["Jugador"], df["Goles"], color="limegreen")
ax.set_ylabel("Goles")
ax.set_title("Goles por jugador")
st.pyplot(fig)

# ------------------ COMPARADOR ------------------
st.subheader("⚔️ Comparador de Jugadores")

jugadores = ["Messi", "Cristiano", "Mbappé", "Haaland"]
col1, col2 = st.columns(2)
with col1:
    j1 = st.selectbox("Jugador 1", jugadores, index=0)
with col2:
    j2 = st.selectbox("Jugador 2", jugadores, index=1)

st.write(f"Comparando **{j1}** vs **{j2}**")

df_stats = pd.DataFrame(data)
comparativa = df_stats[df_stats["Jugador"].isin([j1, j2])]
st.dataframe(comparativa.set_index("Jugador"))
