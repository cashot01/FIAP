let texto = document.querySelector('#idTexto')
let resultado = document.querySelector('#res')

texto.addEventListener('keydown', ()=>{
    resultado.innerHTML = ''
    texto.value = ''
})
// keydown - quando aperta um atecla do teclado

texto.addEventListener('keyup', (e)=>{
    resultado.innerHTML = ` A tecla ${texto.value} = ${e.keyCode}`
})
// keyup - quando solta a tecla

