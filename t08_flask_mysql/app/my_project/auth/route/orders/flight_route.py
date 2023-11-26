"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import flight_controller
from t08_flask_mysql.app.my_project.auth.domain import Flight

flight_bp = Blueprint('flights', __name__, url_prefix='/flights')


@flight_bp.get('')
def get_all_flights() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(flight_controller.find_all()), HTTPStatus.OK)


@flight_bp.post('')
def create_flight() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    flight = Flight.create_from_dto(content)
    flight_controller.create(flight)
    return make_response(jsonify(flight.put_into_dto()), HTTPStatus.CREATED)


@flight_bp.get('/<int:flight_id>')
def get_flight(flight_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(flight_controller.find_by_id(flight_id)), HTTPStatus.OK)


@flight_bp.put('/<int:flight_id>')
def update_flight(flight_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    flight = Flight.create_from_dto(content)
    flight_controller.update(flight_id, flight)
    return make_response("Client updated", HTTPStatus.OK)


@flight_bp.patch('/<int:flight_id>')
def patch_flight(flight_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    flight_controller.patch(flight_id, content)
    return make_response("flight updated", HTTPStatus.OK)


@flight_bp.delete('/<int:flight_id>')
def delete_flight(flight_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    flight_controller.delete(flight_id)
    return make_response("flight deleted", HTTPStatus.OK)
