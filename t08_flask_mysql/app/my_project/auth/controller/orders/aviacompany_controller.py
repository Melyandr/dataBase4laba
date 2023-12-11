"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import client_type_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ClientTypeController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = client_type_service

    def create_database(self):
        result = self._service.create_database()
        return result