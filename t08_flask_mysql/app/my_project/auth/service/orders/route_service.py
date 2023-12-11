"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import route_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class RouteService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = route_dao

    def insert_with_params_routes(self, start_country_params, last_country_params, marshrut_id_params,max_price_param):
        result = self._dao.insert_with_params_routes(start_country_params, last_country_params, marshrut_id_params, max_price_param)
        return result


    def finding_max_price_in_route(self):
        result = self._dao.finding_max_price_in_route()
        return result