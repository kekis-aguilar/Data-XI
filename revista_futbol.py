import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ELEVEN DATA", layout="wide")

# Inicializar la página en sesión si no existe
if "page" not in st.session_state:
    st.session_state.page = "portada"

# ------------------ NAVBAR ------------------
col1, col2, col3 = st.columns([1,1,1])

with col1:
    # Logo → Portada
    if st.button(" ", key="logo"):
        st.session_state.page = "portada"
    st.image("https://raw.githubusercontent.com/kekis-aguilar/Data-XI/88f7bfee363408bba592025e74c9ea453148cf95/Eleven_Data.png", width=80)

with col2:
    if st.button("📊 Dashboard"):
        st.session_state.page = "dashboard"

with col3:
    if st.button("⚔️ Comparador"):
        st.session_state.page = "comparador"


# ------------------ CONTENIDO ------------------
if st.session_state.page == "portada":
    st.markdown("<h1 style='text-align: center; color: darkgreen;'>ELEVEN DATA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Edición Septiembre 2025</h3>", unsafe_allow_html=True)

    st.image("https://raw.githubusercontent.com/kekis-aguilar/Data-XI/88f7bfee363408bba592025e74c9ea453148cf95/Eleven_Data.png", width=80)


    st.markdown("""
    <p style='text-align: center; font-size: 18px;'>
    Bienvenido a la revista digital de <b>estadísticas y análisis de fútbol</b>.  
    Explora comparativas, dashboards y artículos exclusivos sobre tus jugadores favoritos.
    </p>
    """, unsafe_allow_html=True)

elif st.session_state.page == "dashboard":
    st.title("📊 Dashboard de Estadísticas")

    data = {
        "Jugador": ["Messi", "Cristiano", "Mbappé", "Haaland"],
        "Goles": [30, 28, 25, 27],
        "Asistencias": [12, 9, 10, 5],
        "Partidos": [28, 30, 26, 25]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)

    st.subheader("Comparativa de Goles")
    fig, ax = plt.subplots()
    ax.bar(df["Jugador"], df["Goles"], color="blue")
    ax.set_ylabel("Goles")
    ax.set_title("Goles por jugador")
    st.pyplot(fig)

elif st.session_state.page == "comparador":
    st.title("⚔️ Comparador de Jugadores")

    jugadores = ["Messi", "Cristiano", "Mbappé", "Haaland"]
    j1 = st.selectbox("Jugador 1", jugadores, index=0)
    j2 = st.selectbox("Jugador 2", jugadores, index=1)

    st.write(f"Comparando **{j1}** vs **{j2}**")

    stats = {
        "Jugador": ["Messi", "Cristiano", "Mbappé", "Haaland"],
        "Goles": [30, 28, 25, 27],
        "Asistencias": [12, 9, 10, 5],
        "Partidos": [28, 30, 26, 25]
    }
    df_stats = pd.DataFrame(stats)
    jugador1 = df_stats[df_stats["Jugador"] == j1]
    jugador2 = df_stats[df_stats["Jugador"] == j2]

    comparativa = pd.concat([jugador1, jugador2])
    st.dataframe(comparativa.set_index("Jugador"))
