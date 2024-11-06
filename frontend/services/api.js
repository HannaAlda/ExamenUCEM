import axios from 'axios';

// Configura la instancia de Axios con la URL base de la API
const api = axios.create({
    baseURL: 'http://localhost:5000/api', // Cambia esto si tu backend tiene una URL diferente
});

// Función para obtener todas las noticias
export const obtenerNoticias = async () => {
    try {
        const response = await api.get('/notas');
        return response.data;
    } catch (error) {
        console.error('Error al obtener noticias:', error);
        throw error;
    }
};

// Función para obtener los comentarios de una noticia específica
export const obtenerComentarios = async (idnota) => {
    try {
        const response = await api.get(`/notas/${idnota}/comentarios`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener comentarios:', error);
        throw error;
    }
};

// Función para agregar un comentario a una noticia
export const agregarComentario = async (idnota, contenido, idusuario) => {
    try {
        const response = await api.post(`/notas/${idnota}/comentarios`, {
            contenido,
            idusuario,
        });
        return response.data;
    } catch (error) {
        console.error('Error al agregar comentario:', error);
        throw error;
    }
};

// Función para obtener las respuestas de un comentario específico
export const obtenerRespuestas = async (idcomentario) => {
    try {
        const response = await api.get(`/comentarios/${idcomentario}/respuestas`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener respuestas:', error);
        throw error;
    }
};

// Función para agregar una respuesta a un comentario
export const agregarRespuesta = async (idcomentario, contenido, idusuario) => {
    try {
        const response = await api.post(`/comentarios/${idcomentario}/respuestas`, {
            contenido,
            idusuario,
        });
        return response.data;
    } catch (error) {
        console.error('Error al agregar respuesta:', error);
        throw error;
    }
};

export default api;
