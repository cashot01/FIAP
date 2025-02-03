import { Comp1Props, Comp2Props } from "../types"


export default function Componente1({children, autor}:Comp1Props & Comp2Props){

    return(
        <div>
            <h2>Componente1</h2>
            {children}
            <p> Menssagem enviada pelo {autor}</p>
        </div>
    )
}