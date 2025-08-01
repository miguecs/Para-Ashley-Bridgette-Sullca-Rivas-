import streamlit as st

st.set_page_config(page_title="Para Ashley", layout="centered")

st.markdown("""
    <!-- Cargar fuente Pacifico para mensaje y botón -->
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <!-- Cargar fuente Caviar Dreams para nombres -->
    <link href="https://fonts.cdnfonts.com/css/caviar-dreams" rel="stylesheet">

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
    .names {
        font-family: 'Caviar Dreams', sans-serif;
        font-size: 4rem;
        color: black;
        max-width: 600px;
        margin: 10px auto;
    }
    /* Para que el nombre de Ashley no haga salto de línea */
    .single-line {
        white-space: nowrap;
    }
    .confirmation-box {
        margin-top: 20px;
        padding: 20px 40px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        font-size: 1.8rem;
        color: black;
        font-family: 'Pacifico', cursive;
        max-width: 400px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        margin-left: auto;
        margin-right: auto;
    }
    div.stButton {
        margin-top: 40px;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        font-size: 24px;
        padding: 15px 50px;
        cursor: pointer;
        border-radius: 20px;
        background-color: #a64ca6;
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

st.markdown('<div class="names">De: Miguel Caso</div>', unsafe_allow_html=True)
st.markdown('<div class="names single-line">Para: Ashley Sullca Rivas</div>', unsafe_allow_html=True)

st.markdown('<div class="confirmation-box">¡Lista Para Empezar!</div>', unsafe_allow_html=True)

if st.button("Comenzar"):
    st.session_state.clicked = True
