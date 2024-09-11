import { useState } from "react"


export default function TesteState2(){

    const [count, setCount] = useState(0);
    let valorVariavel = 0

    const aumentar = ()=>{
        setCount(count + 1)
        valorVariavel = valorVariavel + 1
    }

    return(
        <>
        <h2>Teste de Estado 2</h2>
        <p>O valor de count: {count}</p>
        <p>O valor da variavel: {valorVariavel}</p>
        <button onClick={aumentar}>Aumentar</button>
        {/* <button onClick={()=>setCount(count - 1)}>Diminuir</button> */}
        
        </>

    )
}