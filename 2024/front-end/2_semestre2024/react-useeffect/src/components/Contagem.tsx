import { useEffect, useState } from "react"

type CountProps ={
    count: number
    aumentar: ()=> void
}

export default function Contagem({count, aumentar}:CountProps){

    const [valor, setValor] = useState(0)

    // chamado e todas as fases do ciclo de vida
    useEffect(()=>{
        console.log('Sempre sou chamado');
        
    })

    // chamado apenas na construção do componente
    useEffect(()=>{
        console.log('Sou chamado quando o componente é criado');  
    },[])

    // chamado apenas quando o useState count é alterado
    useEffect(()=>{
        if(count != 0){
            console.log('Chamado apenas quando o count é alterado');
        }
    },[count])

    // chamado quando o componente é desmontado
    useEffect(()=>{
        return ()=>{
            console.log('Ops... Me desmontaram');
            
        }
    }, [])

    return(
        <div>
            <h2>Contagem</h2>
            <p>Valor count = {count}</p>
            <p>Valor do valor = {valor}</p>
            <button onClick={aumentar}>Aumentar</button>
            <button onClick={()=>setValor(valor + 1)}>Aumentar Valor</button>
        </div>
    )
}