import streamlit as st

def main():
    st.title("Formulario de Dados Medicos")

    with st.form(key="formulario_medico"):
        
        idade = st.number_input("Idade", min_value=0, max_value=120, step=1)

        genero = st.selectbox("Genero", options=("M", "F"))

        bp = st.selectbox("Pressao Arterial", options=("HIGH", "NORMAL", "LOW"))

        sodio = st.number_input("Nivel de sodio (mg/L)", min_value=0, max_value=200, step=1)

        colesterol = st.selectbox("Colesterol", options=("HIGH", "NORMAL", "LOW"))

        submit_button = st.form_submit_button(label="Enviar")

    if submit_button:
        st.success("Formulario enviado com sucesso")
        st.write("Dados enviados:")
        st.write(f"Idade: {idade}")
        st.write(f"Genero: {genero}")
        st.write(f"Pressao Arterial: {bp}")
        st.write(f"Nivel de sodio: {sodio}")
        st.write(f"Colesterol: {colesterol}")

    with st.sidebar:
        st.title("Sobre")
        st.info("App desenvolvido por Cauan Passos")
        st.info("Este app é um exemplo de como criar um formulario medico em Streamlit")


if __name__ == "__main__":
    main()