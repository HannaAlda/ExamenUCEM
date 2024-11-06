from flask import Flask, jsonify, request
from models import db, Personal, Usuario, Nota, Comentario, Respuesta
from datetime import datetime

app = Flask(__name__)

# Ruta para obtener todas las noticias
@app.route('/api/notas', methods=['GET'])
def obtener_notas():
    notas = Nota.query.all()
    resultado = [{"idnota": nota.idnota, "titulo": nota.titulo, "contenido": nota.contenido, "fecha_publicacion": nota.fecha_publicacion} for nota in notas]
    return jsonify(resultado), 200

# Ruta para obtener una noticia específica por ID
@app.route('/api/notas/<int:idnota>', methods=['GET'])
def obtener_nota(idnota):
    nota = Nota.query.get(idnota)
    if nota is None:
        return jsonify({"error": "Nota no encontrada"}), 404
    resultado = {
        "idnota": nota.idnota,
        "titulo": nota.titulo,
        "contenido": nota.contenido,
        "fecha_publicacion": nota.fecha_publicacion
    }
    return jsonify(resultado), 200

# Ruta para crear una nueva noticia
@app.route('/api/notas', methods=['POST'])
def crear_nota():
    data = request.json
    nueva_nota = Nota(
        titulo=data['titulo'],
        contenido=data['contenido'],
        fecha_publicacion=datetime.now(),
        idpersonal=data['idpersonal']  # ID del personal que publica la nota
    )
    db.session.add(nueva_nota)
    db.session.commit()
    return jsonify({"message": "Nota creada con éxito"}), 201

# Ruta para agregar un comentario a una noticia
@app.route('/api/notas/<int:idnota>/comentarios', methods=['POST'])
def agregar_comentario(idnota):
    data = request.json
    nota = Nota.query.get(idnota)
    if nota is None:
        return jsonify({"error": "Nota no encontrada"}), 404
    nuevo_comentario = Comentario(
        contenido=data['contenido'],
        fecha_comentario=datetime.now(),
        idnota=idnota,
        idusuario=data['idusuario']  # ID del usuario que comenta
    )
    db.session.add(nuevo_comentario)
    db.session.commit()
    return jsonify({"message": "Comentario agregado con éxito"}), 201

# Ruta para obtener los comentarios de una noticia
@app.route('/api/notas/<int:idnota>/comentarios', methods=['GET'])
def obtener_comentarios(idnota):
    comentarios = Comentario.query.filter_by(idnota=idnota).all()
    resultado = [{"idcomentario": c.idcomentario, "contenido": c.contenido, "fecha_comentario": c.fecha_comentario} for c in comentarios]
    return jsonify(resultado), 200

# Ruta para agregar una respuesta a un comentario
@app.route('/api/comentarios/<int:idcomentario>/respuestas', methods=['POST'])
def agregar_respuesta(idcomentario):
    data = request.json
    comentario = Comentario.query.get(idcomentario)
    if comentario is None:
        return jsonify({"error": "Comentario no encontrado"}), 404
    nueva_respuesta = Respuesta(
        contenido=data['contenido'],
        fecha_respuesta=datetime.now(),
        idcomentario=idcomentario,
        idusuario=data['idusuario']  # ID del usuario que responde
    )
    db.session.add(nueva_respuesta)
    db.session.commit()
    return jsonify({"message": "Respuesta agregada con éxito"}), 201

# Ruta para obtener las respuestas de un comentario
@app.route('/api/comentarios/<int:idcomentario>/respuestas', methods=['GET'])
def obtener_respuestas(idcomentario):
    respuestas = Respuesta.query.filter_by(idcomentario=idcomentario).all()
    resultado = [{"idrespuesta": r.idrespuesta, "contenido": r.contenido, "fecha_respuesta": r.fecha_respuesta} for r in respuestas]
    return jsonify(resultado), 200
