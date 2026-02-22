import React, { useEffect, useState } from "react";
import axios from "axios";

export default function HomeUser() {
  const token = localStorage.getItem("token");

  const [users, setUsers] = useState([]);
  const [filtro, setFiltro] = useState("");
  const [resultado, setResultado] = useState([]);


  const listar = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/usuarios/",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setUsers(response.data);
    } catch (error) {
      console.error("Erro ao listar usuários", error);
    }
  };

  const buscarUsuarios = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/usuarios/?nome=${filtro}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setResultado(response.data);
    } catch (error) {
      console.error("Erro ao buscar usuários", error);
    }
  };

  useEffect(() => {
    listar();
  }, []);

  return (
    <div className="tabela">
      <h2>Lista de Usuários</h2>

      <table border="1">
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

      {resultado.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <h3>Resultado do Filtro</h3>
          <table border="1">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
              </tr>
            </thead>
            <tbody>
              {resultado.map((user) => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>{user.nome}</td>
                  <td>{user.email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}