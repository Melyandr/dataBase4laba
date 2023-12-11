"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import pilot_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PilotService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = pilot_dao


    def ten_inserts_in_pilots(self):
        result = self._dao.ten_inserts_in_pilots( )
        return result