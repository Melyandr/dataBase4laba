"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import pilot_controller
from t08_flask_mysql.app.my_project.auth.domain import Pilot

pilot_bp = Blueprint('pilots', __name__, url_prefix='/pilots')


@pilot_bp.get('')
def get_all_pilots() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(pilot_controller.find_all()), HTTPStatus.OK)


@pilot_bp.post('')
def create_pilot() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    pilot = Pilot.create_from_dto(content)
    pilot_controller.create(pilot)
    return make_response(jsonify(pilot.put_into_dto()), HTTPStatus.CREATED)


@pilot_bp.get('/<int:pilot_id>')
def get_pilot(pilot_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(pilot_controller.find_by_id(pilot_id)), HTTPStatus.OK)


@pilot_bp.put('/<int:pilot_id>')
def update_pilot(pilot_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    pilot = Pilot.create_from_dto(content)
    pilot_controller.update(pilot_id, pilot)
    return make_response("Client updated", HTTPStatus.OK)


@pilot_bp.patch('/<int:pilot_id>')
def patch_pilot(pilot_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    pilot_controller.patch(pilot_id, content)
    return make_response("Pilot updated", HTTPStatus.OK)


@pilot_bp.delete('/<int:pilot_id>')
def delete_pilot(pilot_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    pilot_controller.delete(pilot_id)
    return make_response("Pilot deleted", HTTPStatus.OK)

@pilot_bp.post('/ten_inserts_in_pilot')
def ten_inserts_in_pilots() -> Response:
    content = request.get_json()


    result = pilot_controller.ten_inserts_in_pilots()
    return make_response(jsonify({'message': result}), HTTPStatus.OK)