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
   <main className="flex justify-center p-10">
      <span>{user?.nome == "" ? "Fazer o login" : user?.nome}</span>

      <h1 className="text-center text-4xl font-bold text-indigo-800">Home</h1>
      
      <form onSubmit={handleSubmit}>
        <div>
          <input type="text" placeholder="Nome" name="nome" value={dados.nome} onChange={handleChange} />
        </div>

        <div>
          <input type="password" placeholder="senha" name="senha" value={dados.senha} onChange={handleChange}  />
        </div>
        <button type="submit">Logar</button>
      </form>
   </main>
  );
}
