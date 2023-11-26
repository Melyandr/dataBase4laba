"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.registration_dao import ClientDAO
from .orders.aviacompany_dao import ClientTypeDAO
from .orders.pilot_dao import PilotDAO
from .orders.air_hostess_dao import AirHostessDao
from .orders.aeroport_dao import AeroportDAO
from .orders.dispatcher_dao import DispatcherDAO
from .orders.marshrut_dao import MarshrutDAO
from .orders.route_dao import RouteDAO
from .orders.airplane_dao import AirplaneDAO
from .orders.flight_dao import FlightDAO
from .orders.dispatcher_has_flight_dao import DispatcherHasFlightDAO
from .orders.pilot_has_flight_dao import PilotHasFlightDAO
from .orders.air_hostess_has_flight_dao import AirHostessHasFlightDAO

client_dao = ClientDAO()
client_type_dao = ClientTypeDAO()
pilot_dao = PilotDAO()
air_hostess_dao = AirHostessDao()
aeroport_dao = AeroportDAO()
dispatcher_dao = DispatcherDAO()
marshrut_dao = MarshrutDAO()
route_dao = RouteDAO()
airplane_dao = AirplaneDAO()
flight_dao = FlightDAO()
dispatcher_has_flight_dao=DispatcherHasFlightDAO()
pilot_has_flight_dao = PilotHasFlightDAO()
air_hostess_has_flight_dao = AirHostessHasFlightDAO()