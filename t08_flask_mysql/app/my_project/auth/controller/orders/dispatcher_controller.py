from t08_flask_mysql.app.my_project.auth.service import dispatcher_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class DispatcherController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = dispatcher_service
