import { useState } from "react"
import Contagem from "./components/Contagem"


function App() {

  const [count, setCount] = useState(0)
  const [contagem, setContagem] = useState(true)

  function aumentar(){
    setCount(count + 1)
  }

  return (
    <>
      <h1>React - Hooks - useEffect</h1>
      <button onClick={()=>setContagem(!contagem)}>Criar contagem</button>
      {contagem ? <Contagem count={count} aumentar={aumentar}/> : '' }
      
    </>
  )
}

export default App
