import Cabecalho from "./components/Cabacalho"
import Componente1 from "./components/Componente1"


function App() {

  // essa parte trablha com TS / JS
  const curso:string = 'Javascript'

  const titulo:string = 'React - Intro 2'

  const status = 'deployed' 

  const aviso = ()=> alert('Esta menssagem vem de App')


  return (
    // essa parte trabalha TSX / JSX, como um 'html'
    <>
      <Cabecalho titulo={titulo} status={status}/>
      <Componente1 curso={curso} aviso={aviso}>
        // children - tudo que esta no Componente1 nesse caso
        <h3>Lista de cursos</h3>
        <ul>
          <li>React</li>
          <li>Angular</li>
          <li>Vue</li>
        </ul>
      </Componente1>  
      
    </>
  )
}

export default App
