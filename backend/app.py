from flask import Flask, jsonify, request
from database_models import db, Personal, Usuario, Nota, Comentario, Respuesta
from datetime import datetime
import config  # Importa la configuración desde config.py

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Importa CORS para permitir comunicación con el frontend

app = Flask(__name__)

# Configuración de conexión a MySQL usando config.py
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Habilitar CORS
CORS(app)

# Inicializar la base de datos
db = SQLAlchemy(app)

@app.route('/')
def index():
    return jsonify({"message": "API de Noticias está funcionando"}), 200

# Ruta para obtener todas las noticias
@app.route('/api/notas', methods=['GET'])
def obtener_notas():
    notas = Nota.query.all()
    resultado = [{"idnota": nota.idnota, "titulo": nota.titulo, "contenido": nota.contenido, "fecha_publicacion": nota.fecha_publicacion} for nota in notas]
    return jsonify(resultado), 200

# Ruta para crear una nueva noticia
@app.route('/api/notas', methods=['POST'])
def crear_nota():
    try:
        data = request.json
        nueva_nota = Nota(
            titulo=data['titulo'],
            contenido=data['contenido'],
            fecha_publicacion=datetime.now(),
            idpersonal=data['idpersonal']  # ID del empleado que publica la nota
        )
        db.session.add(nueva_nota)
        db.session.commit()
        return jsonify({"message": "Nota creada con éxito"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Ruta para agregar un comentario a una noticia
@app.route('/api/notas/<int:idnota>/comentarios', methods=['POST'])
def agregar_comentario(idnota):
    try:
        data = request.json
        nuevo_comentario = Comentario(
            contenido=data['contenido'],
            fecha_comentario=datetime.now(),
            idnota=idnota,
            idusuario=data['idusuario']  # ID del usuario que comenta
        )
        db.session.add(nuevo_comentario)
        db.session.commit()
        return jsonify({"message": "Comentario agregado con éxito"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Ruta para obtener todos los comentarios de una noticia
@app.route('/api/notas/<int:idnota>/comentarios', methods=['GET'])
def obtener_comentarios(idnota):
    comentarios = Comentario.query.filter_by(idnota=idnota).all()
    resultado = [{"idcomentario": comentario.idcomentario, "contenido": comentario.contenido, "fecha_comentario": comentario.fecha_comentario} for comentario in comentarios]
    return jsonify(resultado), 200

# Ruta para responder a un comentario
@app.route('/api/comentarios/<int:idcomentario>/respuestas', methods=['POST'])
def agregar_respuesta(idcomentario):
    try:
        data = request.json
        nueva_respuesta = Respuesta(
            contenido=data['contenido'],
            fecha_respuesta=datetime.now(),
            idcomentario=idcomentario,
            idusuario=data['idusuario']  # ID del usuario que responde
        )
        db.session.add(nueva_respuesta)
        db.session.commit()
        return jsonify({"message": "Respuesta agregada con éxito"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Iniciar la aplicación
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos si no existen
    app.run(debug=True)
