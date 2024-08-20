



export default function Componente1(props:{curso:string, aviso: () => void}){

    return(
        <div>
            <p>usando um pouco de typescript</p>
            <p>Curso: {props.curso}</p>
            <button onClick={()=> props.aviso()}>Aviso</button>
        </div>
    )
}