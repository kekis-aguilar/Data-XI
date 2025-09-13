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
    # Logo clicable (cambia el estado, no abre otra pestaña)
    if st.image(
        "https://raw.githubusercontent.com/kekis-aguilar/Data-XI/88f7bfee363408bba592025e74c9ea453148cf95/Eleven_Data.png",
        width=80,
        caption=" ",  # truco para que no tenga caption
    ):
        st.session_state.page = "portada"

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

    st.image("https://images.unsplash.com/photo-1521412644187-c49fa049e84d", use_column_width=True)

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

elif st.session_state.page == "comparador":
    st.title("⚔️ Comparador de Jugadores")
    jugadores = ["Messi", "Cristiano", "Mbappé", "Haaland"]
    j1 = st.selectbox("Jugador 1", jugadores, index=0)
    j2 = st.selectbox("Jugador 2", jugadores, index=1)
    st.write(f"Comparando **{j1}** vs **{j2}**")

