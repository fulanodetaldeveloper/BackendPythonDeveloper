from flask import jsonify
from database.model import Solicitud, AsignacionDeGrimorios
from schema.asignacion_grimorio_schema  import  AsignacionDeGrimoriosSchema


asignacion_de_grimorios_schema = AsignacionDeGrimoriosSchema()


class AsignacionService:
    
    @staticmethod
    def list_asignacion_grimorios():
        asignaciones = Solicitud.query.all();
        result = []
        for a in asignaciones:
            obj = AsignacionDeGrimorios(a.id, a.nombre, a.apellido, 
                                        a.identificacion, a.edad, 
                                        a.afinidad_magica.afinidad, a.grimorio.id,
                                        a.grimorio.numero_de_trevoles, a.grimorio.clasificacion.clasificacion)
            
            result.append(obj)
            
        return jsonify(asignacion_de_grimorios_schema.dump(result, many=True)), 200