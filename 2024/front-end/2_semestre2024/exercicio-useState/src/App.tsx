import { useState } from "react"


function App() {
  
  const [count, setCount] = useState<number>(0)

  const aumentar = ()=>{
    setCount(count + 1)
  }

  const diminuir = ()=>{
    setCount(count - 1)
  }

  return (
    <>
     <h1>Exercicio UseSate</h1>
     <h2>Contador</h2>
     <p> {count}</p>
     <button onClick={aumentar}>Aumentar</button>
     <button onClick={diminuir}>Diminuir</button>
    </>
  )
}

export default App
