import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Para Ashley 💖", layout="centered")

# Ocultar el menú y pie de página de Streamlit
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background-color: #ffe6f0; /* fondo rosa claro */
        padding-top: 100px;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Mostrar encabezado
st.markdown("<h2 style='text-align: center;'>DE: Miguel Caso Poma</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>PARA: Ashley Sullca Rivas</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Botón de comenzar
if st.button("💌 Comenzar"):
    st.session_state.comenzar = True

# Cuando se presiona "comenzar", pasamos al contenido principal
if 'comenzar' in st.session_state and st.session_state.comenzar:
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>Bienvenida, esta app es para ti 💖</h3>", unsafe_allow_html=True)
    st.markdown("Aquí irá el contenido de la carta, test, imágenes, etc.")
