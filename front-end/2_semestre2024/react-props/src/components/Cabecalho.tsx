
type CabecProps ={
    titulo:string;
    codigo:number;
    info: ()=> void;
}

export default function Cabecalho(props:CabecProps){
    // props - objeto

    return(
        <div>
            <h1>{props.codigo} - {props.titulo}</h1>
            <p>Continuação da aula 1 de props</p>
            <button onClick={props.info}>Informação</button>
        </div>
    )
}