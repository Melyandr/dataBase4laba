from t08_flask_mysql.app.my_project.auth.service import air_hostess_has_flight_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AirHostessHasFlightController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = air_hostess_has_flight_service
