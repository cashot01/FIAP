import streamlit as st

def main():
    st.title("Formulario de Dados Medicos")

    with st.form(key="formulario_medico"):
        
        idade = st.number_input("Idade", min_value=0, max_value=120, step=1)

        genero = st.selectbox("Genero", options=("M", "F"))

        bp = st.number_input("Blood Pressure", min_value=0, max_value=300, step=1)

        sodio = st.number_input("Nivel de sodio (mg/L)", min_value=0, max_value=200, step=1)

        submit_button = st.form_submit_button(label="Enviar")

    if submit_button:
        st.success("Formulario enviado com sucesso")
        st.write("Dados enviados:")
        st.write(f"Idade: {idade}")
        st.write(f"Genero: {genero}")
        st.write(f"Pressao Arterial: {bp}")
        st.write(f"Nivel de sodio: {sodio}")

    with st.sidebar:
        st.title("Sobre")
        st.info("App desenvolvido por Cauan Passos")
        st.info("Este app é um exemplo de como criar um formulario medico em Streamlit")


if __name__ == "__main__":
    main()