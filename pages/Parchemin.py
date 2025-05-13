import streamlit as st
import pandas as pd
import math

# ---------------- CONFIG PAGE ----------------
st.set_page_config(layout="wide", initial_sidebar_state="collapsed",page_title="Parchemins",page_icon="📜")
# --- nav bar ---

st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #fca311;
            margin-bottom: 0.5rem;
        }
        .sub {
            font-size: 1.3em;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
            color: #ffffff;
        }
        .metric-value {
            font-size: 2.5em !important;
            color: #ffffff !important;
        }
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

# ------------------- OUTIL DE FORMATTAGE -------------------
def fmt(n: int | float) -> str:
    return f"{n:,}".replace(",", " ")  # espace fine insécable U+202F

# ------------------------ TABLE DES PALIERS ----------------
TIERS = pd.DataFrame(
    [
        (   100_000,     10,       1,  "Petit Parchemin"),
        ( 1_000_000,    100,      35,  "Parchemin"),
        (10_000_000,  1_000,     450,  "Grand Parchemin"),
        (100_000_000,10_000,   6_000,  "Puissant Parchemin"),
    ],
    columns=["seuil_max", "cout", "gain", "label"],
)

# ------------------------ FONCTION DE CALCUL ------------------------
@st.cache_data
def calculer_cout_parchemin(niveau_actuel: int, niveau_voulu: int, tiers_df: pd.DataFrame):
    temp = niveau_actuel
    cout_total = 0
    nb_parchemins = {row.label: 0 for row in tiers_df.itertuples()}

    for row in tiers_df.itertuples():
        if temp >= niveau_voulu:
            break
        borne_inf = temp
        borne_sup = min(row.seuil_max - 1, niveau_voulu - 1)
        if borne_inf > borne_sup:
            continue
        stats_a_gagner = borne_sup - borne_inf + 1
        parchemins_utiles = math.ceil(stats_a_gagner / row.gain)

        temp        += parchemins_utiles * row.gain
        cout_total  += parchemins_utiles * row.cout
        nb_parchemins[row.label] += parchemins_utiles

    return cout_total, nb_parchemins

# ------------------- UI ------------------------------------
st.markdown('<div class="main-title">Coût en parchemins</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    niveau_actuel = st.number_input("Stats actuelles :", min_value=0, value=1)
with col2:
    niveau_voulu  = st.number_input("Stats voulues :",  min_value=0, value=1_000_000)

if niveau_voulu <= niveau_actuel:
    st.info("Le niveau voulu doit être supérieur au niveau actuel.")
    st.stop()

cout_total, details = calculer_cout_parchemin(niveau_actuel, niveau_voulu, TIERS)

# ------------------- AFFICHAGE ------------------------------
st.markdown('<div class="sub">📊 Résultat</div>', unsafe_allow_html=True)
st.metric("💰 Coût total (points d'éveil)", fmt(cout_total))

res_df = (
    pd.DataFrame([{"Parchemin": k, "Nombre": v} for k, v in details.items() if v > 0])
      .set_index("Parchemin")
)
res_df["Nombre"] = res_df["Nombre"].apply(fmt)

st.dataframe(res_df, use_container_width=True)

# ------------------- RUNS COMPLETS ------------------------------
def points_par_run(i: int, etage_final: int) -> int:
    return sum(range(i, etage_final + 1))

if cout_total > 0:
    st.markdown('<div class="sub">🧪 Simulation de farm</div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        level_relic = st.number_input("Niveau de la relique actuelle :", min_value=0, max_value=350, value=1)
    with col4:
        idle_etage = st.number_input("Étage Maximum idle :", min_value=0, value=1)

    if level_relic > idle_etage:
        st.info("Le niveau de la relique doit être inférieur ou égal à l'étage maximum.")
        st.stop()

    gain_run = points_par_run(level_relic, idle_etage)
    nb_runs = math.ceil(cout_total / gain_run)
    st.metric("⏳ Nombre de runs complets", fmt(nb_runs))
