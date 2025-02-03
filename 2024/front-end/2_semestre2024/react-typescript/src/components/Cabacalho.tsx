

type CabecProps = {
    // pipe( | ) = ou 
    status: 'loading' | 'deployed';
}

interface Cabec2Props {
    titulo:string;
}


export default function Cabecalho(props:Cabec2Props & CabecProps){

    document.title = props.titulo

    return(
        <header>
            <h1>{props.titulo}</h1>
            <p>Status: {props.status}</p>
        </header>
    )
}