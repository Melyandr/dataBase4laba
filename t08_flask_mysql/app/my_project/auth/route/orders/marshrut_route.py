"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import marshrut_controller
from t08_flask_mysql.app.my_project.auth.domain import Marshrut

marshrut_bp = Blueprint('marshruts', __name__, url_prefix='/marshruts')


@marshrut_bp.get('')
def get_all_marshruts() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(marshrut_controller.find_all()), HTTPStatus.OK)


@marshrut_bp.post('')
def create_marshrut() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    marshrut = Marshrut.create_from_dto(content)
    marshrut_controller.create(marshrut)
    return make_response(jsonify(marshrut.put_into_dto()), HTTPStatus.CREATED)


@marshrut_bp.get('/<int:marshrut_id>')
def get_marshrut(marshrut_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(marshrut_controller.find_by_id(marshrut_id)), HTTPStatus.OK)


@marshrut_bp.put('/<int:marshrut_id>')
def update_marshrut(marshrut_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    pilot = Marshrut.create_from_dto(content)
    marshrut_controller.update(marshrut_id, pilot)
    return make_response("marshrut updated", HTTPStatus.OK)


@marshrut_bp.patch('/<int:marshrut_id>')
def patch_marshrut(marshrut_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    marshrut_controller.patch(marshrut_id, content)
    return make_response("marshrut updated", HTTPStatus.OK)


@marshrut_bp.delete('/<int:pilot_id>')
def delete_marshrut(marshrut_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    marshrut_controller.delete(marshrut_id)
    return make_response("marshrut deleted", HTTPStatus.OK)
