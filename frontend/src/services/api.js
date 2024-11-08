// services/api.js
import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000/api',
});

export const obtenerNoticias = () => api.get('/notas');
export const crearNoticia = (data) => api.post('/notas', data);
export const obtenerComentarios = (idnota) => api.get(`/notas/${idnota}/comentarios`);
export const agregarComentario = (idnota, data) => api.post(`/notas/${idnota}/comentarios`, data);
export const responderComentario = (idcomentario, data) => api.post(`/comentarios/${idcomentario}/respuestas`, data);

export default api;
