import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Para Ashley", layout="centered")

# Inicializar variables de sesión
if "page" not in st.session_state:
    st.session_state.page = "inicio"
if "carta" not in st.session_state:
    st.session_state.carta = None
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# URL de la canción en GitHub (raw)
audio_url = "https://github.com/miguecs/Para-Ashley-Bridgette-Sullca-Rivas-/raw/main/Elvis%20Presley%20-%20Can't%20Help%20Falling%20In%20Love.mp3"

# CSS y estilos generales
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
    /* Centrar audio */
    .audio-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Reproducir música en autoplay y loop (oculto pero centrado)
st.markdown(f"""
    <div class="audio-container">
        <audio autoplay loop controls style="width: 300px;">
          <source src="{audio_url}" type="audio/mpeg">
          Tu navegador no soporta el elemento de audio.
        </audio>
    </div>
""", unsafe_allow_html=True)


# --------- Páginas -----------

if st.session_state.page == "inicio":
    # Página inicial con saludo y botón comenzar
    st.markdown('<div class="names">De: Miguel Caso</div>', unsafe_allow_html=True)
    st.markdown('<div class="names single-line">Para: Ashley Sullca Rivas</div>', unsafe_allow_html=True)
    st.markdown('<div class="confirmation-box">¡Lista Para Empezar!</div>', unsafe_allow_html=True)

    if st.button("Comenzar"):
        st.session_state.page = "preguntas"
        st.experimental_rerun()


elif st.session_state.page == "preguntas":
    # Preguntas para conocerla
    st.markdown('<h2 style="color: white; font-family: Caviar Dreams;">Quiero conocerte mejor</h2>', unsafe_allow_html=True)

    # 5 preguntas con texto inputs
    p1 = st.text_input("¿Cuál es tu canción favorita?", key="p1")
    p2 = st.text_area("¿Cómo supiste que si me querías enserio?", key="p2")
    p3 = st.text_area("¿Por qué conmigo sí quieres hacer las cosas bien?", key="p3")
    p4 = st.text_area("Para ti, ¿qué es lo que me hace diferente a los demás?", key="p4")
    p5 = st.text_input("¿Qué es lo que más te gusta de tu canción favorita?", key="p5")

    if st.button("Enviar respuestas"):
        # Guardar respuestas en estado sesión
        st.session_state.respuestas = {
            "cancion_favorita": p1,
            "como_supo_que_me_queria": p2,
            "por_que_conmigo": p3,
            "que_me_hace_diferente": p4,
            "que_le_gusta_cancion": p5
        }
        st.session_state.page = "gracias"
        st.experimental_rerun()

elif st.session_state.page == "gracias":
    st.success("¡Gracias por compartir conmigo! 💜")

    if st.button("Continuar"):
        st.session_state.page = "gran_mensaje"
        st.experimental_rerun()

elif st.session_state.page == "gran_mensaje":
    st.markdown("""
    <style>
    .final-message {
        font-family: 'Caviar Dreams', sans-serif;
        font-size: 3rem;
        color: white;
        margin-top: 50px;
        line-height: 1.6;
        white-space: pre-line;
    }
    </style>
    <div class="final-message">
        Que eres la mormona que más quiero,\n
        la loca que más adoro\n
        y el ángel que quiero en mi vida.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Continuar"):
        st.session_state.page = "cartas_dia"
        st.experimental_rerun()

elif st.session_state.page == "cartas_dia":
    st.markdown("""
    <h2 style="color: white; font-family: 'Caviar Dreams', sans-serif;">
        💝 Ábrelo el día que...
    </h2>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Si estás triste 😔"):
            st.session_state.carta = "triste"
            st.experimental_rerun()
    with col2:
        if st.button("Si dudas de mí 💭"):
            st.session_state.carta = "duda"
            st.experimental_rerun()
    with col3:
        if st.button("Si quieres recordar que te amo ❤️"):
            st.session_state.carta = "amor"
            st.experimental_rerun()

    # Mostrar carta seleccionada
    if st.session_state.carta:
        st.markdown("""<div style='margin-top:30px; padding: 25px; background: rgba(255,255,255,0.15); 
                        border-radius: 15px; color: white; font-family: "Caviar Dreams", sans-serif; 
                        font-size: 1.4rem; line-height: 1.8;'>""", unsafe_allow_html=True)

        if st.session_state.carta == "triste":
            st.markdown("""
            Si estás triste, quiero que sepas que no estás sola. Puedes contar conmigo, aunque no diga nada, aunque no sepa qué hacer... estaré ahí. No porque tenga que hacerlo, sino porque me nace cuidar de ti. Eres importante, incluso cuando no te sientes así.
            """)
        elif st.session_state.carta == "duda":
            st.markdown("""
            Si alguna vez dudas de mí, recuerda esto: no vine a prometerte perfección, vine a demostrarte constancia. No quiero que me creas por palabras, sino por hechos con el tiempo. Estoy aquí, con la intención más pura que he tenido: hacer las cosas bien contigo.
            """)
        elif st.session_state.carta == "amor":
            st.markdown("""
            Si solo quieres recordar que te amo... entonces aquí va: Te amo con cada cosa buena que tengo. Con cada parte rota que intento sanar. Con cada sueño que nace contigo en mente. Y con todo lo que todavía no sé, pero quiero aprender a tu lado.
            """)

        st.markdown("</div>", unsafe_allow_html=True)
