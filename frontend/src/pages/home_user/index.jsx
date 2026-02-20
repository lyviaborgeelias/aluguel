import React, {useEffect, useState} from "react";
import axios from 'axios'

export default function HomeUser(){
    const token = localStorage.getItem('token')

    const [users, setUsers] = useState([]);

    const listar= async ()=>{
        const response = await axios.get('http://127.0.0.1:8000/api/usuarios')
        console.log(response.data[0]);
    }
    useEffect(()=>{
        listar()
        fetch('http://127.0.0.1:8000/api/usuarios')
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                setUsers(data)
            })
    }, [])

    return(
        <div className="tabela">
            <h2>Lista de Usuários</h2>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => (
                    <tr key={user.id}>
                        <td>{user.id}</td>
                        <td>{user.nome}</td>
                        <td>{user.email}</td>
                    </tr>
            ))}
            </tbody>
        </div>
    )
}