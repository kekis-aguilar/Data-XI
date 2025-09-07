import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración
st.set_page_config(page_title="Revista Futbolera", layout="wide")

# Menú lateral (estilo secciones de revista)
menu = st.sidebar.radio("Navegación", ["🏠 Portada", "📊 Dashboard", "⚔️ Comparador"])

# --- Portada ---
if menu == "🏠 Portada":
    st.title("⚽ Revista Futbolera")
    st.subheader("Edición Digital")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Soccer_ball.svg", width=150)

    st.write("""
    Bienvenido a la revista digital de **estadísticas futboleras**.  
    Aquí encontrarás análisis, comparativas y visualizaciones interactivas sobre tus jugadores favoritos.
    """)

    st.markdown("### 📰 Última Noticia")
    st.write("Messi y Cristiano siguen rompiendo récords. ¿Quién es el verdadero GOAT? Aquí analizamos sus números…")

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