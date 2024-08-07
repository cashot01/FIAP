
let carros = ['Fusca', 'Gol', 'Palio', 'Celta']

// adicionando um item no array

carros.splice(2,0, 'Fiesta', 'Opala')

// console.log(carros);

// alterando um item no array
// ['Fusca', 'Gol', 'Fiesta', 'Opala', 'Palio', 'Celta']

carros.splice(1,1,'Polo')

// console.log(carros);


const alunos = [
    {nome:'Luiz', nota:5},
    {nome:'Gustavo', nota:7},
    {nome:'Erick', nota:4},
    {nome:'Felipe', nota:3},
    {nome:'Giovanna', nota:6}
]

let listaAlunos = alunos.map( aluno => aluno.nome)

console.log(listaAlunos);

let aprovados = alunos.filter(aluno => aluno.nota >= 6).map(aluno => `O ${aluno.nome} foi aprovado com a nota ${aluno.nota} de média`)

console.log(aprovados);

const vendedores = [
    {nome:'Janaina', idade:24, vendas:5},
    {nome:'Vitoria', idade:30, vendas:7},
    {nome:'Marcelo', idade:35, vendas:3},
    {nome:'Henrrique', idade:40, vendas:9}
]

const totalVendas = vendedores.reduce((valorTotal,valorAtual)=> valorTotal + valorAtual.vendas,0)

const dadosVendas = vendedores.reduce(
    (acc, item)=>{
        const maisNovo = acc.maisNovo < item.idade ? acc.maisNovo : item.idade
        // acc.maisNovo < item.idade ? acc.maisNovo : item.idade - ternario

        const maisVelho = acc.maisVelho > item.idade ? acc.maisVelho : item.idade

        return {totalVendas: acc.totalVendas + item.vendas, 
            maisNovo: maisNovo,
            maisVelho: maisVelho
        }

    },{totalVendas: 0, maisNovo: undefined, maisVelho: undefined}
)

console.log(dadosVendas);

const fliaBrinquedo = [
    {nome:'Sara', idade:17, altura: 1.5},
    {nome:'Luciana',idade:18, altura: 1.7},
    {nome:'Cleber',idade:15, altura: 1.65},
    {nome:'Andreson',idade:22, altura: 1.80},
]

const todaFilaPode = fliaBrinquedo.every(pessoas => PermissionStatus.altura >= 1.60)
// todas as alternativas tem que ser verdadeira

console.log(todaFilaPode ? "Vamos lá": "Nem todos podem");

const temResponsavel = fliaBrinquedo.some(pessoa => pessoa.idade >= 18)
// pelo menos 1 tem que ser verdadeira

console.log(temResponsavel ? "Sim, vcs podem": "Precisa alguem maior de 18");

const responsavel = fliaBrinquedo.find(pessoa => pessoa.idade >= 18)

console.log(`A pessoa será ${responsavel.nome} pois ela tem ${responsavel.idade}`);

const convidados = ['prof Luiz', 'Gustavo', 'Anne', ' prof Rafael Ronqui', 'Carolina']




