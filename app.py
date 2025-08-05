import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Para Ashley", layout="centered")

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

audio_url = "https://github.com/miguecs/Para-Ashley-Bridgette-Sullca-Rivas-/raw/main/Elvis%20Presley%20-%20Can't%20Help%20Falling%20In%20Love.mp3"
st.markdown(f"""
<div class="audio-player">
  <audio autoplay loop controls style="width: 100%;">
    <source src="{audio_url}" type="audio/mpeg">
    Tu navegador no soporta el elemento de audio.
  </audio>
</div>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "inicio"
if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

if st.session_state.page == "inicio":
    st.markdown('<div class="names">De: Miguel Caso</div>', unsafe_allow_html=True)
    st.markdown('<div class="names single-line">Para: Ashley Sullca Rivas</div>', unsafe_allow_html=True)
    st.markdown('<div class="confirmation-box">¡Lista Para Empezar!</div>', unsafe_allow_html=True)

    if st.button("💌Comenzar💌"):
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
    st.success("❤️¡Gracias por compartir conmigo!❤️")

    if st.button("Continuar"):
        st.session_state.page = "mensaje_final"

elif st.session_state.page == "mensaje_final":
    st.markdown(f"""
    <div class="love-message">
        <p>Ashley:</p>
        <p>No estás leyendo cualquier carta, estás leyendo un pedacito de lo que hay dentro de mí.</p>
        <p>Quiero que sepas algo, no importa cuánto tiempo pase, si tengo que esperar años o incluso décadas, lo haré. Porque tú vales eso y mucho más.</p>
        <p>Quiero ser alguien que te acompañe en lo bueno y lo difícil. No porque sea perfecto, sino porque mi intención contigo es verdadera. Quiero cuidarte, con paciencia, con respeto, y sobre todo, con amor.</p>
        <p>Sé que las palabras pueden ser bonitas, pero mis acciones con el tiempo quiero que las respalden. Estoy aquí para ti. Siempre.</p>
        <p> Miguel Caso</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Ver algo más bonito 🎁"):
        st.session_state.page = "gran_mensaje"

elif st.session_state.page == "gran_mensaje":
    st.markdown(f"""
    <div class="final-message">
        ¡QUE ERES LA MORMONA QUE MÁS QUIERO,<br>
        LA LOCA QUE MÁS ADORO<br>
        Y EL ÁNGEL QUE QUIERO EN MI VIDA!
    </div>
    """, unsafe_allow_html=True)

    if st.button("Ábrelo el día que..."):
        st.session_state.selected_card = None
        st.session_state.page = "cartas_abrelo"

elif st.session_state.page == "cartas_abrelo":
    st.markdown('<h2 style="color: white; font-family: Caviar Dreams, sans-serif;">Ábrelo el día que...</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Estés Triste 😔"):
            st.session_state.selected_card = "triste"
    with col2:
        if st.button("Dudes de Mí 🤔"):
            st.session_state.selected_card = "dudas"
    with col3:
        if st.button("Quieras Recordar que Te Amo ❤️"):
            st.session_state.selected_card = "amo"


    if st.session_state.selected_card == "triste":
        st.markdown("""
        <div class="card-message">
            <p>Sé que ahora puede que te sientas triste, pero quiero que recuerdes algo muy importante, nunca estarás sola. Siempre estaré aquí, a tu lado, para apoyarte, escucharte y ofrecerte todo mi amor. Las dificultades pueden parecer grandes en este momento, pero quiero que sepas que juntos podemos enfrentarlas. Mi hombro estará siempre disponible, y mi corazón, siempre contigo. Te amo, y no importa lo que pase, siempre estaré para ti..</p>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.selected_card == "dudas":
        st.markdown("""
        <div class="card-message">
            <p>Cuando sientas dudas, quiero que mires atrás y veas todo lo que hemos construido juntos, cada momento que hemos compartido, cada sacrificio que he hecho por ti. Verás lo mucho que te he dado, lo sincero que siempre he sido y cómo mi amor por ti no tiene límites ni condiciones. Confía en lo que somos, porque lo que siento por ti es verdadero, profundo y eterno. Siempre estaré aquí, a tu lado, sin importar lo que pase.</p>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.selected_card == "amo":
        st.markdown("""
        <div class="card-message">
            <p>Si alguna vez te sientes perdida o sola, recuerda estas palabras y deja que mi amor te envuelva. Cada letra lleva mi corazón latiendo por ti, cada palabra es un pedazo de lo que eres para mí. Eres mi razón, mi sol en los días grises, mi alegría infinita. No hace falta que busques más pruebas de lo que significas para mí, porque tú eres mi vida, mi todo, y siempre serás lo más importante de mi mundo.</p>
        </div>
        """, unsafe_allow_html=True)

    if st.button("🌹Ver Mi Promesa Para Ti🌹"):
        st.session_state.page = "promesa"

elif st.session_state.page == "promesa":
    st.markdown("""
    <div class="card-message">
        <p>Querida Ashley,</p>
        <p>Te hago esta promesa con todo mi corazón:</p>
        <p>Prometo estar a tu lado en cada paso, en las alegrías y en las dificultades, sin importar el tiempo que pase.</p>
        <p>Te brindaré paciencia, respeto y amor sincero, cuidando siempre de ti y de nuestro vínculo.</p>
        <p>Prometo ser honesto y esforzarme cada día para construir juntos un futuro lleno de felicidad y sueños cumplidos.</p>
        <p>No importa cuántos años o décadas pasen, mi compromiso contigo es eterno.</p>
    </div>
    """, unsafe_allow_html=True)

        
    st.markdown("### 🤨 Botón para Descifrar 🤨")

    with st.form("descifrar_form"):
        fecha_input = st.text_input("Introduce la fecha importante (Pista: 5:00 am) (Formato: DD-MM-AAAA)")
        submitted = st.form_submit_button("😨 Descifrar 😨")

        if submitted:
            if fecha_input.strip() == "24-01-2022":
                st.success("¡Fecha correcta! Aquí tienes tu mensaje especial:")
                st.markdown("""
                <div class="card-message">
                    <p>Ese día comenzó todo... El inicio de lo que para mí es lo más bonito que he vivido.</p>
                    <p>Desde ese 24 de enero, no hay un solo día en el que no haya pensado en ti, en cómo has transformado mi vida y en cómo quiero seguir construyendo algo eterno contigo.</p>
                    <p>Gracias por existir. Gracias por quedarte. ❤️ Te amo con todo mi corazón, Ashley ❤️.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Fecha incorrecta. Intenta de nuevo con la fecha que marcó un antes y un después.")

    if st.button("🌹 Volver al Mensaje Bonito 🌹"):
        st.session_state.page = "gran_mensaje"

    if st.button("Finalizar Recorrido"):
        st.session_state.page = "final_final"


elif st.session_state.page == "final_final":
    st.markdown("""
    <div class="final-message">
        GRACIAS POR LLEGAR HASTA AQUÍ ❤️<br>
        ESTE ES EL FINAL DE ESTE PEQUEÑO REGALO,<br>
        PERO NO EL FINAL DE TODO LO QUE QUIERO CONTIGO.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="love-message">
        <p>Gracias por tomarte el tiempo de leer cada palabra, responder con sinceridad, y llegar hasta aquí.</p>
        <p>Todo esto lo hice desde el corazón, porque tú, Ashley, eres la persona que más quiero en este mundo.</p>
        <p>Esto no termina aquí, nuestro viaje apenas comienza. </p>
        <p><strong> Miguel Caso 💌</strong></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🌹 Volver a las cartas 🌹"):
        st.session_state.page = "cartas_abrelo"
        st.session_state.selected_card = None
