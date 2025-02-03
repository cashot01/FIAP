
let data = new Date()

console.log(data)


// getDate pega somento o dia
console.log(data.getDate());

console.log(('0'+data.getDate()).slice(-2));

// getMonth pega a posição do array de meses
console.log(data.getMonth()+1);

console.log(data.getFullYear());


let diasSemana = [
    'Domingo',
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sabado'
]

// getDay pega a posição do dia da semana
console.log(diasSemana[data.getDay()]);

// manipula o dia do mês
data.setDate(data.getDate()+5)
console.log(data);

// manipula o mês 
data.setMonth(data.getMonth()+5)
console.log(data);

// manipula o ano
data.setFullYear(data.getFullYear()+5)
console.log(data);

// mostra somente dia da semana, mes, dia, ano padrão internacional
console.log(data.toDateString());

// padrão do local que vc está ex: Brasil 21/05/2024
console.log(data.toLocaleDateString());

/*********************************************************** */

let data2 = new Date()

let dia = ('0'+data2.getDate()).slice(-2)
let mes = data2.getMonth()
let meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
]

let ano = data2.getFullYear()
// resultado -> 21 de Maio de 2024
console.log(`${dia} de ${meses[mes]} de ${ano}`);

// getHours pega a hora atual
console.log(('0'+data2.getHours()).slice(-2));

// getMinutes pega os minutos atuais
console.log(data2.getMinutes());

// getSeconds pega os segundos atuais
console.log(data2.getSeconds());

// manipula as horas
data2.setHours(data2.getHours()+6)
console.log(data2);

// manipula os minutos
data2.setMinutes(data2.getMinutes()+15)
console.log(data2);

// manipula os segundos
data2.setSeconds(data2.getSeconds()+20)
console.log(data2);

// pega só o relogio 15:44:44
console.log((data2.toLocaleString()).slice(-8));

function ola(){
    alert('olá pessoal')

}

// dispara a função só uma vez, em determinado tempo em milisegundos
// setTimeout(ola, 5000)

function tempo(){
    let relogio = document.querySelector('#div1')
    
    let data3 = new Date()
    
    relogio.innerHTML = (data3.toLocaleString()).slice(-8)

}

let tmp 

document.querySelector('#ligar').addEventListener('click', ()=>{
   tmp =  setInterval(tempo, 1000)
})

document.querySelector('#desligar').addEventListener('click', ()=>{
    // clearInterval para o setInterval
    clearInterval(tmp)
})

// setInterval(tempo, 1000)












