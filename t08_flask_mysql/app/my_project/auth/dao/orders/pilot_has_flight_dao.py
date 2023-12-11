"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import PilotHasFlight


class PilotHasFlightDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = PilotHasFlight

    def insert_in_pilot_has_flights(self, pilot_id, flight_id):
        self._session.execute(text(
            f"call insert_in_pilot_has_flight('{pilot_id}', '{flight_id}')",
        ))
        self._session.commit()
        return "inserted in_pilot_has_flights"