import react from './../assets/react.svg'
// nome da function sempre = nome do arquivo
export default function Componente1(){

    let aluno = 'Bruno'


    return(
        <>
        <h2>Componente 1</h2>
        <img src={react} alt="logo React" />
        <br />
        <p>Nome do aluno: {aluno}</p>
        </>
    )
}