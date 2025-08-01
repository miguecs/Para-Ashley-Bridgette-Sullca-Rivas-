import streamlit as st

st.set_page_config(page_title="Para Ashley 💖", layout="centered")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background-color: #4b0082;  /* morado oscuro */
        color: black;
        font-family: 'Pacifico', cursive;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0 20px;
        text-align: center;
    }
    h2 {
        font-size: 4rem;
        margin: 1rem 0 0.6rem 0; /* más espacio arriba y abajo */
        font-weight: normal;
    }
    .confirmation-box {
        margin-top: 30px;
        padding: 20px 40px;
        background: rgba(255, 255, 255, 0.15); /* cuadro transparente */
        border-radius: 15px;
        font-size: 1.8rem;
        color: black;
        font-family: 'Pacifico', cursive;
        max-width: 400px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    div.stButton {
        margin-top: 50px;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        font-size: 24px;
        padding: 15px 50px;
        cursor: pointer;
        border-radius: 20px;
        background-color: #a64ca6; /* morado medio */
        border: none;
        color: black;
        font-family: 'Pacifico', cursive;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.35);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #8b3d8b;
        color: white;
        transform: scale(1.05);
        box-shadow: 3px 3px 15px rgba(0,0,0,0.45);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2>DE: Miguel Caso Poma</h2>", unsafe_allow_html=True)
st.markdown("<h2>PARA: Ashley Sullca Rivas</h2>", unsafe_allow_html=True)

if "clicked" not in st.session_state:
    st.session_state.clicked = False

if st.button("💌 Comenzar"):
    st.session_state.clicked = True

if st.session_state.clicked:
    st.markdown('<div class="confirmation-box">¡Listo para empezar! ❤️</div>', unsafe_allow_html=True)
