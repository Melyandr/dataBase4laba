from t08_flask_mysql.app.my_project.auth.service import dispatcher_has_flight_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class DispatcherHasFlightController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = dispatcher_has_flight_service
