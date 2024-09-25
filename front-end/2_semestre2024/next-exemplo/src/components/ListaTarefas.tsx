import { useState } from "react";
import Tarefa from "./Tarefa";


export default function ListaTarefas(){

    const [tarefas, setTarefas] = useState([
        {titulo:'Lista de Pagamentos', setor:'Dep. Vendas', descricao:'Levantar os valores das Vendas'},
        {titulo:'Planilha de Salarios', setor:'Dep. Pessoal', descricao:'Gerar Planilhas'}
    ])


    return(
        <div className="lista-tarefa">
            {
            tarefas.map((t, i)=>(
                <Tarefa key={i} {...t}/>
            ))
            }
        </div>
    )
}