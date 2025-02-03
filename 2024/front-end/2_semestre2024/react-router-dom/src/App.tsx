import { Outlet } from "react-router-dom"
import Menu from "./components/Menu"
import Rodape from "./components/Rodape"



function App() {
  

  return (
    <>
      <Menu/> {/** Elemento Menu fica fixo na pagina */}
      <Outlet/> {/** Outlet é onde sera chamado o corpo da pagina */}
      <Rodape/> {/** Elemento Rodape fica fix na pagina */}
    </>
  )
}

export default App
