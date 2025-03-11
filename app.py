import streamlit as st
import requests

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        /* Forçar o tamanho e a cor da barra lateral */
        [data-testid="stSidebar"] {
            background-color: #191a1f !important;
            width: 70px !important; /* Reduzir largura */
        }

        /* Redimensionar a imagem na barra lateral */
        [data-testid="stImage"] img {
            width: 50px; /* Reduzir tamanho da imagem */
            display: block;
            margin: 0 auto;
        }

        /* Centralizar e ajustar o header */
        .header-container {
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
        }

        /* Ajustar as tabs para não sobrepor */
        div[data-testid="stTabs"] > div {
            margin-top: -10px;
        }

        /* Estilizar os botões na barra lateral */
        .sidebar-button {
            display: block;
            text-align: center;
            background-color: white;
            color: black !important;
            padding: 10px 15px;
            margin: 10px auto;
            border-radius: 15px;
            text-decoration: none;
            font-weight: bold;
        }

        .sidebar-button:hover {
            background-color: #f0f0f0;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

st.sidebar.image("logobkartspng.png", caption="", width=80, use_container_width=False)


st.title('Dashboard BK Arts')

tab1, tab2 = st.tabs(["BK ARTS", "BK ARTS CRIATIVOS"])
with tab1:
    st.markdown(
        """
        <iframe title="BK ARTS" width="843" height="540" src="https://app.powerbi.com/view?r=eyJrIjoiYjA0ZjEyZTItYzIxOS00MjY4LTljYTEtYTUwMjMxYTAxMmFhIiwidCI6ImFiYThhNDc3LTE0MGItNDNiOC04MGQzLWYxOTQwNGVhMTc0YyJ9
" frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True,
    )

with tab2:
    st.markdown(
        """
        <iframe title="BK ARTS - Criativos" width="853" height="540" src="https://app.powerbi.com/view?r=eyJrIjoiNjZkNzZjYjUtYzJiMi00NjMxLTgzNGEtY2Y0MjdhMTQxNTA2IiwidCI6ImFiYThhNDc3LTE0MGItNDNiOC04MGQzLWYxOTQwNGVhMTc0YyJ9" frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True,)


planilhas = {
    "Tráfego Ads": "https://docs.google.com/spreadsheets/d/1WekoU7hKiA8FIQDvn7lAxRf3YCFODhY1NCO2YdLRWLU/edit?gid=0#gid=0",  
    "Financeiro Arts": "https://docs.google.com/spreadsheets/d/1aLMifpOxJBer9h3xUf70Fq9DvpnlokZh/edit?gid=12781143#gid=12781143",
    "Fluxo Anual 2025": "https://docs.google.com/spreadsheets/d/1B1Hqh6uKciOnAlT8OAEJcp2Ybo5bXqT2514G-iouPXQ/edit?gid=513733305#gid=513733305",
    "Fechamentos 2025": "https://docs.google.com/spreadsheets/d/16PVILwVOZxrzpT0U9qnRjyu2o1ac3dlHUa6lM_5DqhY/edit?gid=424343636#gid=424343636"
}

for planilha, link in planilhas.items():
    if st.sidebar.button(planilha):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={link}">', unsafe_allow_html=True)