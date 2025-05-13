import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Accueil - Dofus IDLE Flemme",
    page_icon="🧙‍♂️",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- nav bar ---
st.markdown("""
    <style>
        /* Barre latérale */
        section[data-testid="stSidebar"] {
            background-color: #1c1c2e;
            padding: 1.5rem 1rem;
        }

        /* Titres de pages */
        .css-17eq0hr {
            font-weight: bold;
            color: #fca311;
        }

        /* Lien de page */
        .css-1d391kg a {
            color: #ffffff !important;
            text-decoration: none;
            font-size: 1rem;
            padding: 0.4rem 0.8rem;
            display: block;
            border-radius: 0.5rem;
        }

        /* Lien actif */
        .css-1d391kg .css-1v3fvcr {
            background-color: #3c3c5e !important;
        }

        /* Au survol */
        .css-1d391kg a:hover {
            background-color: #2a2a40;
        }

        /* Espacement pour la lisibilité */
        .css-1d391kg {
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Style custom ---
st.markdown("""
    <style>
        html, body {
            background-color: #0e0e11;
        }

        .main-title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            color: #fca311;
            margin-top: 2rem;
        }

        .intro {
            text-align: center;
            font-size: 1.1em;
            margin-bottom: 2rem;
            color: #ccc;
        }

        .category-title {
            font-size: 1.5em;
            font-weight: bold;
            color: #fca311;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
        }

        .st-emotion-cache-1v0mbdj, .st-emotion-cache-1c7y2kd {
            margin-left: 1.2rem;
        }

        .st-emotion-cache-1v0mbdj a, .st-emotion-cache-1c7y2kd a {
            font-size: 1.05em;
        }
    </style>
""", unsafe_allow_html=True)

# --- Titre & description ---
st.markdown('<div class="main-title">Dofus IDLE Flemme</div>', unsafe_allow_html=True)
st.markdown('<div class="intro">Si t\'as la flemme de sortir une calculette, ou que ton Excel met trop de temps à s\'ouvrir.</div>', unsafe_allow_html=True)

# --- Catégories & liens ---
st.markdown('<div class="category-title">🧰 Outils</div>', unsafe_allow_html=True)
st.page_link("pages/Parchemin.py", label="📜 Parchemin")
st.page_link("pages/Rentabilite_Relique.py", label="📦 Rentabilité Relique")

st.markdown('<div class="category-title">⚙️ Optimisation</div>', unsafe_allow_html=True)
st.page_link("pages/Ramdisk.py", label="🚀 Ramdisk")

st.markdown('<div class="category-title">💰 Farm Donjons</div>', unsafe_allow_html=True)
st.page_link("pages/Korriandre.py", label="🕷️ Korriandre")
# Ajoute d'autres pages ici si nécessaire
