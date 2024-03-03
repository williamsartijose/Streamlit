import streamlit as st

st.title("Meu Segundo Aplicativo")

st.sidebar.title("Configurações")

st.sidebar.subheader("Nome do Usuário")
nome_usuario = st.sidebar.text_input("Digite seu nome")

st.header("Nome do Usuário")
st.subheader(nome_usuario)

st.sidebar.subheader("Números")
prm_nr = st.sidebar.number_input("Digite o primeiro número")
seg_nr = st.sidebar.number_input("Digite o segundo número")

st.sidebar.subheader("Operação")
operacao_selecionada  = st.sidebar.radio("Escolha a operação que você quer realizar",
                                         ("Adição", "Subtração"))

