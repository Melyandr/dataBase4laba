"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import aeroport_controller
from t08_flask_mysql.app.my_project.auth.domain import Aeroport

aeroport_bp = Blueprint('aeroports', __name__, url_prefix='/aeroports')


@aeroport_bp.get('')
def get_all_aeroports() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(aeroport_controller.find_all()), HTTPStatus.OK)


@aeroport_bp.post('')
def create_aeroports() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    aeroport = Aeroport.create_from_dto(content)
    aeroport_controller.create(aeroport)
    return make_response(jsonify(aeroport.put_into_dto()), HTTPStatus.CREATED)


@aeroport_bp.get('/<int:aeroport_id>')
def get_pilot(aeroport_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(aeroport_controller.find_by_id(aeroport_id)), HTTPStatus.OK)


@aeroport_bp.put('/<int:aeroport_id>')
def update_aeroport(aeroport_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    aeroport = Aeroport.create_from_dto(content)
    aeroport_controller.update(aeroport_id, aeroport)
    return make_response("Aeroport updated", HTTPStatus.OK)


@aeroport_bp.patch('/<int:aeroport_id>')
def patch_aeroport(aeroport_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    aeroport_controller.patch(aeroport_id, content)
    return make_response("Aeroport updated", HTTPStatus.OK)


@aeroport_bp.delete('/<int:aeroport_id>')
def delete_aeroport(aeroport_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    aeroport_controller.delete(aeroport_id)
    return make_response("Aeroport deleted", HTTPStatus.OK)
