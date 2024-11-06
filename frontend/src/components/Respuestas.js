import React from 'react';

function Respuestas({ respuestas }) {
    return (
        <div className="respuestas">
            <h2>Respuestas</h2>
            {respuestas.length > 0 ? (
                <ul>
                    {respuestas.map((respuesta) => (
                        <li key={respuesta.idrespuesta}>
                            <p>{respuesta.contenido}</p>
                            <small>Fecha de Respuesta: {new Date(respuesta.fecha_respuesta).toLocaleString()}</small>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No hay respuestas disponibles para este comentario.</p>
            )}
        </div>
    );
}

export default Respuestas;
