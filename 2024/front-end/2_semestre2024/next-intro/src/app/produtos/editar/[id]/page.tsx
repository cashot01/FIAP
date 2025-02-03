"use client"

import { listaProdutos } from "@/listaProdutos"
import { useParams } from "next/navigation"


export default function EditarProdutos(){

    const {id} = useParams()
    const idProd:number = Number(id)

    const proc = listaProdutos.filter(p=> p.id === idProd)

    return(
        <div>
            <h1>Editar Produtos</h1>
            <p>Produto escolhido é {proc[0].nome} e custa R$ {proc[0].preco}</p>

        </div>
    )
}