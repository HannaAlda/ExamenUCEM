import React from 'react';

function Noticias({ noticias, setComentarios }) {
    // Maneja la selección de una noticia para obtener sus comentarios
    const handleSelectNoticia = (id) => {
        fetch(`/api/notas/${id}/comentarios`)
            .then(response => response.json())
            .then(data => setComentarios(data))
            .catch(error => console.error('Error al cargar comentarios:', error));
    };

    return (
        <div className="noticias">
            <h2>Noticias</h2>
            {noticias.length > 0 ? (
                <ul>
                    {noticias.map((nota) => (
                        <li key={nota.idnota} onClick={() => handleSelectNoticia(nota.idnota)}>
                            <h3>{nota.titulo}</h3>
                            <p>{nota.contenido}</p>
                            <small>Fecha de Publicación: {new Date(nota.fecha_publicacion).toLocaleString()}</small>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No hay noticias disponibles.</p>
            )}
        </div>
    );
}

export default Noticias;
