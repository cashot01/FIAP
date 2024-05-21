let nome = document.querySelector('#idNome')
let span = document.querySelector('#acao')

nome.addEventListener('focus', ()=>{
    nome.style.outlineColor = 'blue'
    span.innerHTML = 'O usuario acessou o campo'
})