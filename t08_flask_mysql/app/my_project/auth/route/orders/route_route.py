"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import route_controller
from t08_flask_mysql.app.my_project.auth.domain import Route

route_bp = Blueprint('routes', __name__, url_prefix='/routes')


@route_bp.get('')
def get_all_routes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(route_controller.find_all()), HTTPStatus.OK)


@route_bp.post('')
def create_route() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.create(route)
    return make_response(jsonify(route.put_into_dto()), HTTPStatus.CREATED)


@route_bp.get('/<int:route_id>')
def get_route(route_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(route_controller.find_by_id(route_id)), HTTPStatus.OK)


@route_bp.put('/<int:route_id>')
def update_route(route_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.update(route_id, route)
    return make_response("route updated", HTTPStatus.OK)


@route_bp.patch('/<int:route_id>')
def patch_route(route_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    route_controller.patch(route_id, content)
    return make_response("route updated", HTTPStatus.OK)


@route_bp.delete('/<int:route_id>')
def delete_route(route_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    route_controller.delete(route_id)
    return make_response("route deleted", HTTPStatus.OK)


@route_bp.post('/insert_with_params_route')
def insert_with_params_routes() -> Response:
    content = request.get_json()
    start_country_params = content.get('start_country_params')
    last_country_params = content.get('last_country_params')
    marshrut_id_params = content.get('marshrut_id_params')
    
    max_price_param = content.get('max_price_param')

    result = route_controller.insert_with_params_routes(start_country_params, last_country_params, marshrut_id_params,max_price_param)
    return make_response(jsonify({'message': result}), HTTPStatus.OK)


@route_bp.post('/finding_max_price_in_route')
def finding_max_price_in_route() -> Response:
    content = request.get_json()

    result = route_controller.finding_max_price_in_route()
    return make_response(jsonify({'message': result}), HTTPStatus.OK)