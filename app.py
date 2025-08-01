import streamlit as st

# Configurar la página
st.set_page_config(page_title="Para Ashley 💖", layout="centered")

# Controlador de páginas
if 'page' not in st.session_state:
    st.session_state.page = 1

# Estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #e6ccff; /* Morado claro */
        font-family: 'Segoe UI', sans-serif;
        padding-top: 50px;
        color: black;
    }
    h1, h2, h3, h4, p {
        color: black !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- PÁGINA 1: PRESENTACIÓN -----------
if st.session_state.page == 1:
    st.markdown("<h2>DE: Miguel Caso Poma</h2>", unsafe_allow_html=True)
    st.markdown("<h2>PARA: Ashley Sullca Rivas</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💌 Comenzar"):
        st.session_state.page = 2
        st.experimental_rerun()

# ----------- PÁGINA 2: CARTA -----------
elif st.session_state.page == 2:
    st.markdown("### 💖 Carta para ti, Ashley:")
    st.markdown("""
    No sé cómo decirte esto en persona, así que decidí hacerlo de una forma especial.

    Desde que te conozco, algo en mí cambió. Tu forma de ser, tu sonrisa, tu energía… todo eso me hace sentir diferente.

    No somos nada (todavía), pero eres muchísimo para mí.

    No espero nada, ni te pongo presión... solo quería que supieras que me importas de verdad.

    Quiero estar para ti, cuando sonrías, cuando estés mal, cuando simplemente necesites a alguien.

    No es una declaración dramática. Solo quería abrirte mi corazón.

    Y si en algún momento llegas a sentir algo parecido... aquí estaré. 🌷
    """)
    st.image("https://i.pinimg.com/originals/ba/b9/2f/bab92f94a035e78c81ab3b6cf7d7d542.gif", width=300)

    if st.button("➡️ Siguiente"):
        st.session_state.page = 3
        st.experimental_rerun()
