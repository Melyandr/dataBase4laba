from t08_flask_mysql.app.my_project.auth.service import route_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class RouteController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = route_service
