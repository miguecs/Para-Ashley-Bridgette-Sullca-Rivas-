import streamlit as st

st.set_page_config(page_title="Para Ashley 💖", layout="centered")

# Agregar fuente romántica de Google Fonts y estilos
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background-color: #e6ccff;  /* Morado claro */
        color: black;
        font-family: 'Dancing Script', cursive;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;  /* pantalla completa */
        margin: 0;
    }
    h2 {
        margin: 10px 0;
        font-size: 3rem;
    }
    div.stButton > button {
        font-size: 24px;
        padding: 15px 40px;
        cursor: pointer;
        border-radius: 15px;
        background-color: #d1a3ff;
        border: none;
        color: black;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #b074ff;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2>DE: Miguel Caso Poma</h2>", unsafe_allow_html=True)
st.markdown("<h2>PARA: Ashley Sullca Rivas</h2>", unsafe_allow_html=True)

if st.button("💌 Comenzar"):
    st.success("¡Listo para empezar! ❤️")
