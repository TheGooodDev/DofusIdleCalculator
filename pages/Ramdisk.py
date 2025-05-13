import streamlit as st

# --- nav bar ---
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
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
st.title("🚀 Booster Dofus grâce au Ramdisk")
st.header("1. Secret professionnel")

# st.header("1. Pourquoi utiliser un Ramdisk ?")
# st.markdown("""
# Chargement instantanément. Plus de freezes relous, et en prime, tu économises la vie de ton SSD.
# """)

# st.header("2. Pré-requis")
# st.markdown("""
# - Windows 10 ou 11
# - 16 Go de RAM minimum (32 c’est mieux)
# - Le logiciel : [ImDisk Toolkit](https://sourceforge.net/projects/imdisk-toolkit/) (Gratuit)
# """)

# st.header("3. Installation et configuration du Ramdisk")
# st.subheader("Étape 1 : Installer ImDisk Toolkit")
# st.markdown("Télécharge le lien juste au-dessus et installe.")

# st.subheader("Étape 2 : Créer un Ramdisk")
# st.code("""
# - Lance ImDisk « ImDisk Virtual Disk Driver ».
# - Clique sur « Mount new ».
# - Réglages conseillés :
#   - Taille : 8 Go
#   - Lettre : R:
#   - Système : NTFS
#   - Décoche tout ce qui est sauvegarde auto
# - Et valide.
# """, language='text')

# st.image("./img.png", caption="Configuration du Ramdisk avec ImDisk Toolkit")
# st.image("./img2.png", caption="Formater le disque Ram avec le système de fichiers NTFS")

# st.markdown("""
# ⚠️ **Attention si t'as pas beaucoup de RAM** :
# Créer un Ramdisk réserve une partie de ta mémoire vive. Donc si t'as seulement 8 ou 12 Go, le reste de ton système et tes applis peuvent galérer. Ton PC risque de swapper, ramer, ou planter si t'abuses. Si t’es juste niveau RAM, vaut mieux éviter ou mettre une petite taille de disque virtuel (genre 2 ou 4 Go max).
# """)


# st.header("4. Déplacement du cache de Dofus vers le Ramdisk")
# st.code("""
# - Trouve ton cache : C:\\Users\\TonNom\\AppData\\Roaming\\Dofus
# - Crée un dossier R:\\DofusCache
# - Colle tout ton cache dedans
# - Renomme ou vire l’ancien dossier cache
# - Fais un lien symbolique :

# mklink /D "C:\\Users\\TonNom\\AppData\\Roaming\\Dofus" "R:\\DofusCache"
# """, language='cmd')

# st.header("5. Automatisation (optionnelle mais utile)")
# st.markdown("Mets ça dans un fichier `Start-Dofus.ps1` :")
# st.code("""
# $ramdiskPath = "R:\\DofusCache"
# $symlinkPath = "$env:APPDATA\\Dofus"
# $backupCache = "D:\\DofusCacheBackup"

# if (!(Test-Path "R:\")) {
#     Write-Host "Oups, le ramdisk est pas monté." -ForegroundColor Red
#     exit
# }

# if (!(Test-Path $ramdiskPath)) {
#     New-Item -ItemType Directory -Path $ramdiskPath
#     if (Test-Path $backupCache) {
#         Copy-Item "$backupCache\\*" -Destination $ramdiskPath -Recurse
#     }
# }

# if (!(Test-Path $symlinkPath)) {
#     cmd /c mklink /D "$symlinkPath" "$ramdiskPath"
# }

# Start-Process "C:\\CheminVersDofus\\Dofus.exe"
# """, language='powershell')

# st.header("6. Vérification")
# st.markdown(r"""
# - Vérifie que ton Ramdisk (`R:`) est bien là
# - Check ton lien symbolique :
#   ```
#   C:\Users\TonNom\AppData\Roaming\Dofus
#   ```
# - Lance Dofus, vois si ça tourne vite et si des fichiers apparaissent dans `R:\DofusCache`
# """)

# st.header("7. Sauvegarde du cache initial (optionnelle)")
# st.markdown("Une fois que t’as joué un peu, pense à sauvegarder ton cache:")
# st.code("""
# Copie R:\\DofusCache vers D:\\DofusCacheBackup
# """, language='cmd')

# st.success("Voilà, maintenant ton Dofus tourne comme une balle !")
