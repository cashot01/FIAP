import styled from "styled-components"
import Button from "./Button"

const DivComp1 = styled.div`
    border: 2px solid red;
    padding: 10px;
    background-color: lightcoral;

    h2{
        color: #fff;
        text-align: center;
    }

    p{
        color: #fff;
        text-align: justify;
        font-size: 1.5em;
    }

`


export default function Componente1(){

    return(
        <DivComp1>
            <h2>Componente 1</h2>
            <p>Este é o componente 1</p>
            <Button/>
        </DivComp1>
    )
}