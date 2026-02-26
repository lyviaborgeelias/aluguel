import React, { useEffect, useState } from "react";
import axios from 'axios'

export default function HomeUser() {
    const token = localStorage.getItem('token')
    const [users, setUser] = useState([]);
    const [filtro, setFiltro] = useState("");
    const [resultado, setResultado] = useState([]);

    const listar = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/usuarios',
                {
                    headers: {Authorization: `Bearer ${token}`}
                }
            )
            setUser(response.data)
        } catch (error) {
            console.log("Erro: ", error);

        }
    };
    const buscarUsuarios = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/usuarios/?nome=${filtro}`,
                {
                    headers: {Authorization: `Bearer ${token}`}
                }
            )
            setResultado(response.data);
        } catch (error) {
            console.error("Erro ao buscar usuários", error);
        }
    };
    useEffect(() => {
        listar()
    }, [])

    return (
        <div className="tabela">
            <h2>Lista de Usuários</h2>
            <table border='1px solid'>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <div style={{ marginTop: "20px" }}>
                <input
                    type="text"
                    placeholder="Digite ID ou Nome"
                    value={filtro}
                    onChange={(e) => setFiltro(e.target.value)}
                />
                <button onClick={buscarUsuarios}>Filtrar</button>
            </div>
            <div style={{ marginTop: "20px" }}>
                <h3>Resultado do Filtro</h3>
                <table border="1">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Email</th>
                            <th>Telefone</th>
                            <th>Tipo</th>
                        </tr>
                    </thead>
                    <tbody>
                        {resultado.map((user) => (
                            <tr key={user.id}>
                                <td>{user.id}</td>
                                <td>{user.nome}</td>
                                <td>{user.email}</td>
                                <td>{user.telefone}</td>
                                <td>{user.tipo}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}