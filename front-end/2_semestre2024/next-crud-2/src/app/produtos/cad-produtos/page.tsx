"use client"
import { TipoProduto } from "@/types";
import { useRouter } from "next/navigation";
import { useState } from "react";


export default function CadastroProdutos(){

    const navigate = useRouter()

    const [produto, setProduto] = useState<TipoProduto>({
        id:0,
        nome:'',
        preco:0,
        estoque:0
    })

    // capta os dados digitatos e insere no objeto produto
    const handleChange = (e:React.ChangeEvent<HTMLInputElement>)=>{
        const {name, value} = e.target
        setProduto({...produto, [name]:value })
    }

    const handleSubmit = async (e:React.FormEvent<HTMLFormElement>)=>{
        e.preventDefault()

        const cabecalho = {
            method: "POST",
            headers:{
                "Content-Type": "application/json",
            },
            body: JSON.stringify(produto)
        }

        try{
            const response = await fetch("http://localhost:3000/api/base-produtos", cabecalho)

            if(response.ok){
                alert(`${produto.nome} cadastrado com sucesso`)
                setProduto({
                    id:0,
                    nome:'',
                    preco:0,
                    estoque:0
                })
                navigate.push("/produtos")
            }else{
                alert("Erro ao cadastrar")
            }
        }catch(error){
            console.error("Erro ao cadastarar o produto:",error);
            
        }
    }

    return(
        <main className="grow p-5">
            <h1 className="text-3xl text-center font-bold mb-2 text-indigo-600">Cadastro de Produtos</h1>
            <p className="text-xl text-center font-bold mb-4">Aqui inserimos um novo produto assim que chega na loja.</p>
            <form className="w-1/3 m-auto border border-indigo-950 p-2 rounded-e-md" onSubmit={handleSubmit}>
                <div className="flex flex-col p-2">
                    <label htmlFor="idNome">Nome</label>
                    <input type="text" name="nome" id="idNome" onChange={handleChange} value={produto.nome}/>
                </div>
                <div className="flex flex-col p-2">
                    <label htmlFor="idPreco">Preço</label>
                    <input type="number" step={'0.01'} name="preco" id="idPreco" onChange={handleChange} value={produto.preco} />
                </div>
                <div className="flex flex-col p-2">
                    <label htmlFor="idEstoque">Estoque</label>
                    <input type="number" name="estoque" id="idEstoque" onChange={handleChange} value={produto.estoque} />
                </div>
                <button type="submit">Cadastrar Produto</button>
            </form>
        </main>
    )
}