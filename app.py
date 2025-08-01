import streamlit as st

st.set_page_config(page_title="Para Ashley 💖", layout="centered")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background-color: #4b0082;  /* morado oscuro */
        color: black;
        font-family: 'Dancing Script', cursive;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        text-align: center;
        padding: 0 20px;
    }
    h2 {
        font-size: 3.5rem;
        margin: 0.3rem 0;
        font-weight: 700;
        color: black;
        text-shadow: 1px 1px 2px #c8a2c8;
    }
    div.stButton > button {
        font-size: 24px;
        padding: 15px 40px;
        cursor: pointer;
        border-radius: 15px;
        background-color: #a64ca6; /* morado medio */
        border: none;
        color: black;
        transition: background-color 0.3s ease;
        margin-top: 30px;
        font-family: 'Dancing Script', cursive;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }
    div.stButton > button:hover {
        background-color: #8b3d8b;
        color: white;
    }
    .confirmation-box {
        margin-top: 30px;
        padding: 20px 40px;
        background: rgba(255, 255, 255, 0.2); /* transparente blanco suave */
        border-radius: 15px;
        font-size: 1.8rem;
        color: black;
        font-family: 'Dancing Script', cursive;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        max-width: 400px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2>DE: Miguel Caso Poma</h2>", unsafe_allow_html=True)
st.markdown("<h2>PARA: Ashley Sullca Rivas</h2>", unsafe_allow_html=True)

if st.button("💌 Comenzar"):
    st.markdown('<div class="confirmation-box">¡Listo para empezar! ❤️</div>', unsafe_allow_html=True)
