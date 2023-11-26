"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.registration_controller import ClientController
from .orders.aviacompany_controller import ClientTypeController
from .orders.pilot_controller import PilotController
from .orders.air_hostess_controller import AirHostessController
from .orders.aeroport_controller import AeroportController
from .orders.dispatcher_controller import DispatcherController
from .orders.marshrut_controller import MarshrutController
from .orders.route_controller import RouteController
from .orders.airplane_controller import AirplaneController
from .orders.flight_controller import FlightController
from .orders.dispatcher_has_flight_controller import DispatcherHasFlightController
from .orders.pilot_has_flight_controller import PilotHasFlightController
from .orders.air_hostess_has_flight_controller import AirHostessHasFlightController

client_controller = ClientController()
client_type_controller = ClientTypeController()
pilot_controller = PilotController()
air_hostess_controller = AirHostessController()
aeroport_controller = AeroportController()
dispatcher_controller = DispatcherController()
marshrut_controller = MarshrutController()
route_controller = RouteController()
airplane_controller = AirplaneController()
flight_controller = FlightController()
dispatcher_has_flight_controller= DispatcherHasFlightController()
pilot_has_flight_controller = PilotHasFlightController()
air_hostess_has_flight_controller = AirHostessHasFlightController()