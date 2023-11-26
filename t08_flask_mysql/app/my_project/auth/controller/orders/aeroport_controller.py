from t08_flask_mysql.app.my_project.auth.service import aeroport_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AeroportController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = aeroport_service
