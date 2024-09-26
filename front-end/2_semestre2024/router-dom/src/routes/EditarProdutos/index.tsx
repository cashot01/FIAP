import { listaProdutos } from "../../listaProdutos"
import { useParams, useNavigate } from "react-router-dom"
import { ProdutoType } from "../../types"
import { MainGeral } from "../../styled"


export default function EditarProdutos(){

    const lista:ProdutoType[] = listaProdutos
    const navegacao = useNavigate()
    const { id } = useParams() // recebendo id que veio como parametro
    const idProd:number = Number(id) // convertendo o id em number

    // procurando o objeto com o id que veio da URI
    const proc = lista.filter((prod)=> prod.id === idProd)
    const produto = proc[0] // tirando o objeto do array

    const salvar = ()=>{
        alert(`Produto: ${produto.nome} editado com sucesso! `)
        return navegacao('/produtos')
    }


    return(
        <MainGeral>
            <h1>Editar Produtos</h1>
            <p>Editando o produto: {produto.nome}</p>
            <button onClick={salvar}>Salvar</button>
        </MainGeral>
    )
}