from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Personal(db.Model):
    __tablename__ = 'personal'
    idpersonal = db.Column(db.Integer, primary_key=True)
    apepaterno = db.Column(db.String(50))
    apematerno = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    fechadeingreso = db.Column(db.Date)

    def __repr__(self):
        return f"<Personal {self.nombre}>"

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    tipo_usuario = db.Column(db.Enum('interno', 'externo'), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nombre_usuario}>"

class Nota(db.Model):
    __tablename__ = 'notas'
    idnota = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_publicacion = db.Column(db.DateTime, default=datetime.utcnow)
    idpersonal = db.Column(db.Integer, db.ForeignKey('personal.idpersonal'), nullable=False)

    # Relación
    personal = db.relationship('Personal', backref=db.backref('notas', lazy=True))

    def __repr__(self):
        return f"<Nota {self.titulo}>"

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    idcomentario = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha_comentario = db.Column(db.DateTime, default=datetime.utcnow)
    idnota = db.Column(db.Integer, db.ForeignKey('notas.idnota'), nullable=False)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuarios.idusuario'), nullable=False)

    # Relaciones
    nota = db.relationship('Nota', backref=db.backref('comentarios', lazy=True))
    usuario = db.relationship('Usuario', backref=db.backref('comentarios', lazy=True))

    def __repr__(self):
        return f"<Comentario {self.idcomentario} en Nota {self.idnota}>"

class Respuesta(db.Model):
    __tablename__ = 'respuestas'
    idrespuesta = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha_respuesta = db.Column(db.DateTime, default=datetime.utcnow)
    idcomentario = db.Column(db.Integer, db.ForeignKey('comentarios.idcomentario'), nullable=False)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuarios.idusuario'), nullable=False)

    # Relaciones
    comentario = db.relationship('Comentario', backref=db.backref('respuestas', lazy=True))
    usuario = db.relationship('Usuario', backref=db.backref('respuestas', lazy=True))

    def __repr__(self):
        return f"<Respuesta {self.idrespuesta} a Comentario {self.idcomentario}>"
