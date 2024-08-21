import Cabecalho from "./components/Cabecalho"
import Cards from "./components/Cards"
import Componente1 from "./components/Componente1"



function App() {
  
  const titulo:string = "Aula React Props"

  const codigo:number = 15

  const informacao = ()=>{
    alert('Esta aula fala sobre a passagem de dados')
  }

  const autor:string = "Coordenador de vendas"

  const alunos = [
    {nome:'Joao', idade:25},
    {nome:'Maria', idade:22},
    {nome:'Pedro', idade:30}
  ]

  return (
    <>
      <Cabecalho titulo={titulo} codigo={codigo} info={informacao}/>
      <Componente1 autor={autor}>
        <p>Aqui o componente fala sobre este curso</p>
      </Componente1>

      {
        alunos.map((aluno, i)=>(<Cards index={i} nome={aluno.nome} idade={aluno.idade}/>))
      }
    </>
  )
}

export default App
