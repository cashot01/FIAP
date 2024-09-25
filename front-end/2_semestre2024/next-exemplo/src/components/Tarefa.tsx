import { TarefaProps } from "@/types";


export default function Tarefa({titulo, setor, descricao}: TarefaProps){


    return(
        <div className="tarefa">
            <h2>{titulo}</h2>
            <p>{setor}</p>
            <p>{descricao}</p>
        </div>
    )
}