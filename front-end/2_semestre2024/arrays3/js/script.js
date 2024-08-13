
// Spread

const frutas = ['maça', 'uva', 'mamao']
const legumes = ['batata', 'cenoura', 'mandioca']

const feira = [...frutas, ...legumes]

console.log(feira);
// sem spread - [Array(3), Array(3)]
// com spread - ['maça', 'uva', 'mamao', 'batata', 'cenoura', 'mandioca']

let carro ={
    marca: 'Fiat',
    modelo: 'Palio',
    ano: 2000
}

carro = {...carro, modelo:'Uno'}
// {marca: 'Fiat', modelo: 'Palio', ano: 2000}
// {marca: 'Fiat', modelo: 'Uno', ano: 2000}

carro = {...carro, motor:'1.0 turbo'}
// {marca: 'Fiat', modelo: 'Uno', ano: 2000, motor: '1.0 turbo'}

console.log(carro);

// Rest Parameter

function soma(...numeros){
    return  numeros.reduce((acc, item)=> acc += item)
}
console.log(soma(5, 7,3,7,9,1,234));


// Destructuring

let alunos = ['Adriano', 'Bianca', 'Carolina']

let [aluno1,aluno2,aluno3] = alunos

console.log(aluno1); // Adriano
console.log(aluno2); // Bianca
console.log(aluno3); // Carolina

// let car1, car2, car3, car4

// [car1, car2, car3, car4] = ['Civic', 'Cruse', 'Corolla', 'Sentra']

// console.log(car1); 
// console.log(car2);
// console.log(car3);
// console.log(car4);

let car1, car2, car3, car4

[car1 = 'X1', car2 = 'A4', car3 = 'Corvetti', car4 = 'Mustang'] = ['Civic', , 'Corolla']
// trocou X1 pelo Civic e Corvetti pelo Corolla

console.log(car1); 
console.log(car2);
console.log(car3);
console.log(car4);


const exemploFilmes = {
    ficcao: 'Vingadores',
    terror: 'O exorcista',
    comedia: 'O poderoso chefão'
}

let {ficcao, comedia} = exemploFilmes

ficcao = 'Star Wars'

console.log(ficcao); // Star Wars
console.log(exemploFilmes.ficcao); // Vingadores 

// CreatElement - criar elementos no html estático

// jeito manual
// const titulo = "<h1>Titulo da Pagina</h1>"
// document.querySelector('body').innerHTML = titulo


const titulo = document.createElement('h1')
// criando um elemento H1 e guardando na variavel titulo

const texto = document.createTextNode('Titulo da pagina')
// guarda um nó de texto dentro da variavel texto

titulo.appendChild(texto)
// pega o texto e coloca dentro do titulo

titulo.setAttribute('id', 'titulo')
// inserindo um atributo no elemento

document.querySelector('body').appendChild(titulo)
// pega o h1 titulo e insere dentro do body




