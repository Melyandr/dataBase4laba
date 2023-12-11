"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import dispatcher_controller
from t08_flask_mysql.app.my_project.auth.domain import Dispatcher

dispatcher_bp = Blueprint('dispatchers', __name__, url_prefix='/dispatchers')


@dispatcher_bp.get('')
def get_all_dispatchers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(dispatcher_controller.find_all()), HTTPStatus.OK)


@dispatcher_bp.post('')
def create_dispatcher() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    dispatcher = Dispatcher.create_from_dto(content)
    dispatcher_controller.create(dispatcher)
    return make_response(jsonify(dispatcher.put_into_dto()), HTTPStatus.CREATED)


@dispatcher_bp.get('/<int:dispatcher_id>')
def get_dispatcher(dispatcher_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(dispatcher_controller.find_by_id(dispatcher_id)), HTTPStatus.OK)


@dispatcher_bp.put('/<int:dispatcher_id>')
def update_dispatcher(dispatcher_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    dispatcher = Dispatcher.create_from_dto(content)
    dispatcher_controller.update(dispatcher_id, dispatcher)
    return make_response("dispatcher updated", HTTPStatus.OK)


@dispatcher_bp.patch('/<int:dispatcher_id>')
def patch_dispatcher(dispatcher_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    dispatcher_controller.patch(dispatcher_id, content)
    return make_response("dispatcher updated", HTTPStatus.OK)


@dispatcher_bp.delete('/<int:dispatcher_id>')
def delete_dispatchers(dispatcher_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    dispatcher_controller.delete(dispatcher_id)
    return make_response("dispatcher deleted", HTTPStatus.OK)
