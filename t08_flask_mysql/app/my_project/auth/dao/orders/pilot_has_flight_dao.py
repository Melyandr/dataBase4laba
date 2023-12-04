"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import PilotHasFlight


class PilotHasFlightDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = PilotHasFlight

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(PilotHasFlight).filter(PilotHasFlight.name == name).order_by(PilotHasFlight.name).all()

    def find_by_number(self, number: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(PilotHasFlight).filter(PilotHasFlight.number == number).order_by(PilotHasFlight.number.desc()).all()
