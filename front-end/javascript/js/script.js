
// alert("Terceiro olá mundo!!!!")
// comentario 1 linha 
/*
comentario varias linhas  (barra * * barra)
*/ 

if(true){
    
}

const curso = "Javascript"
// const - variavel constante,  não muda o valor dela
console.log(curso);

let nome = "Cauan" // String
// let - variavel 
console.log(nome)
console.log(typeof nome);
// typeof mostra o tipo da variavel

let preco = 17.35 // Number
console.log(preco);

let quant = 53 // Number
console.log(quant);

let casado = true // Boolean
console.log(casado);

let frutas = ["Maça", "Banana", "Uva"]
console.log(frutas);
console.log(frutas[0]);

let carro = {
    cor: "Preta",
    marca: "Honda",
    modelo: "Civic",
    portas: 4,
    correr: function(){
        alert("Estou correndo")
    }
}

console.log(carro)
console.log(carro.cor)
console.log(carro.marca)
// carro.correr()

// let cliente = prompt("Qual o seu nome? ")
// prompt é o input do python
// alert(cliente)

// let num1 = parseInt(prompt("n1: "))
// let num1 = Number(prompt("n1: "))
// let num2 = parseInt(prompt("n2: "))
// parseInt converte em inteiro
// parseFloat converte para decimal
// Number reconhece o inteiro e decimal 
// console.log("Os valores somados são: "+num1+" e " +num2+"!");
// console.log(`Os valores somado são: ${num1} e ${num2}`);
// console.log(num1 + num2);

let exemplo1 = "Aspas Duplas"
let exemplo2 = 'Aspas Simples'
let exemplo3 = `Uso de Crases`

console.log(exemplo1.length);

// let  user = prompt("Qual seu nome completo?")
// let final = user.indexOf(' ')
// console.log(`Seja bem vindo ${user.slice(0, final)}`);

let txt = "Estão chegando as provas"
console.log(txt.indexOf("as"));
// .indexOf localiza o texto do começo da frase pro final
console.log(txt.lastIndexOf("as"));
// lastIndexOf localiza o texto do final pro começo
console.log(txt.slice(0,5));
// .slice pega o q tem nesse intervalo (Estão)
console.log(txt.substring(6,15));
console.log(txt.replace("provas", "avaliações"));
// replace troca as palavras por outras

let valorJuros = 15.12345
console.log(valorJuros.toFixed(2));
// toFixed mostra quantas casas decimais vc quer (15.12)

let soma = 5 + 5
console.log(soma);

let subtracao = 5 - 3
console.log(subtracao);

let multiplicacao = 5 * 10
console.log(multiplicacao);

let divisao = 100 / 5
console.log(divisao);

let exponciacao = 5 ** 2
console.log(exponciacao);

let modulo = 10 % 3
console.log(modulo);

// let socio = confirm("vc é socio")
// // confirma - alerta se OK (true) ou Cancel (false)
// console.log(socio);

// if(socio){
//     alert("Aproveite nossas promoções")
// } else{
//     alert("Quer se cadastrar?")
// }

let valor1 = 5
let valor2 = "5"
let teste = 6

if(valor1 === valor2){
    // === verifica o tipo (string, number, boolean) e o valor da variavel
    // && - e
    // || - ou
    console.log("verdadeiro");
}else {
    console.log("Falso");
}

for()







// ; é opcional



// document.write(nome)

