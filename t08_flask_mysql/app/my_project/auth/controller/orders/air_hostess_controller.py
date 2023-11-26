from t08_flask_mysql.app.my_project.auth.service import air_hostess_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AirHostessController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = air_hostess_service
