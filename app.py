import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Para Ashley", layout="centered")

# Fonts + styles
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
    <link href="https://fonts.cdnfonts.com/css/caviar-dreams" rel="stylesheet">

    <style>
    .stApp {
        background-color: #4b0082;
        color: black;
        font-family: 'Pacifico', cursive;
        text-align: center;
        padding-top: 30px;
    }
    .names {
        font-family: 'Caviar Dreams', sans-serif;
        font-size: 4rem;
        color: black;
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
        margin-left: auto;
        margin-right: auto;
    }
    .audio-player {
        margin: 30px auto;
        width: 320px;
    }
    .love-message {
        font-size: 1.6rem;
        color: white;
        max-width: 750px;
        margin: 30px auto;
        line-height: 1.7;
        font-family: 'Caviar Dreams', sans-serif;
    }
    .final-message {
        font-family: 'Caviar Dreams', sans-serif;
        font-size: 3.5rem;
        color: white;
        margin-top: 80px;
        line-height: 1.6;
    }
    .card-button {
        font-size: 1.4rem;
        padding: 12px 25px;
        margin: 15px 10px;
        border-radius: 15px;
        background-color: #a64ca6;
        color: black;
        border: none;
        font-family: 'Pacifico', cursive;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.35);
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .card-button:hover {
        background-color: #8b3d8b;
        color: white;
        transform: scale(1.05);
    }
    .card-message {
        background: rgba(255, 255, 255, 0.15);
        color: white;
        padding: 20px 30px;
        border-radius: 20px;
        max-width: 700px;
        margin: 30px auto;
        font-family: 'Caviar Dreams', sans-serif;
        font-size: 1.5rem;
        line-height: 1.6;
    }
    div.stButton {
        margin-top: 40px;
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        font-size: 20px;
        padding: 15px 40px;
        border-radius: 20px;
        background-color: #a64ca6;
        color: black;
        border: none;
        font-family: 'Pacifico', cursive;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.35);
    }
    div.stButton > button:hover {
        background-color: #8b3d8b;
        color: white;
        transform: scale(1.05);
        transition: 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Música
audio_url = "https://github.com/miguecs/Para-Ashley-Bridgette-Sullca-Rivas-/raw/main/Elvis%20Presley%20-%20Can't%20Help%20Falling%20In%20Love.mp3"
st.markdown(f"""
<div class="audio-player">
  <audio autoplay loop controls style="width: 100%;">
    <source src="{audio_url}" type="audio/mpeg">
    Tu navegador no soporta el elemento de audio.
  </audio>
</div>
""", unsafe_allow_html=True)

# Estado inicial
if 'page' not in st.session_state:
    st.session_state.page = "inicio"
if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

# Navegación entre páginas
if st.session_state.page == "inicio":
    st.markdown('<div class="names">De: Miguel Caso</div>', unsafe_allow_html=True)
    st.markdown('<div class="names single-line">Para: Ashley Sullca Rivas</div>', unsafe_allow_html=True)
    st.markdown('<div class="confirmation-box">¡Lista Para Empezar!</div>', unsafe_allow_html=True)

    if st.button("Comenzar"):
        st.session_state.page = "preguntas"

elif st.session_state.page == "preguntas":
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

    if st.button("Enviar respuestas"):
        st.session_state.page = "carta"

        # Guardar en CSV
        df = pd.DataFrame({
            "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "pregunta_1": [respuestas[0]],
            "pregunta_2": [respuestas[1]],
            "pregunta_3": [respuestas[2]],
            "pregunta_4": [respuestas[3]],
            "pregunta_5": [respuestas[4]],
        })

        if os.path.exists("respuestas.csv"):
            df.to_csv("respuestas.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("respuestas.csv", index=False)

elif st.session_state.page == "carta":
    st.success("¡Gracias por compartir conmigo! ❤️")

    if st.button("Continuar"):
        st.session_state.page = "mensaje_final"

elif st.session_state.page == "mensaje_final":
    st.markdown(f"""
    <div class="love-message">
        <p>Ashley:</p>
        <p>No estás leyendo cualquier carta, estás leyendo un pedacito de lo que hay dentro de mí.</p>
        <p>Quiero que sepas algo: no importa cuánto tiempo pase, si tengo que esperar años o incluso décadas, lo haré. Porque tú vales eso y mucho más.</p>
        <p>Quiero ser alguien que te acompañe en lo bueno y lo difícil. No porque sea perfecto, sino porque mi intención contigo es verdadera. Quiero cuidarte, con paciencia, con respeto, y sobre todo, con amor.</p>
        <p>Sé que las palabras pueden ser bonitas, pero mis acciones con el tiempo quiero que las respalden. Estoy aquí para ti. Siempre.</p>
        <p>— Miguel</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Ver algo más bonito ❤️"):
        st.session_state.page = "gran_mensaje"

elif st.session_state.page == "gran_mensaje":
    st.markdown(f"""
    <div class="final-message">
        Que eres la mormona que más quiero,<br>
        la loca que más adoro<br>
        y el ángel que quiero en mi vida.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Ábrelo el día que..."):
        st.session_state.selected_card = None
        st.session_state.page = "cartas_abrelo"

elif st.session_state.page == "cartas_abrelo":
    st.markdown('<h2 style="color: white; font-family: Caviar Dreams, sans-serif;">Ábrelo el día que...</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Estés triste 😔"):
            st.session_state.selected_card = "triste"
    with col2:
        if st.button("Dudes de mí 💭"):
            st.session_state.selected_card = "dudas"
    with col3:
        if st.button("Quieras recordar que te amo ❤️"):
            st.session_state.selected_card = "amo"

    # Mostrar mensaje según botón elegido
    if st.session_state.selected_card == "triste":
        st.markdown("""
        <div class="card-message">
            <p>Mi amor, si estás triste, recuerda que después de la tormenta siempre llega la calma. Estoy aquí para ti, aunque no lo veas, siempre te estoy cuidando con mi amor infinito.</p>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.selected_card == "dudas":
        st.markdown("""
        <div class="card-message">
            <p>Cuando dudes de mí, mira hacia atrás y ve todo lo que hemos vivido, lo mucho que he dado y lo sincero que soy. Confía en que mi amor por ti es verdadero y sin condiciones.</p>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.selected_card == "amo":
        st.markdown("""
        <div class="card-message">
            <p>Si quieres recordar que te amo, mira este mensaje y siente mi corazón latiendo por ti. Eres mi vida, mi alegría, y mi todo.</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Ver mi promesa para ti"):
        st.session_state.page = "promesa"

elif st.session_state.page == "promesa":
    st.markdown("""
    <div class="card-message" style="background: rgba(255, 255, 255, 0.25); color: white;">
        <p><strong>Mi promesa para ti, Ashley:</strong></p>
        <p>Prometo estar a tu lado en cada paso, en cada sonrisa y en cada lágrima. Mi amor será constante, paciente y sincero.</p>
        <p>Quiero construir contigo un camino lleno de confianza, respeto y alegría. Eres mi prioridad, hoy y siempre.</p>
        <p>Te amo con todo mi corazón.</p>
        <p>— Miguel</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Volver al mensaje final"):
        st.session_state.page = "mensaje_final"
