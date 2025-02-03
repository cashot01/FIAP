import { useState } from "react"

export default function TesteState3(){

    const [nome, setNome] = useState<string>('')

    return(
        <div>
            <h2>Teste de Estado 3</h2>
            <p>O nome do usuario é: {nome}</p>
            <input type="text"
                name={nome}
                placeholder="Digite o nome do usuario"
                onChange={(e)=>setNome(e.target.value)}
            />
        </div>
    )
}