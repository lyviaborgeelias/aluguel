import React, {use, useState} from "react";
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import './styles.css'

export default function Login(){
    const [user, setUser] = useState('')
    const [password, setPassword] = useState('')
    const [message, setMessage] = useState('')

    const navigate = useNavigate()
    const logar = async ()=>{
        try {
            const response = await axios.post(
                'http://127.0.0.1:8000/api/token/',{
                    username: user,
                    password: password
                }
            )
            console.log("Deu certo")
            setMessage("Usuario logado")

            localStorage.setItem('token', response.data.access)
            const me = await axios.get('http://127.0.0.1:8000/api/me')
            if(me.data.is_staff){
                navigate('/homeuser')
            }else{
                navigate('/homeuser')
            }
            navigate('/homeuser')              
        } catch (error) {
            console.log("Error: ", error);
            setMessage("Usuario ou senha invalida...")
            
        }

    }
    return(
        <div className="container_login">
            <section className="section_1">
                <p className="user">Login</p>
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
                <div className="text_1">
                    <p>{message}</p>
                </div>
                <button className="btn_1" onClick={logar}>Enter</button>
                <p>Não tem conta?</p>
                <button className="btn_1" onClick={() => navigate('/register')}>Cadastre-se</button>
            </section>
            
            </div>
    )
}