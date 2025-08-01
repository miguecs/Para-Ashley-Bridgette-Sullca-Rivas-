import streamlit as st

st.set_page_config(page_title="Para Ashley", layout="centered")

# Cambia por el enlace real donde alojas la canción
audio_url = "https://tu-repositorio.com/cant_help_falling_in_love.mp3"

# Mostrar botón para reproducir música
if "music_playing" not in st.session_state:
    st.session_state.music_playing = False

def play_music():
    st.session_state.music_playing = True

st.markdown("""
    <!-- Fuentes y estilos omitidos para simplificar -->
""", unsafe_allow_html=True)

st.markdown('<div class="names">De: Miguel Caso</div>', unsafe_allow_html=True)
st.markdown('<div class="names single-line">Para: Ashley Sullca Rivas</div>', unsafe_allow_html=True)

st.markdown('<div class="confirmation-box">¡Lista Para Empezar!</div>', unsafe_allow_html=True)

if st.button("Comenzar"):
    st.session_state.clicked = True

if not st.session_state.music_playing:
    if st.button("▶️ Reproducir música"):
        play_music()

if st.session_state.music_playing:
    st.audio(audio_url, format='audio/mp3', start_time=0)
