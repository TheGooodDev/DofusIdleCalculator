import streamlit as st
import pandas as pd
import math

###################################
# 1) Chargement des données Excel
###################################
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)

df = load_data("Classeur1.xlsx")

###################################
# 2) Fonctions de calcul
###################################
def sum_of_integers(a, b):
    """Somme des entiers de a à b (inclus). Si b < a, renvoie 0."""
    if b < a:
        return 0
    return (b - a + 1) * (a + b) // 2

def points_par_run(palier_debut, etage_final):
    """Calcule la somme des étages de palier_debut à etage_final (inclus)."""
    return sum_of_integers(palier_debut, etage_final)

def temps_run(palier_debut, etage_final, vitesse):
    """
    Calcule la durée (en minutes) pour parcourir
    les étages de palier_debut à etage_final,
    à raison de `vitesse` étages/minute.
    """
    if etage_final < palier_debut:
        return 0
    nb_etages = etage_final - palier_debut + 1
    return nb_etages / vitesse

###################################
# 3) Interface Streamlit
###################################
st.title("Calcul de rentabilité de la relique d'éveil")

st.markdown("""
Cette application vous permet :
- De saisir votre **niveau actuel de relique** (1..200).
- De saisir votre **vitesse** (étages / minute).
- D'obtenir, pour chaque palier (1..200) :
  - Le coût cumulé (à partir de 0).
  - Le **coût d'amélioration** depuis votre relique actuelle.
  - Les points gagnés sur un run.
  - Le temps par run.
  - Les points/minute.
  - Le nombre de runs en 3h.
  - Le total de points en 3h.
  - Le **Gain (%)** par rapport au palier 1 sur 3h (en nombre de points cumulés).
""")

# Input: Niveau actuel de la relique
current_relic_level = st.number_input(
    "Niveau actuel de la relique (entre 1 et 200) :",
    min_value=1,
    max_value=200,
    value=1
)

# Input: Étage final
etage_final = st.number_input(
    "Étage final (là où vous mourrez) :",
    min_value=1,
    value=200
)

# Input: Vitesse (étages/minute)
vitesse = st.number_input(
    "Vitesse (étages / minute) :",
    min_value=1,
    value=7
)

st.write(f"Durée totale considérée pour le 'Gain (%)' : **3 heures** (180 minutes).")

###################################
# 4) Calcul de référence (Palier 1)
###################################
time_run_current = temps_run(current_relic_level, etage_final, vitesse)
points_run_current = points_par_run(current_relic_level, etage_final)

if time_run_current > 0:
    nb_runs_current = math.floor(180 / time_run_current)
    temps_utilise_current = nb_runs_current * time_run_current
    temps_restant_current = 180 - temps_utilise_current
    # Calcul des étages franchis dans le run partiel
    etages_supp_current = int(temps_restant_current * vitesse)
    etage_debut_partiel_current = current_relic_level
    etage_fin_partiel_current = min(current_relic_level + etages_supp_current - 1, etage_final)
    points_partiel_current = sum_of_integers(etage_debut_partiel_current, etage_fin_partiel_current)
    points_current_3h = nb_runs_current * points_run_current + points_partiel_current
else:
    points_current_3h = 0

###################################
# 5) Récupérer le coût cumulé du niveau actuel de la relique
###################################
cost_current_relic = df.loc[df["Etage"] == current_relic_level, "Cout Cumulé"].iloc[0]

###################################
# 6) Calcul pour chaque palier (1..200)
###################################
results = []
for i in range(1, 201):
    cost_i = df.loc[df["Etage"] == i, "Cout Cumulé"].iloc[0]

    if i <= current_relic_level:
        cost_upgrade = 0
    else:
        cost_upgrade = cost_i - cost_current_relic

    pts_run_i = points_par_run(i, etage_final)
    t_run_i = temps_run(i, etage_final, vitesse)

    # Nombre de runs complets dans 3h
    if t_run_i > 0:
        nb_runs_i = math.floor(180 / t_run_i)
        temps_utilise = nb_runs_i * t_run_i
        temps_restant = 180 - temps_utilise

        # Étages partiels possibles dans le temps restant
        etages_supp = int(temps_restant * vitesse)
        etage_debut_partiel = i
        etage_fin_partiel = min(i + etages_supp - 1, etage_final)
        points_partiel = sum_of_integers(etage_debut_partiel, etage_fin_partiel)
    else:
        nb_runs_i = 0
        points_partiel = 0

    total_pts_i_3h = nb_runs_i * pts_run_i + points_partiel

    # Gain % comparé à la relique actuelle
    if points_current_3h > 0:
        gain_percent = ((total_pts_i_3h - points_current_3h) / points_current_3h) * 100
    else:
        gain_percent = 0

    ratio_pm = pts_run_i / t_run_i if t_run_i > 0 else 0

    results.append({
        "Palier": i,
        "Coût Cumulé (abs.)": cost_i,
        "Coût d'Amélioration (depuis relique actuelle)": cost_upgrade,
        "Points/run": pts_run_i,
        "Temps/run (min)": round(t_run_i, 2),
        "Pts/min (run)": round(ratio_pm, 2),
        "Runs (3h)": nb_runs_i,
        "Points partiels (résiduels)": points_partiel,
        "Points (3h)": total_pts_i_3h,
        "Gain (%) vs. Relique Actuelle": round(gain_percent, 2)
    })

df_results = pd.DataFrame(results)

###################################
# 7) Affichage
###################################
st.subheader("Tableau de rentabilité")

st.dataframe(df_results, use_container_width=True)

st.markdown("""
**Remarques :**
- **Coût Cumulé (abs.)** : somme totale nécessaire pour débloquer ce palier depuis le niveau 0 (non évolué).
- **Coût d'Amélioration (depuis relique actuelle)** : ce que vous devez payer **réellement** si vous êtes déjà au **Niveau actuel**.
- Les colonnes "Points (3h)" et "Gain (%) vs. Palier 1" se basent sur une session théorique de 3h, 
  enchaînant les runs (sans compter le temps résiduel s'il reste quelques minutes après le dernier run entier).
- Le **Gain (%)** compare le total de points d'un palier i avec le total de points gagné en restant à **palier 1**.
""")
