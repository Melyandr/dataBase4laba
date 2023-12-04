"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import pilot_has_flight_controller
from t08_flask_mysql.app.my_project.auth.domain import PilotHasFlight

pilotHasFlight_bp = Blueprint('pilots_has_flights', __name__, url_prefix='/pilots_has_flights')


@pilotHasFlight_bp.get('')
def get_all_pilots_has_flights() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(pilot_has_flight_controller.find_all()), HTTPStatus.OK)


@pilotHasFlight_bp.post('')
def create_pilots_has_flights() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    pilot_has_flight = PilotHasFlight.create_from_dto(content)
    pilot_has_flight_controller.create(pilot_has_flight)
    return make_response(jsonify(pilot_has_flight.put_into_dto()), HTTPStatus.CREATED)


@pilotHasFlight_bp.get('/<int:pilot_has_flight_id>')
def get_pilot_has_flight(pilot_has_flight_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(pilot_has_flight_controller.find_by_id(pilot_has_flight_id)), HTTPStatus.OK)


@pilotHasFlight_bp.put('/<int:pilot_has_flight_id>')
def update_pilot_has_flight(pilot_has_flight_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    pilot_has_flight = PilotHasFlight.create_from_dto(content)
    pilot_has_flight_controller.update(pilot_has_flight_id, pilot_has_flight)
    return make_response("pilot_has_flight updated", HTTPStatus.OK)


@pilotHasFlight_bp.patch('/<int:pilot_has_flight_id>')
def patch_pilot_has_flight_id(pilot_has_flight_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    pilot_has_flight_controller.patch(pilot_has_flight_id, content)
    return make_response("pilot_has_flight updated", HTTPStatus.OK)


@pilotHasFlight_bp.delete('/<int:pilot_has_flight_id>')
def delete_pilot_has_flight_id(pilot_has_flight_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    pilot_has_flight_controller.delete(pilot_has_flight_id)
    return make_response("pilot_has_flight deleted", HTTPStatus.OK)
