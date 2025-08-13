import streamlit as st

# Configurações da página
st.set_page_config(page_title="App com Cores Fiasini", page_icon="💎", layout="wide")

# CSS inline com as cores da Fiasini
st.markdown("""
    <style>
        /* Fundo da página */
        .stApp {
            background-color: #dde3eb;
            color: #0c0c21;
        }
        
        /* Cor dos botões */
        div.stButton > button:first-child {
            background-color: #c6464a;
            color: white;
            border-radius: 8px;
            border: none;
        }
        div.stButton > button:first-child:hover {
            background-color: #715ea5;
            color: white;
        }

        /* Cor dos checkboxes e outros elementos de input */
        input[type=checkbox] {
            accent-color: #c6464a;
        }

        /* Fundo dos containers secundários */
        .block-container {
            background-color: #ffffff;
        }

        /* Cor de links */
        a {
            color: #c6464a;
            text-decoration: none;
        }
        a:hover {
            color: #a63a3e;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Conteúdo de teste
st.title("💎 App com Cores da Fiasini")
st.write("Este app aplica o tema diretamente via CSS no `app.py`.")
st.button("Botão de Teste")
st.checkbox("Exemplo de Checkbox")
st.link_button("Visitar Site", "https://streamlit.io")
