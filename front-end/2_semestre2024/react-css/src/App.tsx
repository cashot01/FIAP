import './App.css'
import Cabecalho from './components/Cabecalho'
import Componente1 from './components/Componente1'
import Componente2 from './components/Componente2'

function App() {

  const paragr = {
    color:'blue',
    backgroundColor:'#ddf',
    padding:'15px'
  }

  return (
    <div className='div1'>
      <Cabecalho/>
      {/* estilo inline*/}
      <p style={{color:'green', backgroundColor:'#dfd'}}>Este é um exemplo de comok usar CSS em React</p>
      <p style={paragr}>Um segundo paragrafo</p>
      <Componente1/>
      <Componente2/>
    </div>
  )
}

export default App
