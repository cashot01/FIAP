import { listaProdutos } from "@/listaProdutos";
import Link from "next/link";


export default function Produtos(){

    return(
        <div>
            <h1>Produtos</h1>
            {
                listaProdutos.map(p=>(
                    <div key={p.id}>
                        <p>{p.nome} - <Link href={`/produtos/editar/${p.id}`}>Editar</Link></p>
                    </div>
                ))
            }
        </div>
    )
}