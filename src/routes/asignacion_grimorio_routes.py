from flask import Blueprint, jsonify, request
from service.asignacion_grimorio_service import AsignacionService

api_asignacion_grimorios_bp = Blueprint('asignacion_grimorios_route', __name__)


@api_asignacion_grimorios_bp.route('/', methods=['GET'])
def get_asignacion_grimorios():
    
    return  AsignacionService.list_asignacion_grimorios()
