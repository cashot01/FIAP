import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'

// import do metodo para criar a lista de rotas e do provedor de rotas
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

// import de todas as paginas do projeto
import Home from './routes/Home/index.tsx'
import Produtos from './routes/Produtos/index.tsx'
import EditarProdutos from './routes/EditarProdutos/index.tsx'
import Error from './routes/Error/index.tsx'
import GlobalStyle from './global-styled.ts'

const router = createBrowserRouter([
  {
    path: '/',
    element:<App/>,
    errorElement:<Error/>,
    children:[
      {path: '/', element:<Home/>},
      {path: '/produtos', element:<Produtos/>},
      {path: '/produtos/editar/:id', element:<EditarProdutos/>}
    ]
  }
])


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
    <GlobalStyle/>
  </StrictMode>,
)
