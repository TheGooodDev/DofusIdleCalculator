import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="Accueil - Dofus IDLE Flemme",
    page_icon="🧙‍♂️",
    layout="centered",
    initial_sidebar_state="auto"
)

# Affichage du titre avec un style personnalisé
st.markdown(
    """
    <style>
    .main {
        background-color: #1e1e1e;
        color: #f0f0f0;
        text-align: center;
    }
    h1 {
        font-size: 3em;
        color: #fca311;
    }
    .intro {
        font-size: 1.2em;
        margin-top: 1em;
        color: #dcdcdc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1>Dofus IDLE Flemme</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="intro">Si t\'as la flemme de sortir une calculette, ou que ton Excel met trop de temps à s\'ouvrir.</p>',
    unsafe_allow_html=True
)
