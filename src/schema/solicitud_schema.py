from marshmallow import Schema, fields, validate


class SolicitudSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=20))
    apellido = fields.String(required=True, validate=validate.Length(min=1, max=20))
    identificacion = fields.String(required=True, validate=validate.Length(equal=10))
    edad = fields.Integer(required=True, validate=validate.Range(min=10, max=99))
    id_afinidad_magica = fields.Integer(required=True)
    id_grimorio = fields.Integer(required=False)
    afinidad_magica = fields.Nested('AfinidadMagicaSchema')
    grimorio = fields.Nested('GrimorioSchema')
    
    
class AfinidadMagicaSchema(Schema):
    id = fields.Integer(dump_only=True)
    afinidad = fields.String(required=True)
    
    
class GrimorioClasificacionSchema(Schema):
    id = fields.Integer(dump_only=True)
    clasificacion = fields.String(required=True, validate=validate.Length(equal=10))
    
    
class GrimorioSchema(Schema):
    id = fields.Integer(dump_only=True)
    numero_de_trevoles = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    id_clasificacion = fields.Integer(required=True)
    clasificacion = fields.Nested('GrimorioClasificacionSchema')
    

    


    
    
