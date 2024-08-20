import Cabecalho from "./components/Cabacalho"
import Componente1 from "./components/Componente1"


function App() {

  // essa parte trablha com TS / JS
  const curso:string = 'Javascript'

  const aviso = ()=> alert('Esta menssagem vem de App')


  return (
    // essa parte trabalha TSX / JSX, como um 'html'
    <>
      <Cabecalho />
      <Componente1 curso={curso} aviso={aviso}/>
      
    </>
  )
}

export default App
