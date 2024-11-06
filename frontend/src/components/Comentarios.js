import React from 'react';

function Comentarios({ comentarios, setRespuestas }) {
    // Maneja la selección de un comentario para obtener sus respuestas
    const handleSelectComentario = (id) => {
        fetch(`/api/comentarios/${id}/respuestas`)
            .then(response => response.json())
            .then(data => setRespuestas(data))
            .catch(error => console.error('Error al cargar respuestas:', error));
    };

    return (
        <div className="comentarios">
            <h2>Comentarios</h2>
            {comentarios.length > 0 ? (
                <ul>
                    {comentarios.map((comentario) => (
                        <li key={comentario.idcomentario} onClick={() => handleSelectComentario(comentario.idcomentario)}>
                            <p>{comentario.contenido}</p>
                            <small>Fecha de Comentario: {new Date(comentario.fecha_comentario).toLocaleString()}</small>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No hay comentarios disponibles para esta noticia.</p>
            )}
        </div>
    );
}

export default Comentarios;
