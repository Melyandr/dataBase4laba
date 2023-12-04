from t08_flask_mysql.app.my_project.auth.service import flight_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FlightController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = flight_service
