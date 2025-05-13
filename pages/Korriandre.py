import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Farm Korriandre",
    page_icon="🕷️",
    layout="wide"
)

st.title("🕷️ Farm Korriandre")

# ----------------- PRÉREQUIS -----------------
st.header("Prérequis")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("./spell/peur.png", width=80)
    st.markdown("**Lvl : 6**")

with col2:
    st.image("./spell/coffre.png", width=80)
    st.markdown("**Lvl : 2**")

# ----------------- DESCRIPTION -----------------
st.header("Description")

st.markdown("""
- Bloquer le korriandre dans le coin en base
- Utiliser **Peur** pour le pousser ou **Dispe** si il est sur la case de départ la plus basse
- Utiliser le **Coffre** pour le bloquer
""")

# ----------------- VIDÉO -----------------
st.header("Vidéo")

st.video("https://youtu.be/vvP5knbWTOQ")