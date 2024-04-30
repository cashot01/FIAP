
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



