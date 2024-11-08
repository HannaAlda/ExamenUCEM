// src/components/Noticias.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { obtenerNoticias } from '../services/api';

const Noticias = () => {
    const [noticias, setNoticias] = useState([]);

    useEffect(() => {
        obtenerNoticias()
            .then(response => setNoticias(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>Noticias</h2>
            <ul>
                {noticias.map(noticia => (
                    <li key={noticia.idnota}>
                        <h3>{noticia.titulo}</h3>
                        <p>{noticia.contenido}</p>
                        <Link to={`/noticias/${noticia.idnota}/comentarios`}>Ver comentarios</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Noticias;
