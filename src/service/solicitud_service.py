import random
from flask import jsonify
from sqlalchemy import text
from database.model import Solicitud, db
from schema.solicitud_schema import SolicitudSchema


solicitud_schema = SolicitudSchema()

class SolicitudService:
    
    @staticmethod
    def list():
        solicitudes = Solicitud.query.all();
        return jsonify(solicitud_schema.dump(solicitudes, many=True)), 200
    
    
    @staticmethod
    def add(json):
        errors = solicitud_schema.validate(json)
        
        if errors:
            return jsonify({'message': 'Validation errors', 'errors': errors}), 400
        
        solicitud = Solicitud(nombre = json['nombre'], apellido = json['apellido'],
                              identificacion = json['identificacion'], edad = json['edad'],
                              id_afinidad_magica = json['id_afinidad_magica'], estatus = 'Registrado', id_grimorio=6)
        
        db.session.add(solicitud)
        db.session.commit()
        
        return jsonify(solicitud_schema.dump(solicitud, many=False)), 201
    
    
    @staticmethod
    def update(json, id):
        errors = solicitud_schema.validate(json)
        
        if errors:
            return jsonify({'message': 'Validation errors', 'errors': errors}), 400
        
        solicitud = Solicitud.query.get(id)
        if not solicitud:
            return jsonify({'message': 'Solicitud no encontrada', 'errors': errors}), 404
        
        solicitud.nombre = json['nombre']
        solicitud.apellido = json['apellido'],
        solicitud.identificacion = json['identificacion']
        solicitud.edad = json['edad']
        solicitud.id_afinidad_magica = json['id_afinidad_magica']
        
        db.session.commit()
        
        return jsonify(solicitud_schema.dump(solicitud, many=False)), 200
    
    
    @staticmethod
    def update_estatus(id):
        solicitud = Solicitud.query.get(id)
        if not solicitud:
            return jsonify({'message': 'Solicitud no encontrada', 'errors': errors}), 404
        
        solicitud.estatus = "Aceptado"
        solicitud.id_grimorio = random.randint(1, 5)
        
        db.session.commit()
        
        return jsonify(solicitud_schema.dump(solicitud, many=False)), 200
    
    
    @staticmethod
    def delete(id):
        solicitud = Solicitud.query.get(id)
        if not solicitud:
            return jsonify({'message': 'Solicitud no encontrada', 'errors': id}), 404
        
        db.session.delete(solicitud)
        db.session.commit()
        
        return jsonify({'message': 'Solicitud eliminada', 'id': id}), 200
    
    
    
    