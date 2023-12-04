from t08_flask_mysql.app.my_project.auth.service import airplane_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AirplaneController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = airplane_service
