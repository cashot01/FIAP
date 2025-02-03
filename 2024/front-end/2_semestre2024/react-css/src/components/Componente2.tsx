import { DivComp2, Button1 } from "../styled"
import Button from "./Button"

export default function Componente2(){

    return(
        <DivComp2>
            <h2>Componente 2</h2>
            <p>Este é o componente 2</p>
            {/* este botão é um componente externo estilizado */}
            <Button/>
            {/* este botão é um elemento interno estilizado */}
            <Button1>Botão 2</Button1>
        </DivComp2>
    )
}