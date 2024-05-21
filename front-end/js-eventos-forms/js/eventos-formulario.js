let nome = document.querySelector('#idNome')
let span = document.querySelector('#acao')

// dispara quando damos foco no elemento
nome.addEventListener('focus', ()=>{
    nome.style.outlineColor = 'blue'
    span.innerHTML = 'O usuario acessou o campo'
})

// dispara o evento quando o campo perde o foco (saiu do campo)
nome.addEventListener('blur', ()=>{
    nome.style.borderColor = 'red'
    span.innerHTML = 'O usuario saiu do campo'
})

let range = document.querySelector('#idBarra')
let valor = document.querySelector('#idValor')

// dispara o evento quando mudamos o valor do campo, só mostra quando solta o mouse
// range.addEventListener('change', ()=>{
//     valor.innerHTML = range.value
// })

// quando arrasto o elemento ja muda o valor
range.addEventListener('input', ()=>{
    valor.innerHTML = range.value
})



let form = document.querySelector('#idForm')

// dispara quando submetemos o formulario
form.addEventListener('submit', ()=>{
    alert('Obrigado por preencher nossa pesquisa ')
})