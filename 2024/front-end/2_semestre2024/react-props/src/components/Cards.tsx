import { AlunoProps } from "../types"


export default function Cards({nome, idade, index}:AlunoProps){

    return(
        <div key={index}>
            <p>Aluno: {nome}</p>
            <p>Idade: {idade}</p>
        </div>
    )
}