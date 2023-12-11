"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Route


class RouteDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Route

    def insert_with_params_routes(self, start_country_params, last_country_params, marshrut_id_params
                                  , max_price_param):
        self._session.execute(text(
            f"call insert_with_params_route('{start_country_params}', '{last_country_params}', '{marshrut_id_params}', '{max_price_param}')",
        ))
        self._session.commit()
        return "inserted with params"

    def finding_max_price_in_route(self):
        result = self._session.execute(text(
            f"call finding_max_price_in_route()",

        ))

        return result.scalar()
