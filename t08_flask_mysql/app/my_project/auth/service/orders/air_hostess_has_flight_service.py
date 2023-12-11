"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import air_hostess_has_flight_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class AirHostessHasFlightService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = air_hostess_has_flight_dao