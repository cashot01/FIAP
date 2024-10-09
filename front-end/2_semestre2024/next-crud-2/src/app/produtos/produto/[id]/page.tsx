"use client"
import { TipoProduto } from "@/types"
import { useEffect, useState } from "react"


export default function Produto({params}:{params:{id:number}}){

    const [produto, setProduto] = useState<TipoProduto>()

    useEffect(()=>{
        const chamadaApi = async ()=>{
            const response = await fetch(`http://localhost:3000/api/base-produtos/${params.id}`)
            const data = await response.json()
            setProduto(data)
            console.log(data);
            
        }
        chamadaApi()
    }, [])



    return(
        <main className="grow p-5">
            <h1 className="text-3xl text-center text-indigo-600">Produto</h1>
            <div>
                <p>Id: {produto?.id}</p>
                <p>Nome: {produto?.nome}</p>
                <p>Preço: {produto?.preco}</p>
                <p>Estoque: {produto?.estoque}</p>
            </div>
        </main>
    )
}