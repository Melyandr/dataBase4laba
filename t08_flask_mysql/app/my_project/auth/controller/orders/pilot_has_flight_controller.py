from t08_flask_mysql.app.my_project.auth.service import pilot_has_flight_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PilotHasFlightController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = pilot_has_flight_service
