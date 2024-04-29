from marshmallow import Schema, fields, validate
    

class AsignacionDeGrimoriosSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    identificacion = fields.String(required=True)
    edad = fields.Integer(required=True)
    afinidad_magica = fields.String(required=True)
    grimorio_asignado = fields.Integer(required=True)
    grimorio_numero_de_trevoles = fields.Integer(required=True)
    grimorio_clasificacion = fields.String(required=True)
    
    
