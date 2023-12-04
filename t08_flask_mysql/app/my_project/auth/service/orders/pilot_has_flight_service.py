"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import pilot_has_flight_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PilotHasFlightService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = pilot_has_flight_dao