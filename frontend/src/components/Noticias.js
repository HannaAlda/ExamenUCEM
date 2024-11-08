// src/components/Noticias.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { obtenerNoticias } from '../services/api';

function Noticias() {
  const [noticias, setNoticias] = useState([]);

  useEffect(() => {
    // Cargar las noticias al montar el componente
    const cargarNoticias = async () => {
      try {
        const respuesta = await obtenerNoticias();
        setNoticias(respuesta.data);
      } catch (error) {
        console.error('Error al obtener las noticias:', error);
      }
    };
    
    cargarNoticias();
  }, []);

  return (
    <div>
      <h2>Lista de Noticias</h2>
      <ul>
        {noticias.map((noticia) => (
          <li key={noticia.idnota}>
            <h3>{noticia.titulo}</h3>
            <p>{noticia.contenido}</p>
            <Link to={`/noticias/${noticia.idnota}/comentarios`}>Ver Comentarios</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Noticias;
