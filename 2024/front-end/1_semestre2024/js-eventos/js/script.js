
let botao = document.querySelector('#btn-aviso')

// botao.onclick = function(){
//     alert("olá pessoal, envento de dentro do js")
// }


// função arrow function ()=>{}
// se for apenas uma linha pode retirar as chaves e colocar depois da seta

// botao.onclick = ()=>{
//     alert("olá pessoal, envento de dentro do js")
// }

// botao.onclick = ()=> alert("olá pessoal, envento de dentro do js")

// eventos , 1º parametro oq eu quero fazer, 2ºparametro função relacionada com a ação
botao.addEventListener('click', clicou )
// click - clicar no botão
botao.addEventListener('mouseenter', entrou )
// mouseenter - quando o mouse entra no botão
botao.addEventListener('mouseout', saiu )
// mouseout - quando sai do botão

function saiu(){
    botao.innerHTML = "Saiu !"
}
function entrou(){
    botao.innerHTML = "Entrou !"

}

function clicou(){
    botao.innerHTML = "Clicou, não entra nem sai mais !"
    botao.removeEventListener('mouseenter', entrou)
    botao.removeEventListener('mouseout', saiu)
    // removeEventListener - remove o enento
}


/****************************************************************** */

let botoes = document.querySelectorAll('.item')

// forEach - é um for
botoes.forEach((item, i)=>{
    item.addEventListener('click', ()=> console.log(`Clicou no botão ${i+1} ! `))
})
