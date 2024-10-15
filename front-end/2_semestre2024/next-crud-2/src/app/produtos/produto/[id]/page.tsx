"use client"
import { TipoProduto } from "@/types"
import { headers } from "next/headers"
import { useRouter } from "next/navigation"
import React, { useEffect, useState } from "react"


export default function Produto({params }: {params: {id:number} }){

    const navigate = useRouter()

    const [produto, setProduto] = useState<TipoProduto>({
        id: 0,
        nome: "",
        preco:0,
        estoque:0
    })

    const id = params.id

    useEffect(()=>{
        const chamadaApi = async ()=>{
            const response = await fetch(`http://localhost:3000/api/base-produtos/${id}`)
            const data = await response.json()
            setProduto(data)
            console.log(data);
            
        }
        chamadaApi()
    }, [id])

    const handleChange = (e:React.ChangeEvent<HTMLInputElement>)=>{
        const {name, value} = e.target
        setProduto({...produto, [name]:value})
    }

    const handleSubmit = async (e:React.FormEvent<HTMLFormElement>)=>{
        e.preventDefault()

        try{
            const cabecalho = {
                method: 'PUT',
                headers:{"Content-Type":"application/json"},
                body: JSON.stringify(produto)
            }
            const response = await fetch(`http://localhost:3000/api/base-produtos/${id}`, cabecalho)
            if(response.ok){
                alert("Produto atualizado com sucesso")
                setProduto({id:0, nome:"", preco:0, estoque:0})
                navigate.push('/produtos')
                
            }else{
                alert("Erro ao atualizar o produto")
            }

        }catch(error){
            console.log("Erro ao atualizar o produto", error);
            
        }
    }

    return(
        <main className="grow p-5">
            <h1 className="text-3xl text-center text-indigo-600 mb-4 font-bold">Produto</h1>
            <form>
                <div>
                    <label htmlFor="idnome">Nome</label>
                    <input type="text" name="nome" value={produto.nome} id="idnome" onChange={handleChange} />
                </div>
                <div>
                    <label htmlFor="idpreco">Preço</label>
                    <input type="text" name="preco" value={produto.preco} id="idpreco" onChange={handleChange} />
                </div>
                <div>
                    <label htmlFor="idestoque">Estoque</label>
                    <input type="text" name="estoque" value={produto.estoque} id="idestoque" onChange={handleChange} />
                </div>
                <button type="submit">Editar Produto</button>
            </form>
        </main>
    )
}