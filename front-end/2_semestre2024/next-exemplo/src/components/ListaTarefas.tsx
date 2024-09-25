"use client";
import { useState } from "react";
import Tarefa from "./Tarefa";


export default function ListaTarefas(){

    const [tarefas, setTarefas] = useState([
        {titulo:'Lista de Pagamentos', setor:'Dep. Vendas', descricao:'Levantar os valores das Vendas'},
        {titulo:'Planilha de Salarios', setor:'Dep. Pessoal', descricao:'Gerar Planilhas'}
    ])

    const addTarefa = ()=>{
        const ntarefa = {
            titulo:'Tarefa Teste',
            setor:'Desenvolvimento',
            descricao:'Testar a função addTarefa'
        }
        setTarefas([...tarefas, ntarefa])
    }


    return(
        <div className="lista-tarefa">
            <button onClick={addTarefa}>Adicionar</button>
            {
            tarefas.map((t, i)=>(
                <Tarefa key={i} {...t}/>
            ))
            }
        </div>
    )
}