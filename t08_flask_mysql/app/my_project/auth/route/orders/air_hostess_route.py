"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import air_hostess_controller
from t08_flask_mysql.app.my_project.auth.domain import Air_hostess

air_hostess_bp = Blueprint('air_hostess', __name__, url_prefix='/air_hostess')


@air_hostess_bp.get('')
def get_all_air_hostess() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(air_hostess_controller.find_all()), HTTPStatus.OK)


@air_hostess_bp.post('')
def create_air_hostess() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    air_hostess = Air_hostess.create_from_dto(content)
    air_hostess_controller.create(air_hostess)
    return make_response(jsonify(air_hostess.put_into_dto()), HTTPStatus.CREATED)


@air_hostess_bp.get('/<int:air_hostess_id>')
def get_air_hostess(air_hostess_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(air_hostess_controller.find_by_id(air_hostess_id)), HTTPStatus.OK)


@air_hostess_bp.put('/<int:air_hostess_id>')
def update_air_hostess(air_hostess_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    air_hostess = Air_hostess.create_from_dto(content)
    air_hostess_controller.update(air_hostess_id, air_hostess)
    return make_response("air_hostess updated", HTTPStatus.OK)


@air_hostess_bp.patch('/<int:air_hostess_id>')
def patch_air_hostess(air_hostess_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    air_hostess_controller.patch(air_hostess_id, content)
    return make_response("air_hostess updated", HTTPStatus.OK)


@air_hostess_bp.delete('/<int:air_hostess_id>')
def delete_air_hostess(air_hostess_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    air_hostess_controller.delete(air_hostess_id)
    return make_response("Pilot deleted", HTTPStatus.OK)
