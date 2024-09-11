import { useState } from "react";

export default function TesteState1(){
    const [nome, setNome] = useState<string>('João')

    return(
        <div>
            <h2>Teste de Estado 1</h2>
            <p>o nome do usuario é {nome}</p>
            <button onClick={()=>setNome}>Mudar</button>
        </div>
    )
}