import streamlit as st

# Configuración
st.set_page_config(page_title="Revista Futbolera", layout="wide")

# Menú lateral
menu = st.sidebar.radio("Navegación", ["🏠 Portada", "📊 Dashboard", "⚔️ Comparador"])

# --- Portada ---
if menu == "🏠 Portada":
    # Cabecera tipo magazine
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

    # Noticias destacadas en columnas estilo tarjetas
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
