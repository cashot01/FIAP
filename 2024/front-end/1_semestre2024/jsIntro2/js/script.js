
console.log("1ª saida");

console.log("2ª saida");

function novaSaida(){
    console.log("Mais uma saída");
}

console.log("3ª saida");

novaSaida()

function soma(num1=0, num2=0){
    // num1 e num2 começa com 0

    return num1 + num2
}

console.log(soma(5));

// function somaMuitos(...nums) {
//     let total = 0
//     for(let num of nums){
//         total += num
//     }    
//     return total
// }


// função anônima - coloca em uma variavel e tira o nome da função
let somaMuitos = function(...nums) {
    let total = 0
    for(let num of nums){
        total += num
    }    
    return total
}

console.log(somaMuitos(10, 3, 77, 123, 45, 200));

//window.alert("Olá pessoal")

// document.write("Agora estou dentro do documento")
// document.write - escreve algo no documento

let titulo = document.getElementById("titulo")
// .innerHTML pega o conteudo do elemento 
// titulo.style.color = "red"
// cor do titulo muda pra o vermelho

// console.log(titulo);
// getElementById - pega o elemento pelo id

let novo = document.getElementById("idNome")

function mudar(){
    titulo.innerHTML = novo.value
}

let itens = document.getElementsByClassName("item")
// getElementsByClassName - pega os elementos pela classe
// sempre vai retornar como Array
console.log(itens[2]);

function inserir(){
    let numero = document.getElementById("idPosicao").value -1
    let corredor = document.getElementById("idNovoClass").value 
    document.getElementsByClassName("corredor")[numero].innerHTML = corredor
    // quando inserir o nome do corredor e a posição vai aparecer (Novo: Cauan, posição: 1 ---> Primeiro: Cauan)
}

function mostrar(){
    let num = document.getElementById("idNumMes").value -1
    let mes = document.getElementsByTagName("li")[num].innerHTML
    document.getElementById("resultado").innerHTML = mes

}

let titulo2 = document.querySelector("#titulo")
// querySelector busca só a 1ª ocorrência

console.log(titulo2);

let varias = document.querySelectorAll("li")
// querySelctorAll busca todas as ocorrências
console.log(varias);




