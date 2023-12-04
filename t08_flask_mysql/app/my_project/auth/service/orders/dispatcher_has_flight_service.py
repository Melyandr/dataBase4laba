"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import dispatcher_has_flight_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DispatcherHasFlightService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = dispatcher_has_flight_dao