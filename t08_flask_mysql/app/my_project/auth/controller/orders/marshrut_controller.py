from t08_flask_mysql.app.my_project.auth.service import marshrut_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class MarshrutController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = marshrut_service
