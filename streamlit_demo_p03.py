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

btn_calcular = st.button("Calcular")

if btn_calcular:
    st.header("Operação escolhida")
    st.subheader(operacao_selecionada)
    st.header("Números selecionados")
    st.subheader(f"O primeiro número é: {prm_nr}. O Segundo número é: {seg_nr}.")
    st.header("Resultado da Operação")
    if operacao_selecionada == "Adição":
        resultado = prm_nr + seg_nr
    else:
        resultado = prm_nr - seg_nr
    st.subheader(f"O Resultado da operação selecionada é: {resultado}")

    st.write("Esse foi um tutorial básico sobre o Streamlit. Espero que todos tenham curtido aprender sobre "
             "este super pacote Python")




