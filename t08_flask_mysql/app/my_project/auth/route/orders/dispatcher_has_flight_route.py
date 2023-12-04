"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import dispatcher_has_flight_controller
from t08_flask_mysql.app.my_project.auth.domain import DispatcherHasFlight

dispatcherHasFlight_bp = Blueprint('dispatchers_has_flights', __name__, url_prefix='/dispatchers_has_flights')


@dispatcherHasFlight_bp.get('')
def get_all_dispatchers_has_flights() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(dispatcher_has_flight_controller.find_all()), HTTPStatus.OK)


@dispatcherHasFlight_bp.post('')
def create_dispatchers_has_flights() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    dispatcher_has_flight = DispatcherHasFlight.create_from_dto(content)
    dispatcher_has_flight_controller.create(dispatcher_has_flight)
    return make_response(jsonify(dispatcher_has_flight.put_into_dto()), HTTPStatus.CREATED)


@dispatcherHasFlight_bp.get('/<int:dispatcher_has_flight_id>')
def get_dispatcher_has_flight(dispatcher_has_flight_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(dispatcher_has_flight_controller.find_by_id(dispatcher_has_flight_id)), HTTPStatus.OK)


@dispatcherHasFlight_bp.put('/<int:dispatcher_has_flight_id>')
def update_dispatcher_has_flight(dispatcher_has_flight_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    dispatcher_has_flight = DispatcherHasFlight.create_from_dto(content)
    dispatcher_has_flight_controller.update(dispatcher_has_flight_id, dispatcher_has_flight)
    return make_response("dispatcher_has_flight updated", HTTPStatus.OK)


@dispatcherHasFlight_bp.patch('/<int:dispatcher_has_flight_id>')
def patch_dispatcher_has_flight_id(dispatcher_has_flight_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    dispatcher_has_flight_controller.patch(dispatcher_has_flight_id, content)
    return make_response("dispatcher_has_flight updated", HTTPStatus.OK)


@dispatcherHasFlight_bp.delete('/<int:dispatcher_has_flight_id>')
def delete_dispatcher_has_flight_id(dispatcher_has_flight_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    dispatcher_has_flight_controller.delete(dispatcher_has_flight_id)
    return make_response("dispatcher deleted", HTTPStatus.OK)
