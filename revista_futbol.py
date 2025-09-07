import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración
st.set_page_config(page_title="DATA Xl", layout="wide")

# Menú lateral
menu = st.sidebar.radio("Navegación", ["🏠 Portada", "📊 Dashboard", "⚔️ Comparador"])

# ------------------- PORTADA -------------------
if menu == "🏠 Portada":
    # Cabecera estilo revista
    st.markdown(
        "<h1 style='text-align: center; color: darkgreen;'>⚽ Revista Futbolera</h1>", 
        unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: center; color: gray;'>Edición Septiembre 2025</h3>", 
        unsafe_allow_html=True)

    # Hero image
    st.image("https://images.unsplash.com/photo-1521412644187-c49fa049e84d", use_column_width=True)

    # Texto de bienvenida
    st.markdown("""
    <p style='text-align: center; font-size: 18px;'>
    Bienvenido a la revista digital de <b>estadísticas y análisis de fútbol</b>.  
    Explora comparativas, dashboards y artículos exclusivos sobre tus jugadores favoritos.
    </p>
    """, unsafe_allow_html=True)

    # Noticias destacadas en columnas
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

# ------------------- DASHBOARD -------------------
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

    # Tabla interactiva
    st.dataframe(df)

    # Gráfica de barras
    st.subheader("Comparativa de Goles")
    fig, ax = plt.subplots()
    ax.bar(df["Jugador"], df["Goles"], color="blue")
    ax.set_ylabel("Goles")
    ax.set_title("Goles por jugador")
    st.pyplot(fig)

# ------------------- COMPARADOR -------------------
elif menu == "⚔️ Comparador":
    st.title("⚔️ Comparador de Jugadores")

    jugadores = ["Messi", "Cristiano", "Mbappé", "Haaland"]
    j1 = st.selectbox("Jugador 1", jugadores, index=0)
    j2 = st.selectbox("Jugador 2", jugadores, index=1)

    st.write(f"Comparando **{j1}** vs **{j2}**")

    # Datos ejemplo para comparativa
    stats = {
        "Jugador": ["Messi", "Cristiano", "Mbappé", "Haaland"],
        "Goles": [30, 28, 25, 27],
        "Asistencias": [12, 9, 10, 5],
        "Partidos": [28, 30, 26, 25]
    }
    df_stats = pd.DataFrame(stats)
    jugador1 = df_stats[df_stats["Jugador"] == j1]
    jugador2 = df_stats[df_stats["Jugador"] == j2]

    # Mostrar tabla comparativa
    comparativa = pd.concat([jugador1, jugador2])
    st.dataframe(comparativa.set_index("Jugador"))
