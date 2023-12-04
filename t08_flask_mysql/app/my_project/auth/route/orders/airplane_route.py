"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import airplane_controller
from t08_flask_mysql.app.my_project.auth.domain import Airplane

airplane_bp = Blueprint('airplanes', __name__, url_prefix='/airplanes')


@airplane_bp.get('')
def get_all_airplanes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(airplane_controller.find_all()), HTTPStatus.OK)


@airplane_bp.post('')
def create_airplane() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    airplane = Airplane.create_from_dto(content)
    airplane_controller.create(airplane)
    return make_response(jsonify(airplane.put_into_dto()), HTTPStatus.CREATED)


@airplane_bp.get('/<int:airplane_id>')
def get_airplane(airplane_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(airplane_controller.find_by_id(airplane_id)), HTTPStatus.OK)


@airplane_bp.put('/<int:airplane_id>')
def update_airplane(airplane_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    airplane = Airplane.create_from_dto(content)
    airplane_controller.update(airplane_id, airplane)
    return make_response("airplane updated", HTTPStatus.OK)


@airplane_bp.patch('/<int:airplane_id>')
def patch_airplane(airplane_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    airplane_controller.patch(airplane_id, content)
    return make_response("airplane updated", HTTPStatus.OK)


@airplane_bp.delete('/<int:airplane_id>')
def delete_airplane(airplane_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    airplane_controller.delete(airplane_id)
    return make_response("airplane deleted", HTTPStatus.OK)
