// function soma(n1, n2){
//    return n1 + n2
    
// }

// console.log(soma(3, 4));

// (function(a, b){
//     console.log(a-b);
    
// })
// (10, 5)

// const multi = function(f, g){
//     return f*g
// }

// let resultado = multi(3, 3)
// console.log(resultado);


// const teste = function(){
//     console.log("olá");
    
// }
// teste()

// let triplo = function(a){
//     return a*3
// }
// console.log(triplo(7));


// let triplo = (a) =>{
//     return a*3
// }
// console.log(triplo(5));

// let dobro = (a) => 2*a
// console.log(dobro(10));

// FUNÇÃO COM REST
const soma = (...numeros) =>{
    let aux = 0;
    for(i of numeros){
        aux += 1
    }
    return aux
}


// FUNÇÃO COM SPREAD
const numerosV2 = [1,3,6,4]
console.log("SPREAD " + soma(...numerosV2));
// SPREAD - ESPALHAMENTO



