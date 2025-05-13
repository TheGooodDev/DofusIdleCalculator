import streamlit as st

def custom_sidebar():
    st.markdown("""
        <style>
            body {
                overflow-x: hidden;
            }

            .custom-sidebar {
                position: fixed;
                top: 0;
                left: 0;
                width: 240px;
                height: 100vh;
                background-color: #1c1c2e;
                padding: 2rem 1rem;
                color: white;
                z-index: 100;
            }

            .custom-sidebar h2 {
                font-size: 1.2em;
                margin-bottom: 0.5rem;
                color: #fca311;
            }

            .custom-sidebar a {
                display: block;
                color: #f0f0f0;
                text-decoration: none;
                margin: 6px 0;
                padding: 6px 12px;
                border-radius: 6px;
                transition: 0.2s;
            }

            .custom-sidebar a:hover {
                background-color: #2e2e4e;
            }

            .main-content {
                margin-left: 260px;
                padding: 2rem;
            }
        </style>

        <div class="custom-sidebar">
            <h2>🧰 Outils</h2>
            <a href="Parchemin" target="_self">📜 Parchemin</a>
            <a href="Rentabilite_Relique" target="_self">📦 Rentabilité Relique</a>

            <h2>⚙️ Optimisation</h2>
            <a href="Ramdisk" target="_self">🚀 Ramdisk</a>

            <h2>💰 Farm Donjons</h2>
            <a href="#" target="_self">⛏️ À venir</a>
        </div>
    """, unsafe_allow_html=True)
