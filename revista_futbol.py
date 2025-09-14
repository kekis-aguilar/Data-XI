import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ELEVEN DATA", layout="wide")

# ------------------ SWITCH DE MODO ------------------
modo_claro = st.toggle("🌞 / 🌙 Cambiar tema", value=True)

# CSS dinámico
if modo_claro:
    fondo = "#ffffff"
    texto = "#111111"
    subtitulo = "#555555"
    color_barras = "#007acc"
else:
    fondo = "#111111"
    texto = "#f5f5f5"
    subtitulo = "#aaaaaa"
    color_barras = "limegreen"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {fondo};
        color: {texto};
    }}
    h1 {{
        font-size: 60px !important;
        color: {texto};
    }}
    h3 {{
        color: {subtitulo};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ CABECERA ------------------
col1, col2 = st.columns([1,6])
with col1:
    st.image("https://raw.githubusercontent.com/kekis-aguilar/Data-XI/88f7bfee363408bba592025e74c9ea453148cf95/Eleven_Data.png", width=100)
with col2:
    st.markdown(
        f"""
        <h1 style='text-align: left; font-family: Arial Black, sans-serif;'>
            ELEVEN DATA
        </h1>
        <h3 style='text-align: left;'>{'Edición Septiembre 2025'}</h3>
        """,
        unsafe_allow_html=True
    )

# ------------------ HERO VIDEO ------------------
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <iframe width="800" height="450" 
            src="https://www.youtube.com/embed/dUIvoexhMyw" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
            encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
        </iframe>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <p style='text-align: center; font-size: 20px; color:{texto};'>
    Bienvenido a la revista digital de <b>estadísticas y análisis de fútbol</b>.  
    Explora comparativas, dashboards y artículos exclusivos sobre tus jugadores favoritos.
    </p>
    """, unsafe_allow_html=True
)

# ------------------ NOTICIAS DESTACADAS ------------------
# ------------------ SECCIÓN INTERACTIVA ------------------
st.subheader("📊 Sección Interactiva")

col1, col2, col3 = st.columns(3)

# --- Columna 1: Datos curiosos ---
with col1:
    st.subheader("🤯 Datos Curiosos")
    st.markdown("- ⚽ El partido más largo de la historia duró **65 horas** en Inglaterra (1981).")
    st.markdown("- 🚀 Cristiano Ronaldo salta hasta **2.93m** en un cabezazo.")
    st.markdown("- 🥅 El gol más rápido fue a los **2.4 segundos** (Arabia Saudita, 2009).")

# --- Columna 2 y 3: Selector de liga ---
ligas = ["Liga MX", "Premier League", "LaLiga", "Serie A"]
liga_seleccionada = st.selectbox("Selecciona una liga", ligas)

# Datos de ejemplo
tablas_posiciones = {
    "Liga MX": pd.DataFrame({
        "Equipo": ["América", "Monterrey", "Chivas", "Pumas"],
        "Pts": [30, 28, 25, 22],
        "PJ": [14, 14, 14, 14]
    }),
    "Premier League": pd.DataFrame({
        "Equipo": ["Man City", "Arsenal", "Liverpool", "Chelsea"],
        "Pts": [34, 32, 29, 25],
        "PJ": [14, 14, 14, 14]
    }),
    "LaLiga": pd.DataFrame({
        "Equipo": ["Real Madrid", "Barcelona", "Atlético", "Sevilla"],
        "Pts": [33, 31, 27, 21],
        "PJ": [14, 14, 14, 14]
    }),
    "Serie A": pd.DataFrame({
        "Equipo": ["Inter", "Milan", "Juventus", "Roma"],
        "Pts": [35, 30, 28, 24],
        "PJ": [14, 14, 14, 14]
    })
}

tablas_goleo = {
    "Liga MX": pd.DataFrame({
        "Jugador": ["Henry Martín", "Gignac", "Quiñones"],
        "Goles": [12, 10, 9]
    }),
    "Premier League": pd.DataFrame({
        "Jugador": ["Haaland", "Salah", "Rashford"],
        "Goles": [14, 11, 9]
    }),
    "LaLiga": pd.DataFrame({
        "Jugador": ["Lewandowski", "Benzema", "Griezmann"],
        "Goles": [13, 10, 8]
    }),
    "Serie A": pd.DataFrame({
        "Jugador": ["Osimhen", "Lautaro", "Immobile"],
        "Goles": [11, 9, 8]
    })
}

# --- Columna 2: Tabla General ---
with col2:
    st.subheader(f"🏆 {liga_seleccionada} - Tabla General")
    st.dataframe(
        tablas_posiciones[liga_seleccionada].style.set_properties(
            **{"color": texto, "background-color": fondo}
        )
    )

# --- Columna 3: Tabla de Goleadores ---
with col3:
    st.subheader(f"🥇 {liga_seleccionada} - Goleadores")
    st.dataframe(
        tablas_goleo[liga_seleccionada].style.set_properties(
            **{"color": texto, "background-color": fondo}
        )
    )


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
ax.bar(df["Jugador"], df["Goles"], color=color_barras)
ax.set_ylabel("Goles", color=texto)
ax.set_title("Goles por jugador", color=texto)
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
