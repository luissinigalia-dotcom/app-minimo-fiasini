import streamlit as st

st.set_page_config(page_title="Teste de Paleta Fiasini", page_icon="🎨", layout="wide")

st.title("🎨 Paleta Fiasini – teste do tema")
st.write("Se você vê botões/links em azul-escuro e painéis em cinza claro, o tema está aplicado via `.streamlit/config.toml`.")

with st.expander("Diagnóstico rápido"):
    st.write("App mínimo carregado sem dependências extras.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Botão de teste"):
        st.success("Tema aplicado! ✅")
with col2:
    st.link_button("Link (deverá usar a primaryColor)", "https://streamlit.io")
with col3:
    st.checkbox("Checkbox de teste", value=True)

st.info("Este app NÃO usa CSS nem bibliotecas extras; a cor vem só do arquivo `.streamlit/config.toml`.")
