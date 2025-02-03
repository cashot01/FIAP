"use client"
import { AuthContext } from "@/context";
import { ChangeEvent, FormEvent, useContext, useState } from "react";


export default function Home() {

  const {user, login, logout} = useContext(AuthContext)

  const [dados, setDados] = useState({
    nome:"", senha:""
  })

  const handleChange = (e:ChangeEvent<HTMLInputElement>)=>{
    const {name, value} = e.target
    setDados({...dados, [name]:value})
  }

  const handleSubmit = (e:FormEvent<HTMLFormElement>)=>{
    e.preventDefault()
    login(dados)
  }

  return (
   <main className="flex flex-col itens-center justify-center p-10">
      <span className="text-2xl">{user?.nome == "" ? "Fazer o login" : user?.nome}</span>
      {user?.nome == "" ? "" : (<button className="rounded-md bg-red-600 text-white p-2" onClick={logout}>Deslogar</button>)}
      <h1 className="text-center text-4xl font-bold text-indigo-800">Home</h1>
      
      <form className="w-96 border border-indigo-950 p-6" onSubmit={handleSubmit}>
        <div className="py-2">
          <input className="border-2 border-gray-400 p-2 rounded-md w-full" type="text" placeholder="Nome" name="nome" value={dados.nome} onChange={handleChange} />
        </div>

        <div>
          <input className="border-2 border-gray-400 p-2 rounded-md w-full" type="password" placeholder="senha" name="senha" value={dados.senha} onChange={handleChange}  />
        </div>
        <button type="submit">Logar</button>
      </form>
   </main>
  );
}
