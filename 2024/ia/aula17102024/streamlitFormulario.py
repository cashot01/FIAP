# import streamlit as st

# def main():
#     st.title("Formulario de Dados Medicos")

#     with st.form(key="formulario_medico"):
        
#         idade = st.number_input("Idade", min_value=0, max_value=120, step=1)

#         genero = st.selectbox("Genero", options=("M", "F"))

#         bp = st.selectbox("Pressao Arterial", options=("HIGH", "NORMAL", "LOW"))

#         sodio = st.number_input("Nivel de sodio (mg/L)", min_value=0, max_value=200, step=1)

#         colesterol = st.selectbox("Colesterol", options=("HIGH", "NORMAL", "LOW"))

#         submit_button = st.form_submit_button(label="Enviar")

#     if submit_button:
#         st.success("Formulario enviado com sucesso")
#         st.write("Dados enviados:")
#         st.write(f"Idade: {idade}")
#         st.write(f"Genero: {genero}")
#         st.write(f"Pressao Arterial: {bp}")
#         st.write(f"Nivel de sodio: {sodio}")
#         st.write(f"Colesterol: {colesterol}")

#     with st.sidebar:
#         st.title("Sobre")
#         st.info("App desenvolvido por Cauan Passos")
#         st.info("Este app é um exemplo de como criar um formulario medico em Streamlit")


# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
 
# Título da aplicação
st.title("Análise de Drogas com AI - Via API")
 
# Formulário de entrada de dados
st.header("Insira os dados do paciente para análise")
 
# Campos do formulário
idade = st.number_input("Idade", min_value=1, max_value=120, value=30, step=1)

genero = st.selectbox("Gênero", options=["M", "F"])

pressao_sanguinea = st.selectbox("Nível de Pressão Sanguínea", options=["LOW", "NORMAL", "HIGH"])

colesterol = st.selectbox("Nível de Colesterol", options=["NORMAL", "HIGH"])

nivel_sodio = st.number_input("Nível de Sódio para Potássio (Na/K)", min_value=0.0, max_value=100.0, value=15.0)
 
# Botão de submissão
if st.button("Analisar"):
    # Dados que serão enviados para a API
    dados = {
        "Age": idade,
        "Sex": genero,
        "BP": pressao_sanguinea,
        "Cholesterol": colesterol,
        "Na_to_K": nivel_sodio
    }
   
    # Chamada para a API Flask
    resposta = requests.post("http://127.0.0.1:5000/prever", json=dados)
   
    # Exibir a resposta da API
    if resposta.status_code == 200:
        previsao = resposta.json()['previsao']
        st.success(f"A droga sugerida para o paciente é: {previsao[0]}")
    else:
        st.error(f"Erro ao chamar a API Flask. Status: {resposta.status_code}")