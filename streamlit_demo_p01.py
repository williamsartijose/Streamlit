import streamlit as st

st.title("Meu Primeiro Aplicativo")

st.header("Testando o cabeçalho")
st.subheader("Testando o sub-cabeçalho")

nome = st.text_input("Digite o seu nome: ")
st.write("Seu nome é: " + nome)
