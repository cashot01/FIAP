"use client";
import { useState } from "react";
import Tarefa from "./Tarefa";
import FormTarefas from "./FormTarefas";
import { TarefaProps } from "@/types";


export default function ListaTarefas(){

    const [tarefas, setTarefas] = useState<TarefaProps[]>([])

    const [tarefa, setTarefa] = useState({titulo:'', setor:'', descricao:''})

    const addTarefa = (e:React.FormEvent<HTMLFormElement>)=>{
        e.preventDefault()
        setTarefas([...tarefas, tarefa])
        setTarefa({titulo:'', setor:'', descricao:''})
    }

    const captura = (e:React.ChangeEvent<HTMLInputElement>)=>{
        const {name, value} = e.target
        setTarefa({...tarefa, [name]:value})

    }

    const removeTarefa = (tit:string)=>{
        let lista = tarefas
        lista = lista.filter(t => t.titulo !== tit)
        setTarefas(lista)
    }


    return(
        <div className="lista-tarefa">
            <FormTarefas {...tarefa} add={addTarefa} digit={captura}/>
            {
            tarefas.map((t, i)=>(
                <Tarefa key={i} {...t} remove={removeTarefa}/>
            ))
            }
        </div>
    )
}