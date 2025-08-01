import streamlit as st

st.set_page_config(page_title="Para Ashley", layout="centered")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <link href="https://fonts.cdnfonts.com/css/caviar-dreams" rel="stylesheet">

    <style>
    .stApp {
        background-color: #4b0082;
        color: black;
        font-family: 'Pacifico', cursive;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        height: 100vh;
        margin: 0 20px;
        text-align: center;
        padding-top: 20px;
    }
    .names {
        font-family: 'Caviar Dreams', sans-serif;
        font-size: 4rem;
        color: black;
        max-width: 600px;
        margin: 10px auto;
    }
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
    .audio-player {
        margin-bottom: 30px;
        width: 320px;
    }
    </style>
""", unsafe_allow_html=True)

audio_url = "https://github.com/miguecs/Para-Ashley-Bridgette-Sullca-Rivas-/raw/main/Elvis%20Presley%20-%20Can't%20Help%20Falling%20In%20Love.mp3"

# Música siempre sonando y centrada arriba
st.markdown(f"""
<div class="audio-player">
  <audio autoplay loop controls style="width: 100%;">
    <source src="{audio_url}" type="audio/mpeg">
    Tu navegador no soporta el elemento de audio.
  </audio>
</div>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "start"

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if st.session_state.page == "start":
    st.markdown('<div class="names">De: Miguel Caso</div>', unsafe_allow_html=True)
    st.markdown('<div class="names single-line">Para: Ashley Sullca Rivas</div>', unsafe_allow_html=True)
    st.markdown('<div class="confirmation-box">¡Lista Para Empezar!</div>', unsafe_allow_html=True)
    if st.button("Comenzar"):
        st.session_state.page = "questions"
        st.experimental_rerun()

elif st.session_state.page == "questions":
    st.markdown('<h2 style="color: white;">Quiero conocerte mejor, responde porfa 😊</h2>', unsafe_allow_html=True)

    preguntas = [
        "¿Cuál es tu sueño más grande?",
        "¿Cómo supiste que sí me querías enserio?",
        "¿Por qué conmigo sí quieres hacer las cosas bien?",
        "Para ti, ¿qué es lo que me hace diferente a los demás?",
        "¿Qué te gustaría que supiera sobre ti?"
    ]

    respuestas = []
    for i, pregunta in enumerate(preguntas, 1):
        respuesta = st.text_area(f"Pregunta {i}: {pregunta}", key=f"p{i}")
        respuestas.append(respuesta)

    if st.button("Enviar respuestas") and not st.session_state.submitted:
        st.session_state.submitted = True
        st.success("¡Gracias por compartir conmigo! ❤️")
