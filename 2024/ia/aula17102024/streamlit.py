import streamlit as st
import requests

def ChamadaDoWatson():
    # API DO WATSON
    ...
st.title("Chat simples")

if 'mensagens' not in st.session_state:
    st.session_state.mensagens = []

nova_mensagem = st.text_input("Digite sua mensagem: ")

if st.button("Enviar"):
    if nova_mensagem:

        st.session_state.mensagens.append(f"Voce: {nova_mensagem}")
        
        resposta = ChamadaDoWatson(nova_mensagem)
        st.session_state.mensagens.append(f"Bot: {resposta}")

        st.text_input("Digite sua mensagem: ", value="", key="limpar")

for mensagem in st.session_state.mensagens:
    st.text(mensagem)