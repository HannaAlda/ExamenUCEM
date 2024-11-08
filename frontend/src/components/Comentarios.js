// src/components/Comentarios.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { obtenerComentarios, agregarComentario } from '../services/api';

function Comentarios() {
  const { id } = useParams(); // Extrae el id de la noticia desde la URL
  const [comentarios, setComentarios] = useState([]);
  const [nuevoComentario, setNuevoComentario] = useState('');

  useEffect(() => {
    // Función para cargar los comentarios de una noticia específica
    const cargarComentarios = async () => {
      try {
        const respuesta = await obtenerComentarios(id);
        setComentarios(respuesta.data);
      } catch (error) {
        console.error('Error al obtener los comentarios:', error);
      }
    };

    cargarComentarios();
  }, [id]);

  const manejarEnvioComentario = async (e) => {
    e.preventDefault();
    if (nuevoComentario.trim()) {
      try {
        await agregarComentario(id, { contenido: nuevoComentario, idusuario: 1 }); // Asume idusuario como 1
        setNuevoComentario('');
        const respuesta = await obtenerComentarios(id); // Recargar comentarios
        setComentarios(respuesta.data);
      } catch (error) {
        console.error('Error al agregar el comentario:', error);
      }
    }
  };

  return (
    <div>
      <h2>Comentarios</h2>
      <ul>
        {comentarios.map((comentario) => (
          <li key={comentario.idcomentario}>
            {comentario.contenido}
          </li>
        ))}
      </ul>
      <form onSubmit={manejarEnvioComentario}>
        <textarea
          value={nuevoComentario}
          onChange={(e) => setNuevoComentario(e.target.value)}
          placeholder="Escribe un comentario"
        />
        <button type="submit">Agregar Comentario</button>
      </form>
    </div>
  );
}

export default Comentarios;
