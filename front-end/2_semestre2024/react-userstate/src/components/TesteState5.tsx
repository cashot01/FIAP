import { useState } from "react"
type Pet ={nome: string; idade: number}

export default function TesteState5(){

    const [carros, setCarros] = useState<string[]>(['Onix', 'Polo', 'HB20'])
    const [carro, setCarro] = useState<string>('')

    // exemplo de tipagem para objetos
    const [pet, setPet]  = useState<Pet>({nome:'Spark', idade: 18})
    const [pets, setPets] = useState<Pet[]>([
        {nome: 'Spark', idade: 18},
        {nome: 'Lilica', idade: 15},
        {nome: 'Suzi', idade: 19}
    ])

    return(
        <div>
            <h2>Teste de Estado 5</h2>
            <p>Carros: | {carros.map(car=><span>{car} |</span>)}</p>
            <input type="text" onChange={(e)=>setCarro(e.target.value)}/>
            <button onClick={()=>setCarros([...carros, carro])}>Adicionar</button>
            <button onClick={()=>setCarros([])}>Apagar Todos</button>

        </div>
    )
}