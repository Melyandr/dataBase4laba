"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import air_hostess_has_flight_controller
from t08_flask_mysql.app.my_project.auth.domain import AirHostessHasFlight

airHostessHasFlight_bp = Blueprint('air_hostess_has_flights', __name__, url_prefix='/air_hostess_has_flights')


@airHostessHasFlight_bp.get('')
def get_all_air_hostess_has_flight_controller() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(air_hostess_has_flight_controller.find_all()), HTTPStatus.OK)


@airHostessHasFlight_bp.post('')
def create_air_hostess_has_flight() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    air_hostess_has_flight = AirHostessHasFlight.create_from_dto(content)
    air_hostess_has_flight_controller.create(air_hostess_has_flight)
    return make_response(jsonify(air_hostess_has_flight.put_into_dto()), HTTPStatus.CREATED)


@airHostessHasFlight_bp.get('/<int:air_hostess_has_flight_id>')
def get_air_hostess_has_flight(air_hostess_has_flight_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(air_hostess_has_flight_controller.find_by_id(air_hostess_has_flight_id)), HTTPStatus.OK)


@airHostessHasFlight_bp.put('/<int:air_hostess_has_flight_id>')
def update_air_hostess_has_flight(air_hostess_has_flight_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    air_hostess_has_flight = AirHostessHasFlight.create_from_dto(content)
    air_hostess_has_flight_controller.update(air_hostess_has_flight_id, air_hostess_has_flight)
    return make_response("air_hostess_has_flight updated", HTTPStatus.OK)


@airHostessHasFlight_bp.patch('/<int:air_hostess_has_flight_id>')
def patch_air_hostess_has_flight_id(air_hostess_has_flight_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    air_hostess_has_flight_controller.patch(air_hostess_has_flight_id, content)
    return make_response("air_hostess_has_flight updated", HTTPStatus.OK)


@airHostessHasFlight_bp.delete('/<int:air_hostess_has_flight_id>')
def delete_air_hostess_has_flight_id(air_hostess_has_flight_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    air_hostess_has_flight_controller.delete(air_hostess_has_flight_id)
    return make_response("air_hostess_has_flight deleted", HTTPStatus.OK)
