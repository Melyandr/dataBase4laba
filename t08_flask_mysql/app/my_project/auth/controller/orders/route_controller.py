from t08_flask_mysql.app.my_project.auth.service import route_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class RouteController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = route_service

    def insert_with_params_routes(self, start_country_params, last_country_params, marshrut_id_params,max_price_param):
        result = self._service.insert_with_params_routes(start_country_params, last_country_params, marshrut_id_params,max_price_param)
        return result


    def finding_max_price_in_route(self):
        result = self._service.finding_max_price_in_route()
        return result