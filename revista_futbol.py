import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ELEVEN DATA", layout="wide")

# Inicializar la página
if "page" not in st.session_state:
    st.session_state.page = "portada"

# ------------------ NAVBAR OSCURA ------------------
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        align-items: center;
        background-color: #111;  /* fondo oscuro */
        padding: 10px 30px;
    }
    .navbar img {
        height: 60px;
        cursor: pointer;
        margin-right: 30px;
    }
    .navbar button {
        background: none;
        border: none;
        color: white;
        font-size: 18px;
        font-weight: bold;
        margin-right: 20px;
        cursor: pointer;
    }
    .navbar button:hover {
        color: #00ff99;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,1,8])

with col1:
    if st.button(" ", key="logo_btn"):
        st.session_state.page = "portada"
    st.markdown(
        f"""
        <style>
        div[data-testid="stButton"][key="logo_btn"] button {{
            background: url("https://raw.githubusercontent.com/kekis-aguilar/Data-XI/88f7bfee363408bba592025e74c9ea453148cf95/Eleven_Data.png") no-repeat center;
            background-size: contain;
            height: 60px;
            width: 60px;
            border: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

with col2:
    if st.button("📊 Dashboard"):
        st.session_state.page = "dashboard"

with col3:
    if st.button("⚔️ Comparador"):
        st.session_state.page = "comparador"


# ------------------ CONTENIDO ------------------
if st.session_state.page == "portada":
    st.markdown(
        """
        <h1 style='text-align: center; 
                   font-size: 60px;
                   background: -webkit-linear-gradient(#00ff99, #00ccff);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   font-family: Arial Black, sans-serif;'>
            ELEVEN DATA
        </h1>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center; color: gray;'>Edición Septiembre 2025</h3>", 
        unsafe_allow_html=True
    )

    st.image("https://images.unsplash.com/photo-1521412644187-c49fa049e84d", use_column_width=True)

    st.markdown("""
    <p style='text-align: center; font-size: 20px;'>
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
    ax.bar(df["Jugador"], df["Goles"], color="limegreen")
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
    comparativa = df_stats[df_stats["Jugador"].isin([j1, j2])]
    st.dataframe(comparativa.set_index("Jugador"))
