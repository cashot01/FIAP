import { RemoveProps, TarefaProps } from "@/types";
import { FaTrashAlt } from "react-icons/fa";


export default function Tarefa({titulo, setor, descricao, remove}: TarefaProps&RemoveProps){


    return(
        <div className="tarefa">
            <button onClick={()=>remove(titulo)}><FaTrashAlt/></button>
            <h2>{titulo}</h2>
            <p>{setor}</p>
            <p>{descricao}</p>
        </div>
    )
}