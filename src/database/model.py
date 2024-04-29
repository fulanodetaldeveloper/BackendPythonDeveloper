from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AfinidadMagica(db.Model):
    __tablename__ = 'afinidad_magica'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    afinidad = db.Column(db.String(9), nullable=False)
    
    
class Solicitud(db.Model):
    __tablename__ = 'solicitud'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    identificacion = db.Column(db.String(10))
    edad = db.Column(db.Integer)
    id_afinidad_magica = db.Column(db.Integer, db.ForeignKey('afinidad_magica.id'), nullable=True)
    estatus = db.Column(db.String(9))
    id_grimorio = db.Column(db.Integer, db.ForeignKey('grimorio.id'), nullable=True)

    afinidad_magica = db.relationship('AfinidadMagica', lazy='select', backref='solicitud')
    grimorio = db.relationship('Grimorio', lazy='select', backref='solicitud')
    
    
class Grimorio(db.Model):
    __tablename__ = 'grimorio'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_de_trevoles = db.Column(db.Integer, nullable=False)
    id_clasificacion = db.Column(db.Integer, db.ForeignKey('grimorio_clasificacion.id'), nullable=False)

    clasificacion = db.relationship('GrimorioClasificacion', backref='grimorios')
    
    
class GrimorioClasificacion(db.Model):
    __tablename__ = 'grimorio_clasificacion'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clasificacion = db.Column(db.String(14), nullable=False)
    

class AsignacionDeGrimorios:
    def __init__(self, id, nombre, apellido, identificacion, edad, afinidad_magica, 
                 grimorio_asignado,numero_de_trevoles, clasificacion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.edad = edad
        self.afinidad_magica = afinidad_magica
        self.grimorio_asignado = grimorio_asignado
        self.grimorio_numero_de_trevoles = numero_de_trevoles
        self.grimorio_clasificacion = clasificacion