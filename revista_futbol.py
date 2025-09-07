import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración
st.set_page_config(page_title="Revista Futbolera", layout="wide")

# Menú lateral (estilo secciones de revista)
menu = st.sidebar.radio("Navegación", ["🏠 Portada", "📊 Dashboard", "⚔️ Comparador"])

# --- Portada ---
if menu == "🏠 Portada":

# Portada mejorada
st.title("⚽ Revista Futbolera")
st.markdown("### Edición Septiembre 2025")
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Soccer_ball.svg", width=200)

st.write("Bienvenido a la revista digital de **análisis estadístico de fútbol**. "
         "Explora comparativas, dashboards y artículos exclusivos sobre el mundo del balompié.")

# Noticias destacadas en columnas
st.subheader("📰 Noticias Destacadas")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/36/Leo_Messi_WC2022.jpg")
    st.markdown("**Messi sigue imparable**")
    st.caption("El astro argentino rompe otro récord histórico en goles y asistencias.")

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg")
    st.markdown("**Cristiano desafía el tiempo**")
    st.caption("A sus 40 años, CR7 sigue demostrando vigencia en la élite.")

with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fc/Kylian_Mbappe_2019.jpg")
    st.markdown("**Mbappé, el heredero**")
    st.caption("El francés lidera la nueva generación y se acerca a la cima mundial.")

# --- Dashboard ---
elif menu == "📊 Dashboard":
    st.title("📊 Dashboard de Estadísticas")

    # Datos ejemplo
    data = {
        "Jugador": ["Messi", "Cristiano", "Mbappé", "Haaland"],
        "Goles": [30, 28, 25, 27],
        "Asistencias": [12, 9, 10, 5],
        "Partidos": [28, 30, 26, 25]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)

    # Gráfica
    st.subheader("Comparativa de Goles")
    fig, ax = plt.subplots()
    ax.bar(df["Jugador"], df["Goles"], color="blue")
    ax.set_ylabel("Goles")
    ax.set_title("Goles por jugador")
    st.pyplot(fig)

# --- Comparador ---
elif menu == "⚔️ Comparador":
    st.title("⚔️ Comparador de Jugadores")

    # Filtros
    jugadores = ["Messi", "Cristiano", "Mbappé", "Haaland"]
    j1 = st.selectbox("Jugador 1", jugadores, index=0)
    j2 = st.selectbox("Jugador 2", jugadores, index=1)

    st.write(f"Comparando **{j1}** vs **{j2}**")

    # Mini análisis ficticio
    st.write("👉 Aquí iría la comparación estadística detallada de ambos jugadores.")
