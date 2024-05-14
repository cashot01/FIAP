let minhaDiv = document.querySelector('#div1')

minhaDiv.addEventListener('mouseenter', entrar)
minhaDiv.addEventListener('mouseout', sair)
// minhaDiv.addEventListener('click', clicar)
minhaDiv.addEventListener('contextmenu', clickDireito)
// contextmenu - clicar com botão direito mouse
minhaDiv.addEventListener('dblclick', clickDuplo)
// dblclick click duplo mouse
minhaDiv.addEventListener('mousemove', moveu)
// mousemove - movimento do mouse
minhaDiv.addEventListener('mousedown', apertou)
minhaDiv.addEventListener('mouseup', soutou)
// mousedown e mouseup - é o click dividido
// mouseup só funciona se não tiver click

function soutou(){
    minhaDiv.innerHTML = 'você soutou'
    minhaDiv.style.backgroundColor = 'lime'
}

function apertou(){
    minhaDiv.innerHTML = 'você apertou'
    minhaDiv.style.backgroundColor = 'aqua'
}

function moveu(e){
    let x = e.clientX - this.offsetLeft
    let y = e.clientY - this.offsetTop
    let res = document.querySelector('span')
    res.innerHTML = `Posição X ${x} e Y ${y}`

}

function clickDuplo(){
    
    minhaDiv.innerHTML = 'click Duplo'
    minhaDiv.style.backgroundColor = 'red'
}

function clickDireito(e){
    e.preventDefault()
    // somente na div n abre o menu de contexto (recarregar, inspecionar, etc)
    minhaDiv.innerHTML = 'click Direito'
    minhaDiv.style.backgroundColor = 'pink'
}

function clicar(){
    minhaDiv.innerHTML = 'Você clicou'
    minhaDiv.style.backgroundColor = 'orange'
}

function sair(){
    minhaDiv.innerHTML = 'Você saiu'
    minhaDiv.style.backgroundColor = 'green'
}

function entrar(){
    minhaDiv.innerHTML = 'Você entrou'
    minhaDiv.style.backgroundColor = 'blue'
}

