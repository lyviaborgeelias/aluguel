import React, {useState} from "react";
import {useNavigate} from 'react-router-dom'
import axios from 'axios'

export default function Cadastro(){
    const [user, setUser] = useState('')
    const [password, setPassword] = useState('')
    const [message, setMessage] = useState('')
    const [email, setEmail] = useState('')
    const [tipo, setTipo] = useState('')
    const [telefone, setTelefone] = useState('')

    const navigate = useNavigate()
    const cadastro = async ()=>{
        try {
            const response = await axios.post(
                'http://127.0.0.1:8000/api/register/',{
                    username: user,
                    password: password,
                    email: email,
                    tipo: tipo,
                    telefone: telefone
                }
            )
            console.log("usuario", user)
            console.log("senha",password);
            
            setMessage("Usuario cadastrado")
            
            const resp = await axios.post(
                'http://127.0.0.1:8000/api/token/',{
                    username: user,
                    password: password
                }
            )


            localStorage.setItem('token', resp.data.access)
            navigate('/homeuser') 
            console.log(resp.data.access);
                         
        } catch (error) {
            console.log("Error: ", error);
            setMessage("Usuario não cadastrado!")
        }

    }
    return(
        <div className="container">
            <section className="section_1">
                <p className="user">Cadastre-se</p>
                <p>Usuario</p>
                <input
                    className="caixa"
                    value={user}
                    onChange={(e)=>{setUser(e.target.value)}}
                    placeholder="User"
                />
                <p>Senha</p>
                <input
                    className="caixa"
                    value={password}
                    onChange={(e)=>{setPassword(e.target.value)}}
                    placeholder="Password"
                />
                <p>E-mail</p>
                <input
                    className="caixa"
                    value={email}
                    onChange={(e)=>{setEmail(e.target.value)}}
                    placeholder="email"
                />
                <p>Telefone</p>
                <input
                    className="caixa"
                    value={telefone}
                    onChange={(e)=>{setTelefone(e.target.value)}}
                    placeholder="telefone"
                />
                <p>Tipo</p>
                <input
                    className="caixa"
                    value={tipo}
                    onChange={(e)=>{setTipo(e.target.value)}}
                    placeholder="tipo"
                />
                <div className="text_1">
                    <p>{message}</p>
                </div>
                <button className="btn_1" onClick={cadastro}>Cadastrar</button>
            </section>
        </div>
    )
}