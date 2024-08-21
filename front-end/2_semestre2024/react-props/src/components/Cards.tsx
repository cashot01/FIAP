
type AlunoProps= {
    nome:string;
    idade:number;
    index:number;
}

export default function Cards({nome, idade, index}:AlunoProps){

    return(
        <div key={index}>
            <p>Aluno: {nome}</p>
            <p>Idade: {idade}</p>
        </div>
    )
}