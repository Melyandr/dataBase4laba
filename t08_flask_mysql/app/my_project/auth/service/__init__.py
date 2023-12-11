"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.registration_service import ClientService
from .orders.aviacompany_service import ClientTypeService
from .orders.pilot_service import PilotService
from .orders.air_hostess_service import AirHostessService
from .orders.aeroport_service import AeroportService
from .orders.dispatcher_service import DispatcherService
from .orders.marshrut_service import MarshrutService
from .orders.route_service import RouteService
from .orders.airplane_service import AirplaneService
from .orders.flight_service import FlightService
from .orders.dispatcher_has_flight_service import DispatcherHasFlightService
from .orders.pilot_has_flight_service import PilotHasFlightService
from .orders.air_hostess_has_flight_service import AirHostessHasFlightService
# додати всі сервіси

client_service = ClientService()
client_type_service = ClientTypeService()
pilot_service = PilotService()
air_hostess_service = AirHostessService()
aeroport_service = AeroportService()
dispatcher_service = DispatcherService()
marshrut_service = MarshrutService()
route_service = RouteService()
airplane_service = AirplaneService()
flight_service = FlightService()
dispatcher_has_flight_service = DispatcherHasFlightService()
pilot_has_flight_service = PilotHasFlightService()
air_hostess_has_flight_service = AirHostessHasFlightService()
