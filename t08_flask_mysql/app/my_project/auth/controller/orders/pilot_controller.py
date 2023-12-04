from t08_flask_mysql.app.my_project.auth.service import pilot_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PilotController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = pilot_service
