import { CabecProps } from "../types"

export default function Cabecalho(props:CabecProps){

    return(
        <div>
            <h1>{props.titulo}</h1>
            
        </div>
    )
}