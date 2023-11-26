"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from t08_flask_mysql.app.my_project.auth.domain.orders.registration import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.aviacompany import ClientType
from t08_flask_mysql.app.my_project.auth.domain.orders.pilot import Pilot
from t08_flask_mysql.app.my_project.auth.domain.orders.air_hostess import Air_hostess
from t08_flask_mysql.app.my_project.auth.domain.orders.aeroport import Aeroport
from t08_flask_mysql.app.my_project.auth.domain.orders.dispatcher import Dispatcher
from t08_flask_mysql.app.my_project.auth.domain.orders.marshrut import Marshrut
from t08_flask_mysql.app.my_project.auth.domain.orders.route import Route
from t08_flask_mysql.app.my_project.auth.domain.orders.airplane import Airplane
from t08_flask_mysql.app.my_project.auth.domain.orders.flight import Flight
from t08_flask_mysql.app.my_project.auth.domain.orders.dispatcher_has_flight import DispatcherHasFlight
from t08_flask_mysql.app.my_project.auth.domain.orders.pilot_has_flight import PilotHasFlight
from t08_flask_mysql.app.my_project.auth.domain.orders.air_hostess_has_flight import AirHostessHasFlight