// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CrearNoticia from './components/CrearNoticia';
import Noticias from './components/Noticias';
import Comentarios from './components/Comentarios';

function App() {
    return (
        <Router>
            <div style={{ textAlign: 'center' }}>
                <h1>¡Bienvenido al sistema de noticias!</h1>
                <nav>
                    <Link to="/">Noticias</Link> | 
                    <Link to="/crear-noticia">Crear Noticia</Link>
                </nav>
            </div>
            <Routes>
                <Route path="/" element={<Noticias />} />
                <Route path="/crear-noticia" element={<CrearNoticia />} />
                <Route path="/noticias/:id/comentarios" element={<Comentarios />} />
            </Routes>
        </Router>
    );
}

export default App;
