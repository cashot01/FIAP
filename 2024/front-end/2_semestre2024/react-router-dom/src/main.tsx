import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import './index.css'

// importando o metodo para a lista de rotas e o provedor de rotas
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

// importar paginas do projeto
import Home from './routes/Home/index.tsx'
import Produtos from './routes/Produtos/index.tsx'
import Error from './routes/Error/index.tsx'
import EditarProdutos from './routes/EditarProdutos/index.tsx'
import GlobalStyle from './global-style.ts'


const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement:<Error/>,
    children: [
      {
        path: '/',
        element: <Home />,
      },
      {
        path: '/produtos',
        element: <Produtos />,
      },
      {
        path: '/produtos/editar/:id',
        element: <EditarProdutos />,
      }
    ]
  }
])



createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
    <GlobalStyle/>
  </StrictMode>,
)
