
// setItem - adiciona
// getItem - pega
// removeItem - remove
// clear - remove todos


// localStorage guarda as informações
localStorage.setItem('nome', 'Cauan')


let nome = localStorage.getItem('nome')

console.log(nome);

localStorage.removeItem('nome')

localStorage.setItem('nome', 'Guilherme')
localStorage.setItem('altura', '1.70')
localStorage.setItem('peso', '75')
localStorage.setItem('idade', '21')

localStorage.clear()


let frutas = ['maça', 'banana', 'pera', 'uva']

localStorage.setItem('lista', JSON.stringify(frutas))

let teste = JSON.parse(localStorage.getItem('lista'))

console.log(teste);

let carros = [
    'Fusca',
    'Variant',
    'Brasilia',
    'Chevette',
    'Del Rei',
    'FIAP 147'
]

sessionStorage.setItem('carros', JSON.stringify(carros))

let listaCarros = JSON.parse(sessionStorage.getItem('carros'))

console.log(listaCarros);