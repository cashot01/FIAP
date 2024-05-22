
// setItem - adiciona
// getItem - pega
// removeItem - remove
// clear - remove todos



localStorage.setItem('nome', 'Cauan')


let nome = localStorage.getItem('nome')

console.log(nome);

localStorage.removeItem('nome')

localStorage.setItem('nome', 'Guilherme')
localStorage.setItem('altura', '1.70')
localStorage.setItem('peso', '75')
localStorage.setItem('idade', '21')

localStorage.clear()