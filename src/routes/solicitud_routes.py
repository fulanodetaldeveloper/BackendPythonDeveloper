from flask import Blueprint, jsonify, request
from service.solicitud_service import SolicitudService

api_solicitud_bp = Blueprint('solicitud_route', __name__)


@api_solicitud_bp.route('/', methods=['GET'])
def get_solicitudes():
    
    return  SolicitudService.list()


@api_solicitud_bp.route('/', methods=['POST'])
def post_solicitudes():
    if not request.is_json:
        return jsonify({'message': 'Invalid JSON'}), 400
    
    json = request.get_json()
    
    return  SolicitudService.add(json)


@api_solicitud_bp.route('/<int:id>', methods=['PUT'])
def put_solicitudes(id):
    if not request.is_json and not id:
        return jsonify({'message': 'Invalid JSON'}), 400
    
    json = request.get_json()
    
    return  SolicitudService.update(json, id)


@api_solicitud_bp.route('/<int:id>/estatus', methods=['PATCH'])
def patch_solicitudes(id):
    if not id:
        return jsonify({'message': 'Invalid Id'}), 400
    
    return  SolicitudService.update_estatus(id)


@api_solicitud_bp.route('/<int:id>', methods=['DELETE'])
def delete_solicitudes(id):
    if not id:
        return jsonify({'message': 'Invalid Id'}), 404
    
    return  SolicitudService.delete(id)