


// let grupos = [['João', 'Carlos', 'Maria'], ['Igor', 'Cauan', 'Gustavo']]

// console.log(alunos[1]);

// console.log(grupos[0][0]);
// 1º [] seleciona qual array, 2º [] elemento do array selecionado

// let carros = [
    //     {modelo:'Civic', marca:'Honda', ano:2017},
    //     {modelo:'Fusca', marca:'Volkswagen', ano:1980},
    //     {modelo:'Gol', marca:'Volkswagen', ano:2000}
    //     modelo , marca, ano => atibutos
    // ]
    
    // console.log(carros[0].modelo);
    // [] - seleciona o objeto
    // .  - seleciona o atributo 
    

let alunos = ['João', 'Carlos', 'Maria']

// alunos[3] = 'Barbara'
// adiciona no array

alunos[alunos.length] = 'Barbara'
// uma gambiarra pra adicionar no final

alunos.push('Lucas') 
// push -> inserir um elemneto no final do array

alunos.pop()
// pop -> remove o ultimo elemento

alunos.sort()
// sort -> ordenar o array de forma crescente / alfabética

alunos.sort().reverse()
// ordenar o array em ordem decrescente / alfabética invertida

alunos.unshift('Israel')
// unshift -> adiciona no inicio do array

alunos.shift()
// shift -> remove do inicio do array

// ['Maria', 'João', 'Carlos', 'Barbara']

alunos.splice(1,0,'Junior', 'Julio')
//  insere elementos em uma posição
// ['Maria', 'Junior', 'Julio', 'João', 'Carlos', 'Barbara']

// ['Maria', 'Junior', 'Julio', 'João', 'Carlos', 'Barbara']

alunos.splice(2,1,'Juliana')
// substitui elementos em uma posição
// ['Maria', 'Junior', 'Juliana', 'João', 'Carlos', 'Barbara']

alunos.splice(1,1)
// remove 1 ou + elementos do array

// console.log(alunos);

const cursos = [
    {nome:'HTML5', duracao:'3 meses'},
    {nome:'CSS3', duracao:'4 meses'},
    {nome:'Javascript', duracao:'5 meses'}
]

// const nomeCursos = cursos.map((curso)=>{ return curso.nome})
const nomeCursos = cursos.map(curso => curso.nome)
// map -> mapear , percorrer array
// nesse caso só pega o nome do curso

const propCursos = cursos.map( curso => `O curso ${curso.nome} só dura ${curso.duracao}`)

const sugestaoCursos = cursos.map((curso, i)=> `O curso ${curso.nome} deve ser o ${i+1}º a ser feito` )

// console.log(sugestaoCursos);


const notas = [
    {nome: 'João', nota: 7.5},
    {nome: 'Maria', nota: 8.5},
    {nome: 'José', nota: 6},
    {nome: 'Carlos', nota: 4},
    {nome: 'Filipi', nota: 3},
]

const notasAprov = notas.filter( aluno => aluno.nota >= 6)

// console.log(notasAprov);

const frutas = ['maça', 'banana', 'pera', 'banana', 'uva', 'goiaba', 'maça', 'laranja', 'morango', 'pera', 'morango']

const frutasSelecionadas = frutas.filter((fruta, i, todas)=> todas.indexOf(fruta) === i)
// ['maça', 'banana', 'pera', 'uva', 'goiaba', 'laranja', 'morango']

console.log(frutasSelecionadas);






